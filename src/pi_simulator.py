"""Simulador de exportaciones AVEVA PI System para laboratorios de mantenimiento."""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

RANDOM_STATE = 42
PI_COLUMNS = ["Timestamp", "Tag", "Value", "Unit", "Quality"]

TAG_UNITS = {
    "PUMP101.BEARING_TEMP": "°C",
    "PUMP101.VIBRATION_RMS": "mm/s",
    "PUMP101.DISCHARGE_PRESS": "bar",
    "PUMP101.MOTOR_CURRENT": "A",
    "PUMP101.FLOW_RATE": "m3/h",
    "PUMP101.SPEED_RPM": "rpm",
    "PUMP102.BEARING_TEMP": "°C",
    "PUMP102.VIBRATION_RMS": "mm/s",
    "MILL201.TEMP_OUTLET": "°C",
    "MILL201.POWER_KW": "kW",
}


def _rng() -> np.random.Generator:
    return np.random.default_rng(RANDOM_STATE)


def generate_pi_export(
    tags: Iterable[str],
    start: datetime,
    end: datetime,
    freq: str = "1h",
    base_values: dict[str, float] | None = None,
    noise_std: float = 0.5,
    bad_quality_rate: float = 0.02,
) -> pd.DataFrame:
    """Genera un export PI en formato largo (Timestamp, Tag, Value, Unit, Quality)."""
    rng = _rng()
    timestamps = pd.date_range(start=start, end=end, freq=freq)
    defaults = {
        "PUMP101.BEARING_TEMP": 65.0,
        "PUMP101.VIBRATION_RMS": 2.5,
        "PUMP101.DISCHARGE_PRESS": 12.0,
        "PUMP101.MOTOR_CURRENT": 45.0,
        "PUMP101.FLOW_RATE": 120.0,
        "PUMP101.SPEED_RPM": 1480.0,
        "PUMP102.BEARING_TEMP": 62.0,
        "PUMP102.VIBRATION_RMS": 2.1,
        "MILL201.TEMP_OUTLET": 85.0,
        "MILL201.POWER_KW": 450.0,
    }
    if base_values:
        defaults.update(base_values)

    rows: list[dict] = []
    for tag in tags:
        base = defaults.get(tag, 10.0)
        unit = TAG_UNITS.get(tag, "-")
        values = base + rng.normal(0, noise_std, size=len(timestamps))
        qualities = np.where(rng.random(len(timestamps)) < bad_quality_rate, "BAD", "GOOD")
        for ts, val, qual in zip(timestamps, values, qualities, strict=True):
            rows.append(
                {
                    "Timestamp": ts,
                    "Tag": tag,
                    "Value": round(float(val), 3),
                    "Unit": unit,
                    "Quality": qual,
                }
            )
    return pd.DataFrame(rows, columns=PI_COLUMNS)


def inject_degradation(
    df: pd.DataFrame,
    tag: str,
    slope_per_day: float = 0.05,
    start_fraction: float = 0.3,
) -> pd.DataFrame:
    """Agrega tendencia de degradación lineal a un tag."""
    out = df.copy()
    mask = out["Tag"] == tag
    if not mask.any():
        return out

    idx = out.loc[mask].index
    n = len(idx)
    start_i = int(n * start_fraction)
    days = np.arange(n - start_i) / 24.0
    out.loc[idx[start_i:], "Value"] += slope_per_day * days
    return out


def inject_failures(
    df: pd.DataFrame,
    failure_events: list[dict],
) -> pd.DataFrame:
    """Marca ventanas de falla con Quality=BAD y picos de valor."""
    out = df.copy()
    for event in failure_events:
        tag = event["tag"]
        t0 = pd.Timestamp(event["timestamp"])
        duration = timedelta(hours=event.get("duration_hours", 4))
        spike = event.get("spike", 5.0)
        mask = (out["Tag"] == tag) & (out["Timestamp"] >= t0) & (out["Timestamp"] <= t0 + duration)
        out.loc[mask, "Quality"] = "BAD"
        out.loc[mask, "Value"] = out.loc[mask, "Value"] + spike
    return out


def pivot_pi_wide(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte export PI largo a formato ancho por timestamp."""
    good = df[df["Quality"] == "GOOD"].copy()
    wide = good.pivot_table(index="Timestamp", columns="Tag", values="Value", aggfunc="mean")
    return wide.sort_index()


def save_pi_csv(df: pd.DataFrame, path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path


def save_excel_template(
    path: str | Path,
    tags_df: pd.DataFrame,
    umbrales_df: pd.DataFrame | None = None,
    eventos_df: pd.DataFrame | None = None,
    extra_sheets: dict[str, pd.DataFrame] | None = None,
) -> Path:
    """Guarda plantilla Excel de ingeniería con hojas Tags, Umbrales, Eventos."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        tags_df.to_excel(writer, sheet_name="Tags", index=False)
        if umbrales_df is not None:
            umbrales_df.to_excel(writer, sheet_name="Umbrales", index=False)
        if eventos_df is not None:
            eventos_df.to_excel(writer, sheet_name="Eventos", index=False)
        if extra_sheets:
            for name, sheet_df in extra_sheets.items():
                sheet_df.to_excel(writer, sheet_name=name, index=False)
    return path


def default_tags_table(tags: list[str], asset_path: str = "Planta/Molienda/PUMP101") -> pd.DataFrame:
    """Tabla de metadatos de tags para Asset Framework."""
    return pd.DataFrame(
        {
            "Tag": tags,
            "AssetPath": [asset_path] * len(tags),
            "Componente": [
                "Rodamiento" if "TEMP" in t or "VIB" in t else "Proceso" for t in tags
            ],
            "Descripcion": [f"Sensor simulado {t}" for t in tags],
        }
    )


def default_umbrales_table(tags: list[str]) -> pd.DataFrame:
    """Umbrales de alerta por tag."""
    limits = {
        "PUMP101.BEARING_TEMP": (70, 80),
        "PUMP101.VIBRATION_RMS": (4.5, 7.1),
        "PUMP101.DISCHARGE_PRESS": (8, 15),
        "PUMP101.MOTOR_CURRENT": (55, 65),
    }
    rows = []
    for tag in tags:
        alerta, critico = limits.get(tag, (50, 60))
        rows.append({"Tag": tag, "Alerta": alerta, "Critico": critico, "Unidad": TAG_UNITS.get(tag, "-")})
    return pd.DataFrame(rows)


def generate_failure_log(equipos: list[str], n_failures: int = 8) -> pd.DataFrame:
    """Genera historial de fallas para análisis MTBF/MTTR."""
    rng = _rng()
    start = datetime(2024, 1, 1)
    rows = []
    for equipo in equipos:
        t = start
        for _ in range(n_failures):
            t += timedelta(hours=float(rng.integers(200, 800)))
            mttr = float(rng.integers(2, 24))
            rows.append(
                {
                    "Equipo": equipo,
                    "Falla_Inicio": t,
                    "Falla_Fin": t + timedelta(hours=mttr),
                    "MTTR_horas": mttr,
                    "Modo_Falla": rng.choice(["Sello", "Rodamiento", "Cavitación", "Motor"]),
                }
            )
    return pd.DataFrame(rows).sort_values("Falla_Inicio").reset_index(drop=True)


def generate_weibull_lifetimes(n: int = 50, shape: float = 2.2, scale: float = 5000) -> pd.DataFrame:
    """Genera vidas útil de rodamientos para ajuste Weibull (horas)."""
    rng = _rng()
    lifetimes = rng.weibull(shape, n) * scale
    return pd.DataFrame({"Rodamiento_ID": [f"BRG-{i:03d}" for i in range(1, n + 1)], "Vida_horas": lifetimes})


def generate_turno_csv(
    start: datetime | None = None,
    hours: int = 48,
    equipos: list[str] | None = None,
) -> pd.DataFrame:
    """Genera lecturas de turno para el Módulo 0 (formato simple para principiantes)."""
    rng = _rng()
    start = start or datetime(2025, 3, 1, 8, 0)
    equipos = equipos or ["PUMP101", "PUMP102", "MILL201"]
    variables = {
        "TEMP_RODAMIENTO": ("°C", 70.0, 3.0),
        "VIBRACION_RMS": ("mm/s", 2.5, 0.3),
    }
    rows: list[dict] = []
    for h in range(hours):
        ts = start + timedelta(hours=h)
        for equipo in equipos:
            for var, (unidad, base, noise) in variables.items():
                if equipo == "MILL201" and var == "VIBRACION_RMS":
                    continue
                valor = round(base + rng.normal(0, noise), 2)
                if equipo == "MILL201":
                    valor = round(85 + rng.normal(0, 2), 2)
                quality = "BAD" if rng.random() < 0.03 else "GOOD"
                rows.append(
                    {
                        "Timestamp": ts,
                        "Equipo": equipo,
                        "Variable": var,
                        "Valor": valor,
                        "Unidad": unidad,
                        "Quality": quality,
                    }
                )
    return pd.DataFrame(rows)


def save_turno_csv(path: str | Path, **kwargs) -> Path:
    """Guarda CSV de lecturas de turno para Módulo 0."""
    df = generate_turno_csv(**kwargs)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path


def generate_ecosystem_seed() -> dict[str, pd.DataFrame]:
    """Genera datos coherentes para Módulo B (ecosistema de datos)."""
    equipos = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "codigo": ["PUMP101", "PUMP102", "MILL201"],
            "area": ["Molienda", "Molienda", "Molienda"],
            "tipo": ["Bomba centrífuga", "Bomba centrífuga", "Molino SAG"],
        }
    )

    start = datetime(2025, 1, 1)
    end = datetime(2025, 1, 14)
    tags = ["PUMP101.BEARING_TEMP", "PUMP101.VIBRATION_RMS", "PUMP102.VIBRATION_RMS", "MILL201.POWER_KW"]
    lecturas_long = generate_pi_export(tags, start, end, freq="6h")
    lecturas_long = inject_degradation(lecturas_long, "PUMP101.VIBRATION_RMS", slope_per_day=0.04, start_fraction=0.5)

    lecturas_pi = lecturas_long.rename(
        columns={"Timestamp": "timestamp", "Tag": "tag", "Value": "valor", "Unit": "unidad", "Quality": "quality"}
    )
    lecturas_pi["equipo_codigo"] = lecturas_pi["tag"].str.split(".").str[0]

    eventos_raw = generate_failure_log(["PUMP101", "PUMP102"], n_failures=5)
    eventos_mantenimiento = pd.DataFrame(
        {
            "equipo_id": eventos_raw["Equipo"].map({"PUMP101": 1, "PUMP102": 2, "MILL201": 3}),
            "inicio": eventos_raw["Falla_Inicio"],
            "fin": eventos_raw["Falla_Fin"],
            "modo_falla": eventos_raw["Modo_Falla"],
            "mttr_horas": eventos_raw["MTTR_horas"],
        }
    )

    wide = pivot_pi_wide(lecturas_long)
    dashboard = wide.resample("1D").mean().reset_index()
    dashboard["Timestamp"] = dashboard["Timestamp"].dt.strftime("%Y-%m-%d")
    dashboard_fuente = dashboard.melt(id_vars=["Timestamp"], var_name="Tag", value_name="Valor")
    dashboard_fuente["Equipo"] = dashboard_fuente["Tag"].str.split(".").str[0]

    return {
        "equipos": equipos,
        "lecturas_pi": lecturas_pi,
        "eventos_mantenimiento": eventos_mantenimiento,
        "lecturas_pi_export": lecturas_long,
        "dashboard_fuente": dashboard_fuente,
    }


def generate_predictive_dataset(n_hours: int = 500, failure_rate: float = 0.08) -> pd.DataFrame:
    """Genera dataset multivariable con etiqueta de falla para Módulo C."""
    rng = _rng()
    start = datetime(2024, 6, 1)
    tags = [
        "PUMP101.BEARING_TEMP",
        "PUMP101.VIBRATION_RMS",
        "PUMP101.DISCHARGE_PRESS",
        "PUMP101.MOTOR_CURRENT",
    ]
    df = generate_pi_export(tags, start, start + timedelta(hours=n_hours - 1), freq="1h")
    df = inject_degradation(df, "PUMP101.VIBRATION_RMS", slope_per_day=0.08, start_fraction=0.35)
    df = inject_degradation(df, "PUMP101.BEARING_TEMP", slope_per_day=0.04, start_fraction=0.4)

    wide = pivot_pi_wide(df).dropna()
    wide = wide.reset_index()

    n = len(wide)
    n_failures = max(1, int(n * failure_rate))
    failure_idx = set(rng.choice(n, size=n_failures, replace=False))

    labels = []
    for i in range(n):
        if i in failure_idx:
            labels.append(1)
        elif i + 1 in failure_idx or i - 1 in failure_idx:
            labels.append(1)
        else:
            labels.append(0)
    wide["falla"] = labels

    wide["vib_media_24h"] = wide["PUMP101.VIBRATION_RMS"].rolling(24, min_periods=1).mean()
    wide["temp_pendiente_24h"] = wide["PUMP101.BEARING_TEMP"].diff(24).fillna(0)
    wide["presion_pct"] = wide["PUMP101.DISCHARGE_PRESS"].rank(pct=True)

    return wide.dropna().reset_index(drop=True)
