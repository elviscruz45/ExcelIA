"""Genera datos simulados PI para Lab 08 — IA mantenimiento."""

import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pi_simulator import (  # noqa: E402
    default_tags_table,
    default_umbrales_table,
    generate_failure_log,
    generate_pi_export,
    inject_degradation,
    save_excel_template,
    save_pi_csv,
)

LAB_DIR = Path(__file__).resolve().parent
TAGS = [
    "PUMP101.BEARING_TEMP",
    "PUMP101.VIBRATION_RMS",
    "PUMP102.BEARING_TEMP",
    "PUMP102.VIBRATION_RMS",
    "MILL201.POWER_KW",
]


def main() -> None:
    (LAB_DIR / "outputs").mkdir(exist_ok=True)
    df = generate_pi_export(TAGS, datetime(2024, 10, 1), datetime(2025, 4, 30), freq="2h")
    df = inject_degradation(df, "PUMP101.VIBRATION_RMS", slope_per_day=0.1, start_fraction=0.35)
    df = inject_degradation(df, "PUMP101.BEARING_TEMP", slope_per_day=0.05, start_fraction=0.4)
    eventos = generate_failure_log(["PUMP101", "PUMP102", "MILL201"], n_failures=6)

    save_pi_csv(df, LAB_DIR / "data" / "datos_exportados_PI.csv")
    save_excel_template(
        LAB_DIR / "excel" / "modelo_ingenieria.xlsx",
        tags_df=default_tags_table(TAGS, asset_path="Planta/Molienda"),
        umbrales_df=default_umbrales_table(TAGS),
        eventos_df=eventos,
    )
    print("Lab 08: datos generados correctamente.")


if __name__ == "__main__":
    main()
