"""Genera los 4 notebooks del Módulo C — IA Predictiva."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOD_DIR = ROOT / "05_ia_predictiva"
KERNEL = {"display_name": "ExcelA (uv)", "language": "python", "name": "excela"}

SETUP = """import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

MOD_DIR = Path.cwd()
os.chdir(MOD_DIR)
DATA_DIR = MOD_DIR / "data"
OUTPUT_DIR = MOD_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
DATA_PATH = DATA_DIR / "dataset_predictivo.csv"
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
        "metadata": {"kernelspec": KERNEL, "language_info": {"name": "python"}},
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def save_nb(path: Path, cells: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notebook(cells), indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def nb05() -> list[dict]:
    return [
        md("# IV_05 — De mantenimiento reactivo a predictivo"),
        md(
            "## 1. Objetivo\n\n"
            "Entender la escalera de madurez de mantenimiento y preparar variables "
            "de condición para análisis predictivo en plantas concentradoras."
        ),
        md(
            "## 2. Concepto — Escalera de mantenimiento\n\n"
            "| Nivel | Descripción | Ejemplo PUMP101 |\n"
            "|-------|-------------|------------------|\n"
            "| Reactivo | Reparar tras falla | Cambio rodamiento post-falla |\n"
            "| Preventivo | Por horas/calendario | Lubricación cada 2000 h |\n"
            "| Predictivo | Por condición | Alerta por vibración creciente |\n"
            "| Prescriptivo | Recomendación optimizada | IA prioriza intervención |"
        ),
        code(SETUP),
        code(
            """df = pd.read_csv(DATA_PATH, parse_dates=["Timestamp"])
print(f"Registros: {len(df)} | Fallas: {df['falla'].sum()}")
df.head()
"""
        ),
        md("## 3. Variables de condición"),
        code(
            """# Variables clave en concentradora
variables = [
    "PUMP101.BEARING_TEMP",      # °C — rodamiento
    "PUMP101.VIBRATION_RMS",     # mm/s — vibración
    "PUMP101.DISCHARGE_PRESS",   # bar — proceso
    "PUMP101.MOTOR_CURRENT",     # A — carga motor
]
print("Variables de condición:", variables)
df[variables].describe()
"""
        ),
        md("## 4. Feature engineering"),
        code(
            """# Features derivadas (ya en dataset; aquí se explican)
feature_cols = ["vib_media_24h", "temp_pendiente_24h", "presion_pct"]
print("Features derivadas:")
for f in feature_cols:
    print(f"  - {f}")

df[["PUMP101.VIBRATION_RMS", "vib_media_24h", "falla"]].tail(10)
"""
        ),
        md(
            "## 5. Ejercicio práctico\n\n"
            "¿Por qué la vibración media móvil de 24h es más útil que un solo valor instantáneo "
            "para detectar degradación?"
        ),
        md(
            "## 6. Resumen y siguiente paso\n\n"
            "- El predictivo usa tendencias, no solo umbrales puntuales.\n"
            "- Feature engineering transforma sensores en señales de degradación.\n"
            "- La etiqueta `falla` se deriva de eventos reales o simulados.\n\n"
            "**Siguiente:** `IV_06_ml_clasificacion_fallas.ipynb`"
        ),
    ]


def nb06() -> list[dict]:
    return [
        md("# IV_06 — ML: clasificación de fallas"),
        md(
            "## 1. Objetivo\n\n"
            "Entrenar un clasificador para anticipar fallas en PUMP101 usando variables "
            "de condición multivariable."
        ),
        md(
            "## 2. Concepto\n\n"
            "**Clasificación binaria:** predecir `falla=1` (inminente) vs `falla=0` (normal).\n\n"
            "**Costo industrial:**\n"
            "- Falso positivo → parada innecesaria, pérdida de producción.\n"
            "- Falso negativo → falla no detectada, daño mayor."
        ),
        code(
            SETUP
            + """
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from sklearn.model_selection import train_test_split
"""
        ),
        code(
            """df = pd.read_csv(DATA_PATH, parse_dates=["Timestamp"])
features = [
    "PUMP101.BEARING_TEMP", "PUMP101.VIBRATION_RMS",
    "PUMP101.DISCHARGE_PRESS", "PUMP101.MOTOR_CURRENT",
    "vib_media_24h", "temp_pendiente_24h", "presion_pct",
]
X = df[features]
y = df["falla"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
y_prob = modelo.predict_proba(X_test)[:, 1]

print(classification_report(y_test, y_pred, target_names=["Normal", "Falla"]))
"""
        ),
        md("## 3. Visualizaciones"),
        code(
            """fig, axes = plt.subplots(1, 3, figsize=(15, 4))

cm = confusion_matrix(y_test, y_pred)
axes[0].imshow(cm, cmap="Blues")
axes[0].set_xticks([0, 1]); axes[0].set_yticks([0, 1])
axes[0].set_xticklabels(["Normal", "Falla"]); axes[0].set_yticklabels(["Normal", "Falla"])
for i in range(2):
    for j in range(2):
        axes[0].text(j, i, cm[i, j], ha="center", va="center")
axes[0].set_title("Matriz de confusión")

imp = pd.Series(modelo.feature_importances_, index=features).sort_values()
imp.plot(kind="barh", ax=axes[1], color="teal")
axes[1].set_title("Importancia de features")

fpr, tpr, _ = roc_curve(y_test, y_prob)
axes[1].set_xlabel("")
axes[2].plot(fpr, tpr, label=f"AUC={auc(fpr, tpr):.3f}")
axes[2].plot([0, 1], [0, 1], "k--")
axes[2].set_xlabel("FPR"); axes[2].set_ylabel("TPR")
axes[2].set_title("Curva ROC")
axes[2].legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "ml_clasificacion.png", dpi=150)
print("Gráfico guardado.")
"""
        ),
        md(
            "## 4. Interpretación para mantenimiento\n\n"
            "La vibración RMS y su media móvil suelen ser los predictores dominantes. "
            "Priorizar monitoreo de rodamiento cuando importancia > 20%."
        ),
        md(
            "## 5. Ejercicio práctico\n\n"
            "Si el recall de falla es 0.85, ¿qué significa para el planificador de mantenimiento?"
        ),
        md(
            "## 6. Resumen y siguiente paso\n\n"
            "- Random Forest maneja bien datos tabulares industriales.\n"
            "- Evaluar recall vs precisión según costo de parada.\n"
            "- Importancia de features guía inversiones en sensores.\n\n"
            "**Siguiente:** `IV_07_anomalias_y_rul.ipynb`"
        ),
    ]


def nb07() -> list[dict]:
    return [
        md("# IV_07 — Anomalías y vida útil remanente (RUL)"),
        md(
            "## 1. Objetivo\n\n"
            "Detectar anomalías en vibración y estimar RUL (Remaining Useful Life) "
            "para programar intervenciones antes de la falla funcional."
        ),
        md(
            "## 2. Concepto\n\n"
            "- **Umbral fijo (ISO 10816):** simple pero no detecta degradación gradual.\n"
            "- **Z-score:** alerta si valor > μ + 2σ.\n"
            "- **Isolation Forest:** detecta patrones multivariados anómalos.\n"
            "- **RUL:** horas estimadas hasta intervención recomendada."
        ),
        code(
            SETUP
            + """
from sklearn.ensemble import GradientBoostingRegressor, IsolationForest
from sklearn.model_selection import train_test_split
"""
        ),
        code(
            """df = pd.read_csv(DATA_PATH, parse_dates=["Timestamp"])
vib = df["PUMP101.VIBRATION_RMS"]

# Detección por z-score
media, std = vib.mean(), vib.std()
umbral_z = media + 2 * std
anomalias_z = vib > umbral_z
print(f"Umbral z-score: {umbral_z:.2f} mm/s | Anomalías: {anomalias_z.sum()}")
"""
        ),
        code(
            """# Isolation Forest multivariable
feat_cols = ["PUMP101.VIBRATION_RMS", "PUMP101.BEARING_TEMP", "vib_media_24h"]
iso = IsolationForest(contamination=0.05, random_state=42)
df["anomalia"] = iso.fit_predict(df[feat_cols])
df["anomalia_label"] = df["anomalia"].map({1: "Normal", -1: "Anomalía"})
print(df["anomalia_label"].value_counts())
"""
        ),
        code(
            """# RUL simplificado: regresión sobre índice temporal
df["horas_operacion"] = np.arange(len(df))
rul_target = np.clip(500 - df["PUMP101.VIBRATION_RMS"] * 80 - df["PUMP101.BEARING_TEMP"] * 2, 10, 500)

X = df[["PUMP101.VIBRATION_RMS", "PUMP101.BEARING_TEMP", "vib_media_24h", "horas_operacion"]]
y = rul_target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rul_model = GradientBoostingRegressor(random_state=42)
rul_model.fit(X_train, y_train)
rul_pred = rul_model.predict(X_test)

rul_actual = float(rul_model.predict(X.iloc[[-1]])[0])
print(f"RUL estimado actual: {rul_actual:.0f} horas")
"""
        ),
        md("## 3. Visualización"),
        code(
            """fig, axes = plt.subplots(2, 1, figsize=(12, 8))

axes[0].plot(df["Timestamp"], vib, alpha=0.6, label="Vibración RMS")
axes[0].axhline(umbral_z, color="red", linestyle="--", label="Umbral z-score")
anom_idx = df[df["anomalia"] == -1]
axes[0].scatter(anom_idx["Timestamp"], anom_idx["PUMP101.VIBRATION_RMS"], color="red", s=20, label="Anomalía")
axes[0].set_ylabel("mm/s")
axes[0].set_title("Detección de anomalías — PUMP101")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].scatter(y_test, rul_pred, alpha=0.5)
axes[1].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
axes[1].set_xlabel("RUL real (h)")
axes[1].set_ylabel("RUL predicho (h)")
axes[1].set_title("Modelo RUL")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "anomalias_rul.png", dpi=150)
"""
        ),
        md(
            "## 4. Interpretación para mantenimiento\n\n"
            "Combinar umbral ISO + detección estadística reduce falsas alarmas. "
            "RUL < 72 h sugiere programar inspección predictiva en la próxima ventana de parada."
        ),
        md(
            "## 5. Resumen y siguiente paso\n\n"
            "- Anomalías multivariables captan degradación que un solo umbral no ve.\n"
            "- RUL traduce sensores en tiempo hasta intervención.\n"
            "- Conectar con Lab 06 (vibración) para umbrales ISO.\n\n"
            "**Siguiente:** `IV_08_caso_integrado_alertas.ipynb`"
        ),
    ]


def nb08() -> list[dict]:
    return [
        md("# IV_08 — Caso integrado: pipeline de alertas"),
        md(
            "## 1. Objetivo\n\n"
            "Integrar features, modelo ML, scoring de riesgo y priorización Pareto "
            "en un pipeline único para la línea de molienda."
        ),
        code(
            SETUP
            + """
from sklearn.ensemble import GradientBoostingRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
"""
        ),
        md("## 2. Pipeline completo"),
        code(
            """df = pd.read_csv(DATA_PATH, parse_dates=["Timestamp"])
features = [
    "PUMP101.BEARING_TEMP", "PUMP101.VIBRATION_RMS",
    "PUMP101.DISCHARGE_PRESS", "PUMP101.MOTOR_CURRENT",
    "vib_media_24h", "temp_pendiente_24h",
]
X = df[features]
y_clf = df["falla"]

# Modelo clasificación
clf = RandomForestClassifier(n_estimators=100, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y_clf, test_size=0.2, random_state=42, stratify=y_clf)
clf.fit(X_train, y_train)
prob_falla = clf.predict_proba(X)[:, 1]

# RUL y scoring
rul = np.clip(500 - df["PUMP101.VIBRATION_RMS"] * 80 - df["PUMP101.BEARING_TEMP"] * 2, 10, 500)
riesgo = np.clip(prob_falla * 100, 0, 100)

alertas = pd.DataFrame({
    "Timestamp": df["Timestamp"],
    "Equipo": "PUMP101",
    "Prob_Falla": prob_falla,
    "RUL_horas": rul,
    "Riesgo_pct": riesgo,
})
alertas.tail()
"""
        ),
        md("## 3. Priorización Pareto"),
        code(
            """# Ranking por riesgo (últimas 24 lecturas)
ultimas = alertas.tail(24).sort_values("Riesgo_pct", ascending=False)
ultimas["Riesgo_acum_pct"] = ultimas["Riesgo_pct"].cumsum() / ultimas["Riesgo_pct"].sum() * 100

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].bar(range(len(ultimas)), ultimas["Riesgo_pct"], color="coral")
axes[0].set_xticks(range(len(ultimas)))
axes[0].set_xticklabels(ultimas["Timestamp"].dt.strftime("%m-%d %Hh"), rotation=45, ha="right")
axes[0].set_ylabel("Riesgo %")
axes[0].set_title("Ranking de alertas — PUMP101")

axes[1].plot(ultimas["Riesgo_acum_pct"].values, "ko-")
axes[1].axhline(80, color="red", linestyle="--", label="80% Pareto")
axes[1].set_xlabel("Ranking")
axes[1].set_ylabel("% riesgo acumulado")
axes[1].set_title("Curva Pareto")
axes[1].legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "dashboard_riesgo.png", dpi=150)
"""
        ),
        md("## 4. Exportación"),
        code(
            """out_alertas = OUTPUT_DIR / "alertas_priorizadas.csv"
ultimas.to_csv(out_alertas, index=False)
print(f"Alertas exportadas: {out_alertas}")

resumen = pd.DataFrame({
    "Metrica": ["Riesgo_max_pct", "RUL_min_h", "Prob_falla_max"],
    "Valor": [ultimas["Riesgo_pct"].max(), ultimas["RUL_horas"].min(), ultimas["Prob_Falla"].max()],
})
resumen
"""
        ),
        md(
            "## 5. Interpretación para mantenimiento\n\n"
            "PUMP101 concentra el mayor riesgo en las últimas 24 h de operación simulada. "
            "Ejecutar inspección de vibración (espectro) antes de la falla funcional. "
            "Integrar alertas en PI AF y Supabase (Módulo B) para trazabilidad."
        ),
        md(
            "## 6. Resumen — Módulo C completo\n\n"
            "- Pipeline: datos → features → ML → scoring → Pareto → acción.\n"
            "- IA predictiva complementa, no reemplaza, el criterio del ingeniero.\n"
            "- Profundización: Labs 06–08 en la raíz del proyecto.\n\n"
            "**Curso Minería 5.0 (6h) completado.**"
        ),
    ]


BUILDERS = {
    "IV_05_mantenimiento_predictivo.ipynb": nb05,
    "IV_06_ml_clasificacion_fallas.ipynb": nb06,
    "IV_07_anomalias_y_rul.ipynb": nb07,
    "IV_08_caso_integrado_alertas.ipynb": nb08,
}


def main() -> None:
    for name, builder in BUILDERS.items():
        path = MOD_DIR / name
        save_nb(path, builder())
        print(f"Creado: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
