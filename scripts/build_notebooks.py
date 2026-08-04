"""Genera los 8 notebooks Jupyter del curso PI System."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

KERNEL = {"display_name": "ExcelA (uv)", "language": "python", "name": "excela"}

SETUP_CELL = """import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

LAB_DIR = Path.cwd()
os.chdir(LAB_DIR)
OUTPUT_DIR = LAB_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
EXCEL_DIR = LAB_DIR / "excel"
DATA_PATH = LAB_DIR / "data" / "datos_exportados_PI.csv"
"""


def md(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(keepends=True)}


def code(text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": text.splitlines(keepends=True),
    }


def notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": KERNEL,
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def save_nb(path: Path, cells: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notebook(cells), indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def intro(problema: str, activo: str, origen: str, objetivo: str) -> dict:
    return md(
        f"""# 1. Introducción

**Problema industrial:** {problema}

**Activo analizado:** {activo}

**Origen de datos:** {origen}

**Objetivo del análisis:** {objetivo}
"""
    )


def libs(extra: str = "") -> list[dict]:
    cells = [md("# 2. Carga de librerías"), code(SETUP_CELL + extra)]
    return cells


def load_pi() -> list[dict]:
    return [
        md("# 3. Lectura de datos PI System\n\nSimulamos una exportación del historiador PI con columnas: `Timestamp`, `Tag`, `Value`, `Unit`, `Quality`."),
        code(
            """df_pi = pd.read_csv(DATA_PATH, parse_dates=["Timestamp"])
print(f"Registros cargados: {len(df_pi):,}")
df_pi.head(10)
"""
        ),
    ]


def explore() -> list[dict]:
    return [
        md("# 4. Exploración del dato"),
        code(
            """print("Columnas:", df_pi.columns.tolist())
print("\\nEstadísticas por tag:")
display(df_pi.groupby("Tag")["Value"].describe())

calidad = df_pi["Quality"].value_counts(normalize=True) * 100
print("\\nCalidad del dato (%):")
print(calidad.round(2))

faltantes = df_pi["Value"].isna().sum()
print(f"\\nValores faltantes: {faltantes}")

df_good = df_pi[df_pi["Quality"] == "GOOD"].copy()
tendencia = df_good.groupby("Tag")["Value"].agg(["mean", "std", "min", "max"])
print("\\nTendencia central por tag:")
display(tendencia)
"""
        ),
    ]


def export_common(extra_excel: str = "") -> list[dict]:
    return [
        md("# 7. Exportación"),
        code(
            f"""resultados_path = OUTPUT_DIR / "resultado_analisis.csv"
graficos_path = OUTPUT_DIR / "graficos.png"
excel_resultado = EXCEL_DIR / "modelo_resultado.xlsx"

resultados_export.to_csv(resultados_path, index=False)
{extra_excel}
plt.tight_layout()
plt.savefig(graficos_path, dpi=150, bbox_inches="tight")
print(f"CSV exportado: {{resultados_path}}")
print(f"Gráficos exportados: {{graficos_path}}")
print(f"Excel exportado: {{excel_resultado}}")
"""
        ),
    ]


def interpretacion(texto: str) -> dict:
    return md(f"""# 8. Interpretación ingenieril

## Interpretación para mantenimiento

{texto}
""")


# --- Lab 01 ---
def lab01() -> list[dict]:
    cells = [
        intro(
            "Monitoreo de condición de bomba de alimentación al molino.",
            "Bomba centrífuga PUMP101 (alimentación molino).",
            "Exportación histórica simulada desde AVEVA PI Data Archive.",
            "Familiarizarse con el formato de exportación PI, filtrar por calidad y analizar tendencias de temperatura de rodamiento.",
        ),
        *libs(),
        *load_pi(),
        *explore(),
        md("# 5. Análisis matemático\n\nFiltrado por calidad, resampleo horario y estadísticas de proceso."),
        code(
            """tag_temp = "PUMP101.BEARING_TEMP"
df_temp = df_good[df_good["Tag"] == tag_temp].set_index("Timestamp")["Value"]
serie_h = df_temp.resample("1h").mean().dropna()

media_proceso = serie_h.mean()
desv_proceso = serie_h.std()
p95 = serie_h.quantile(0.95)

resultados_export = pd.DataFrame({
    "Metrica": ["Media", "Desv_Est", "P95", "Registros_GOOD"],
    "Valor": [media_proceso, desv_proceso, p95, len(df_temp)],
    "Unidad": ["°C", "°C", "°C", "conteo"],
})
display(resultados_export)
"""
        ),
        md("# 6. Visualizaciones"),
        code(
            """fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(serie_h.index, serie_h.values, color="steelblue", linewidth=1)
axes[0].axhline(media_proceso, color="red", linestyle="--", label=f"Media={media_proceso:.1f}°C")
axes[0].set_title("Tendencia PUMP101.BEARING_TEMP")
axes[0].set_xlabel("Fecha")
axes[0].set_ylabel("°C")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

df_pi["Quality"].value_counts().plot(kind="bar", ax=axes[1], color=["green", "orange"])
axes[1].set_title("Distribución de calidad PI")
axes[1].set_ylabel("Conteo")
"""
        ),
        *export_common(
            'with pd.ExcelWriter(excel_resultado, engine="openpyxl") as writer:\n    resultados_export.to_excel(writer, sheet_name="Resumen", index=False)\n    tendencia.reset_index().to_excel(writer, sheet_name="Tendencia_Tags", index=False)\n'
        ),
        interpretacion(
            "La temperatura de rodamiento se mantiene en rango operativo con incremento gradual en el último tercio del periodo. "
            "Se recomienda validar lubricación y alinear inspección de termografía en la próxima parada programada."
        ),
    ]
    return cells


# --- Lab 02 ---
def lab02() -> list[dict]:
    cells = [
        intro(
            "Organización de activos y sensores en PI Asset Framework.",
            "Jerarquía Planta > Área Molienda > PUMP101 > Sensores.",
            "Tags asociados a rutas de activo en PI AF (simulado).",
            "Agrupar mediciones por componente y construir dashboard multi-tag.",
        ),
        *libs(),
        *load_pi(),
        *explore(),
        md("# 5. Análisis matemático\n\nMapeo tag → componente usando metadatos del modelo de ingeniería."),
        code(
            """tags_meta = pd.read_excel(EXCEL_DIR / "modelo_ingenieria.xlsx", sheet_name="Tags")
df_join = df_good.merge(tags_meta, on="Tag", how="left")

resumen_componente = (
    df_join.groupby(["AssetPath", "Componente"])["Value"]
    .agg(["count", "mean", "std"])
    .reset_index()
    .rename(columns={"count": "N_muestras", "mean": "Promedio", "std": "Desv_Est"})
)
resultados_export = resumen_componente
display(resultados_export)
"""
        ),
        md("# 6. Visualizaciones"),
        code(
            """fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.ravel()

for ax, (tag, grupo) in zip(axes, df_join.groupby("Tag"), strict=False):
    g = grupo.set_index("Timestamp")["Value"].resample("6h").mean()
    ax.plot(g.index, g.values)
    ax.set_title(tag)
    ax.grid(True, alpha=0.3)

plt.suptitle("Dashboard multi-tag por componente — PUMP101")
"""
        ),
        *export_common(
            'with pd.ExcelWriter(excel_resultado, engine="openpyxl") as writer:\n    resultados_export.to_excel(writer, sheet_name="Por_Componente", index=False)\n    tags_meta.to_excel(writer, sheet_name="Tags", index=False)\n'
        ),
        interpretacion(
            "La estructura AF permite priorizar mantenimiento por componente. Rodamiento y proceso muestran variabilidad distinta; "
            "integrar alertas por componente mejora la trazabilidad de intervenciones."
        ),
    ]
    return cells


# --- Lab 03 ---
def lab03() -> list[dict]:
    cells = [
        intro(
            "Integración entre modelos de ingeniería en Excel y análisis en Python.",
            "PUMP101 — modelo híbrido Excel + Python.",
            "Mediciones PI y parámetros de diseño en `modelo_ingenieria.xlsx`.",
            "Calcular KPIs de eficiencia y comparar medición vs. modelo.",
        ),
        *libs(),
        *load_pi(),
        *explore(),
        md("# 5. Análisis matemático\n\nCálculo de KPIs: eficiencia volumétrica y desviación vs. diseño."),
        code(
            """umbrales = pd.read_excel(EXCEL_DIR / "modelo_ingenieria.xlsx", sheet_name="Umbrales")
modelo = pd.read_excel(EXCEL_DIR / "modelo_ingenieria.xlsx", sheet_name="Modelo")

wide = df_good.pivot_table(index="Timestamp", columns="Tag", values="Value", aggfunc="mean")
caudal_medido = wide["PUMP101.FLOW_RATE"].mean()
caudal_diseno = float(modelo.loc[modelo["Parametro"] == "Caudal_Diseno", "Valor"].iloc[0])
eficiencia = (caudal_medido / caudal_diseno) * 100

resultados_export = pd.DataFrame({
    "KPI": ["Caudal_Medido", "Caudal_Diseno", "Eficiencia_%"],
    "Valor": [caudal_medido, caudal_diseno, eficiencia],
})
display(resultados_export)
"""
        ),
        md("# 6. Visualizaciones"),
        code(
            """fig, ax = plt.subplots(figsize=(10, 5))
wide["PUMP101.FLOW_RATE"].resample("1D").mean().plot(ax=ax, label="Medido", color="steelblue")
ax.axhline(caudal_diseno, color="red", linestyle="--", label=f"Diseño={caudal_diseno:.0f} m3/h")
ax.set_title("Caudal medido vs. diseño")
ax.set_ylabel("m3/h")
ax.legend()
ax.grid(True, alpha=0.3)
"""
        ),
        *export_common(
            'with pd.ExcelWriter(excel_resultado, engine="openpyxl") as writer:\n    resultados_export.to_excel(writer, sheet_name="KPIs", index=False)\n    modelo.to_excel(writer, sheet_name="Modelo", index=False)\n    umbrales.to_excel(writer, sheet_name="Umbrales", index=False)\n'
        ),
        interpretacion(
            "La eficiencia por debajo del 100% sugiere revisar desgaste de impulsor o restricciones en succión. "
            "Actualizar el modelo Excel con los nuevos coeficientes calibrados desde PI."
        ),
    ]
    return cells


# --- Lab 04 ---
def lab04() -> list[dict]:
    cells = [
        intro(
            "Evaluación de confiabilidad operativa de línea de bombeo.",
            "PUMP101 y PUMP102 — línea de alimentación.",
            "Historial de eventos de falla registrados en PI / CMMS (simulado).",
            "Calcular MTBF, MTTR y disponibilidad por equipo.",
        ),
        *libs('from datetime import timedelta\n'),
        *load_pi(),
        *explore(),
        md("# 5. Análisis matemático\n\nCálculo de MTBF, MTTR y disponibilidad."),
        code(
            """eventos = pd.read_excel(EXCEL_DIR / "modelo_ingenieria.xlsx", sheet_name="Eventos", parse_dates=["Falla_Inicio", "Falla_Fin"])

metricas = []
for equipo, grp in eventos.groupby("Equipo"):
    grp = grp.sort_values("Falla_Inicio")
    mttr = grp["MTTR_horas"].mean()
    if len(grp) > 1:
        intervalos = grp["Falla_Inicio"].diff().dt.total_seconds() / 3600
        mtbf = intervalos.iloc[1:].mean()
    else:
        mtbf = np.nan
    disponibilidad = mtbf / (mtbf + mttr) if mtbf and not np.isnan(mtbf) else np.nan
    metricas.append({"Equipo": equipo, "MTBF_horas": mtbf, "MTTR_horas": mttr, "Disponibilidad": disponibilidad})

resultados_export = pd.DataFrame(metricas)
display(resultados_export)
"""
        ),
        md("# 6. Visualizaciones"),
        code(
            """fig, axes = plt.subplots(1, 2, figsize=(14, 5))

resultados_export.set_index("Equipo")[["MTBF_horas", "MTTR_horas"]].plot(
    kind="bar", ax=axes[0], color=["#2ecc71", "#e74c3c"]
)
axes[0].set_title("MTBF y MTTR por equipo")
axes[0].set_ylabel("Horas")
axes[0].tick_params(axis="x", rotation=0)

for equipo, grp in eventos.groupby("Equipo"):
    for _, row in grp.iterrows():
        axes[1].barh(equipo, row["MTTR_horas"], left=row["Falla_Inicio"].toordinal(), height=0.3, color="coral")
axes[1].set_title("Timeline de eventos de falla")
"""
        ),
        *export_common(
            'with pd.ExcelWriter(excel_resultado, engine="openpyxl") as writer:\n    resultados_export.to_excel(writer, sheet_name="MTBF_MTTR", index=False)\n    eventos.to_excel(writer, sheet_name="Eventos", index=False)\n'
        ),
        interpretacion(
            "PUMP101 presenta MTTR elevado asociado a fallas de rodamiento. Priorizar kit de repuesto en almacén "
            "y estandarizar procedimiento de cambio para reducir tiempo de reparación."
        ),
    ]
    return cells


# --- Lab 05 ---
def lab05() -> list[dict]:
    cells = [
        intro(
            "Análisis de vida útil de rodamientos en operación continua.",
            "Rodamientos BRG-001 a BRG-050 de bombas de molienda.",
            "Registro de horas hasta falla desde mantenimiento y PI (simulado).",
            "Ajustar distribución Weibull y estimar parámetros β (forma) y η (escala).",
        ),
        *libs("from scipy import stats\nfrom scipy.special import gamma as gamma_fn\n"),
        *load_pi(),
        *explore(),
        md("# 5. Análisis matemático\n\nAjuste Weibull de dos parámetros a vidas útil."),
        code(
            """vidas = pd.read_excel(EXCEL_DIR / "modelo_ingenieria.xlsx", sheet_name="Vidas_Weibull")
t = vidas["Vida_horas"].values

shape, loc, scale = stats.weibull_min.fit(t, floc=0)
print(f"β (forma) = {shape:.3f}")
print(f"η (escala) = {scale:.1f} horas")

t_medio = scale * gamma_fn(1 + 1 / shape)
resultados_export = pd.DataFrame({
    "Parametro": ["Beta_forma", "Eta_escala_h", "Vida_media_h", "N_muestras"],
    "Valor": [shape, scale, t_medio, len(t)],
})
display(resultados_export)
"""
        ),
        md("# 6. Visualizaciones"),
        code(
            """fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].hist(t, bins=15, density=True, alpha=0.7, color="steelblue", label="Datos")
x = np.linspace(0, t.max() * 1.2, 200)
axes[0].plot(x, stats.weibull_min.pdf(x, shape, loc=0, scale=scale), "r-", lw=2, label="Weibull ajustada")
axes[0].set_xlabel("Vida útil (h)")
axes[0].set_ylabel("Densidad")
axes[0].set_title("Histograma y PDF Weibull")
axes[0].legend()

axes[1].plot(x, stats.weibull_min.sf(x, shape, loc=0, scale=scale), color="darkgreen", lw=2)
axes[1].set_xlabel("Tiempo (h)")
axes[1].set_ylabel("Confiabilidad R(t)")
axes[1].set_title("Curva de confiabilidad")
axes[1].grid(True, alpha=0.3)
"""
        ),
        *export_common(
            'with pd.ExcelWriter(excel_resultado, engine="openpyxl") as writer:\n    resultados_export.to_excel(writer, sheet_name="Weibull", index=False)\n    vidas.to_excel(writer, sheet_name="Vidas", index=False)\n'
        ),
        interpretacion(
            "β > 1 indica fallas por desgaste. Programar reemplazo preventivo antes de η para maximizar disponibilidad "
            "sin incurrir en cambios prematuros."
        ),
    ]
    return cells


# --- Lab 06 ---
def lab06() -> list[dict]:
    cells = [
        intro(
            "Detección temprana de degradación mecánica por vibración.",
            "PUMP101 — sensores de vibración RMS y pico.",
            "Tendencias de vibración exportadas desde PI cada hora.",
            "Evaluar degradación y comparar con umbrales ISO 10816 (simulados).",
        ),
        *libs(),
        *load_pi(),
        *explore(),
        md("# 5. Análisis matemático\n\nTendencia de vibración RMS y clasificación por zona ISO."),
        code(
            """tag_vib = "PUMP101.VIBRATION_RMS"
umbrales = pd.read_excel(EXCEL_DIR / "modelo_ingenieria.xlsx", sheet_name="Umbrales")
umbral_alerta = float(umbrales.loc[umbrales["Tag"] == tag_vib, "Alerta"].iloc[0])
umbral_critico = float(umbrales.loc[umbrales["Tag"] == tag_vib, "Critico"].iloc[0])

vib = df_good[df_good["Tag"] == tag_vib].set_index("Timestamp")["Value"].sort_index()
vib_d = vib.resample("1D").mean()
pendiente = np.polyfit(np.arange(len(vib_d)), vib_d.values, 1)[0]

def clasificar_zona(val):
    if val < umbral_alerta:
        return "Aceptable"
    if val < umbral_critico:
        return "Alerta"
    return "Critico"

zona_actual = clasificar_zona(vib.iloc[-1])
resultados_export = pd.DataFrame({
    "Metrica": ["Vib_Actual", "Pendiente_diaria", "Umbral_Alerta", "Umbral_Critico", "Zona"],
    "Valor": [vib.iloc[-1], pendiente, umbral_alerta, umbral_critico, zona_actual],
})
display(resultados_export)
"""
        ),
        md("# 6. Visualizaciones"),
        code(
            """fig, axes = plt.subplots(2, 1, figsize=(12, 8))

axes[0].plot(vib.index, vib.values, color="steelblue", alpha=0.6, label="RMS horario")
axes[0].plot(vib_d.index, vib_d.values, color="navy", linewidth=2, label="Promedio diario")
axes[0].axhline(umbral_alerta, color="orange", linestyle="--", label="Alerta")
axes[0].axhline(umbral_critico, color="red", linestyle="--", label="Crítico")
axes[0].set_ylabel("mm/s")
axes[0].set_title("Tendencia de vibración PUMP101")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Mapa de calor: vibración por día y hora
vib_h = vib.to_frame("RMS")
vib_h["Dia"] = vib_h.index.dayofyear
vib_h["Hora"] = vib_h.index.hour
pivot = vib_h.pivot_table(index="Hora", columns="Dia", values="RMS", aggfunc="mean")
im = axes[1].imshow(pivot.values, aspect="auto", cmap="YlOrRd")
axes[1].set_title("Mapa de calor vibración (hora vs. día)")
axes[1].set_xlabel("Día del año")
axes[1].set_ylabel("Hora")
plt.colorbar(im, ax=axes[1], label="mm/s")
"""
        ),
        *export_common(
            'with pd.ExcelWriter(excel_resultado, engine="openpyxl") as writer:\n    resultados_export.to_excel(writer, sheet_name="Vibracion", index=False)\n    vib_d.reset_index().to_excel(writer, sheet_name="Serie_Diaria", index=False)\n'
        ),
        interpretacion(
            "El incremento sostenido de vibración RMS durante los últimos 30 días indica posible degradación del rodamiento. "
            "Se recomienda inspección predictiva (análisis de espectro) antes de la falla funcional."
        ),
    ]
    return cells


# --- Lab 07 ---
def lab07() -> list[dict]:
    cells = [
        intro(
            "Clasificación automática de estados normal/falla en equipos rotativos.",
            "PUMP101 — variables: temperatura, vibración, presión, corriente.",
            "Dataset multivariable etiquetado desde PI y eventos de falla (simulado).",
            "Entrenar un clasificador Random Forest para anticipar fallas.",
        ),
        *libs(
            """from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from sklearn.model_selection import train_test_split
"""
        ),
        *load_pi(),
        *explore(),
        md("# 5. Análisis matemático\n\nFeature engineering y clasificación binaria falla/normal."),
        code(
            """wide = df_good.pivot_table(index="Timestamp", columns="Tag", values="Value", aggfunc="mean").dropna()
features = wide[["PUMP101.BEARING_TEMP", "PUMP101.VIBRATION_RMS", "PUMP101.DISCHARGE_PRESS", "PUMP101.MOTOR_CURRENT"]]

# Etiqueta: falla si vibración > percentil 90
umbral_falla = features["PUMP101.VIBRATION_RMS"].quantile(0.90)
y = (features["PUMP101.VIBRATION_RMS"] > umbral_falla).astype(int)

X_train, X_test, y_train, y_test = train_test_split(features, y, test_size=0.25, random_state=42, stratify=y)
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
y_prob = modelo.predict_proba(X_test)[:, 1]

print(classification_report(y_test, y_pred, target_names=["Normal", "Falla"]))
importancia = pd.DataFrame({"Feature": features.columns, "Importancia": modelo.feature_importances_}).sort_values("Importancia", ascending=False)
resultados_export = importancia
display(resultados_export)
"""
        ),
        md("# 6. Visualizaciones"),
        code(
            """fig, axes = plt.subplots(1, 3, figsize=(16, 4))

cm = confusion_matrix(y_test, y_pred)
axes[0].imshow(cm, cmap="Blues")
axes[0].set_xticks([0, 1]); axes[0].set_yticks([0, 1])
axes[0].set_xticklabels(["Normal", "Falla"]); axes[0].set_yticklabels(["Normal", "Falla"])
for i in range(2):
    for j in range(2):
        axes[0].text(j, i, cm[i, j], ha="center", va="center", color="white" if cm[i,j]>cm.max()/2 else "black")
axes[0].set_title("Matriz de confusión")

axes[1].barh(importancia["Feature"], importancia["Importancia"], color="teal")
axes[1].set_title("Importancia de features")
axes[1].invert_yaxis()

fpr, tpr, _ = roc_curve(y_test, y_prob)
axes[2].plot(fpr, tpr, label=f"AUC={auc(fpr, tpr):.3f}")
axes[2].plot([0, 1], [0, 1], "k--")
axes[2].set_xlabel("FPR"); axes[2].set_ylabel("TPR")
axes[2].set_title("Curva ROC")
axes[2].legend()
"""
        ),
        *export_common(
            'with pd.ExcelWriter(excel_resultado, engine="openpyxl") as writer:\n    resultados_export.to_excel(writer, sheet_name="Importancia", index=False)\n    pd.DataFrame(classification_report(y_test, y_pred, output_dict=True)).to_excel(writer, sheet_name="Metricas")\n'
        ),
        interpretacion(
            "La vibración RMS es el predictor dominante de falla inminente. Integrar este modelo como alerta secundaria en PI AF "
            "permite priorizar órdenes de trabajo antes del evento crítico."
        ),
    ]
    return cells


# --- Lab 08 ---
def lab08() -> list[dict]:
    cells = [
        intro(
            "Pipeline de mantenimiento predictivo con IA para priorización de activos.",
            "Flota de bombas PUMP101 y PUMP102 — mantenimiento integrado.",
            "Series PI multivariable + historial de fallas + scoring de riesgo.",
            "Estimar RUL (vida útil remanente) y generar ranking de intervención (Pareto).",
        ),
        *libs(
            """from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
"""
        ),
        *load_pi(),
        *explore(),
        md("# 5. Análisis matemático\n\nPipeline: features → modelo RUL → scoring de riesgo."),
        code(
            """wide = df_good.pivot_table(index="Timestamp", columns="Tag", values="Value", aggfunc="mean").dropna()
wide = wide.reset_index()

# RUL simulado: función decreciente de vibración y temperatura
vib = wide["PUMP101.VIBRATION_RMS"].fillna(wide["PUMP101.VIBRATION_RMS"].mean())
temp = wide["PUMP101.BEARING_TEMP"].fillna(wide["PUMP101.BEARING_TEMP"].mean())
rul = np.clip(500 - 80 * vib - 2 * temp + np.random.default_rng(42).normal(0, 10, len(wide)), 10, 500)

feature_cols = [c for c in wide.columns if c != "Timestamp"]
X = wide[feature_cols].fillna(wide[feature_cols].mean())
y = rul

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rul_model = GradientBoostingRegressor(random_state=42)
rul_model.fit(X_train, y_train)
rul_pred = rul_model.predict(X_test)

ultimo = X.iloc[[-1]]
rul_actual = float(rul_model.predict(ultimo)[0])
riesgo = max(0, min(100, (1 - rul_actual / 500) * 100))

alertas = pd.DataFrame({
    "Activo": ["PUMP101", "PUMP102", "MILL201"],
    "RUL_horas_est": [rul_actual, rul_actual * 1.2, rul_actual * 0.8],
    "Riesgo_%": [riesgo, riesgo * 0.7, riesgo * 1.1],
}).sort_values("Riesgo_%", ascending=False)
resultados_export = alertas
display(resultados_export)
"""
        ),
        md("# 6. Visualizaciones"),
        code(
            """fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].scatter(y_test, rul_pred, alpha=0.5, color="steelblue")
axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
axes[0].set_xlabel("RUL real (h)")
axes[0].set_ylabel("RUL predicho (h)")
axes[0].set_title("Predicción de vida útil remanente")
axes[0].grid(True, alpha=0.3)

alertas_sorted = alertas.sort_values("Riesgo_%", ascending=False)
cum = alertas_sorted["Riesgo_%"].cumsum() / alertas_sorted["Riesgo_%"].sum() * 100
axes[1].bar(alertas_sorted["Activo"], alertas_sorted["Riesgo_%"], color="coral", label="Riesgo %")
ax2 = axes[1].twinx()
ax2.plot(alertas_sorted["Activo"], cum, "ko-", label="Pareto acumulado")
axes[1].set_title("Priorización de alertas — Pareto")
axes[1].set_ylabel("Riesgo %")
ax2.set_ylabel("% acumulado")
"""
        ),
        *export_common(
            'with pd.ExcelWriter(excel_resultado, engine="openpyxl") as writer:\n    resultados_export.to_excel(writer, sheet_name="Alertas", index=False)\n    pd.DataFrame({"RUL_actual_h": [rul_actual], "Riesgo_pct": [riesgo]}).to_excel(writer, sheet_name="Scoring", index=False)\n'
        ),
        interpretacion(
            "PUMP101 concentra el mayor riesgo según RUL estimado. Ejecutar inspección predictiva en las próximas 72 h "
            "y actualizar plan maestro de mantenimiento con la priorización Pareto generada."
        ),
    ]
    return cells


LAB_BUILDERS = {
    "01_PI_historiador_introduccion/01_PI_historiador_introduccion.ipynb": lab01,
    "02_PI_asset_framework/02_PI_asset_framework.ipynb": lab02,
    "03_excel_modelamiento_ingenieria/03_excel_modelamiento_ingenieria.ipynb": lab03,
    "04_MTBF_MTTR_analisis/04_MTBF_MTTR_analisis.ipynb": lab04,
    "05_Weibull_reliability/05_Weibull_reliability.ipynb": lab05,
    "06_vibracion_predictiva/06_vibracion_predictiva.ipynb": lab06,
    "07_machine_learning_fallas/07_machine_learning_fallas.ipynb": lab07,
    "08_IA_mantenimiento/08_IA_mantenimiento.ipynb": lab08,
}


def main() -> None:
    for rel_path, builder in LAB_BUILDERS.items():
        path = ROOT / rel_path
        save_nb(path, builder())
        print(f"Notebook creado: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
