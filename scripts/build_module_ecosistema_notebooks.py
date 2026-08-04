"""Genera los 4 notebooks del Módulo B — Ecosistema de Datos."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOD_DIR = ROOT / "04_ecosistema_datos"
KERNEL = {"display_name": "ExcelA (uv)", "language": "python", "name": "excela"}

SETUP = """import os
import sqlite3
from pathlib import Path

import pandas as pd

MOD_DIR = Path.cwd()
os.chdir(MOD_DIR)
DATA_DIR = MOD_DIR / "data"
OUTPUT_DIR = MOD_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "ecosistema_local.db"
"""

DB_HELPER = """
def init_local_db():
    \"\"\"Carga CSV en SQLite local (fallback sin Supabase).\"\"\"
    if DB_PATH.exists():
        return
    conn = sqlite3.connect(DB_PATH)
    pd.read_csv(DATA_DIR / "equipos.csv").to_sql("equipos", conn, if_exists="replace", index=False)
    pd.read_csv(DATA_DIR / "lecturas_pi_export.csv", parse_dates=["timestamp"]).to_sql(
        "lecturas_pi", conn, if_exists="replace", index=False
    )
    pd.read_csv(DATA_DIR / "eventos_mantenimiento.csv", parse_dates=["inicio", "fin"]).to_sql(
        "eventos_mantenimiento", conn, if_exists="replace", index=False
    )
    conn.close()

def get_supabase_client():
    from dotenv import load_dotenv
    load_dotenv(MOD_DIR / ".env")
    url, key = os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY")
    if url and key:
        from supabase import create_client
        return create_client(url, key)
    return None

def query_sql(sql, params=()):
    init_local_db()
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(sql, conn, params=params)
    conn.close()
    return df
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


def nb01() -> list[dict]:
    return [
        md("# IV_01 — Flujo de datos en Minería 5.0"),
        md(
            "## 1. Objetivo\n\n"
            "Comprender cómo viaja la información desde un sensor en planta hasta una decisión "
            "de mantenimiento, y qué capas tecnológicas intervienen."
        ),
        md(
            "## 2. Concepto\n\n"
            "### OT vs IT\n"
            "- **OT (Operational Technology):** PLC, DCS, sensores, actuadores — tiempo real.\n"
            "- **IT (Information Technology):** bases de datos, reportes, dashboards — análisis y gestión.\n\n"
            "### Modelo Purdue (simplificado)\n"
            "| Nivel | Ejemplo en concentradora |\n"
            "|-------|--------------------------|\n"
            "| 0 | Sensores: temperatura, vibración, presión |\n"
            "| 1 | PLC / control bomba y molino |\n"
            "| 2 | SCADA / supervisión de área |\n"
            "| 3 | PI System historiador, MES |\n"
            "| 4 | Supabase, data lake, Python ETL |\n"
            "| 5 | Power BI, ERP mantenimiento |\n\n"
            "### Flujo de datos (línea molienda)\n"
            "```\n"
            "Sensor → PLC → PI Historian → Python (ETL) → Supabase → Power BI → Alerta mantenimiento\n"
            "```"
        ),
        md("## 3. Tipos de dato en planta"),
        code(SETUP),
        code(
            """# Tabla comparativa de tipos de dato
tipos_dato = pd.DataFrame({
    "Tipo": ["Tiempo real", "Eventos", "Maestros", "Calculados"],
    "Ejemplo": [
        "PUMP101.VIBRATION_RMS cada 1s",
        "Falla rodamiento 2025-03-01 14:00",
        "Lista equipos, BOM, rutas AF",
        "MTBF, disponibilidad, eficiencia",
    ],
    "Herramienta típica": ["PI System", "CMMS / SQL", "Excel / AF", "Python / Power BI"],
})
tipos_dato
"""
        ),
        md(
            "## 4. Herramientas en la cadena de valor\n\n"
            "| Herramienta | Fortaleza | Limitación |\n"
            "|-------------|-----------|------------|\n"
            "| **Excel** | Modelos locales, KPIs rápidos | Escala, automatización, versionado |\n"
            "| **SQL/Supabase** | Consultas, historial centralizado | Requiere modelado de datos |\n"
            "| **Python** | ETL, ML, integración | Curva de aprendizaje |\n"
            "| **Power BI** | Dashboards ejecutivos | Dependiente de calidad de datos |"
        ),
        md(
            "## 5. Ejercicio práctico\n\n"
            "Dibuja en papel el flujo de un tag de vibración desde el sensor hasta un dashboard Power BI. "
            "Identifica en qué paso interviene cada herramienta."
        ),
        md(
            "## 6. Resumen y siguiente paso\n\n"
            "- Minería 5.0 integra OT e IT en un ecosistema de datos.\n"
            "- Python conecta sistemas; no reemplaza Excel ni Power BI.\n"
            "- El historiador PI es el punto de partida del análisis.\n\n"
            "**Siguiente:** `IV_02_excel_y_powerbi.ipynb`"
        ),
    ]


def nb02() -> list[dict]:
    return [
        md("# IV_02 — Excel y Power BI en la cadena de valor"),
        md(
            "## 1. Objetivo\n\n"
            "Diferenciar el rol de Excel y Power BI, y generar un dataset listo para importar en Power BI."
        ),
        md(
            "## 2. Concepto\n\n"
            "**Excel** es ideal para modelos de ingeniería puntuales (curvas de bomba, balances). "
            "**Power BI** consolida datos de múltiples fuentes para dashboards de jefatura.\n\n"
            "### Si vienes de Excel...\n"
            "Una hoja con columnas Fecha | Tag | Valor es equivalente al CSV que importarás en Power BI."
        ),
        code(SETUP),
        md("## 3. Generar dataset para Power BI"),
        code(
            """# Cargar export PI simulado
df_pi = pd.read_csv(DATA_DIR / "lecturas_pi_historiador.csv", parse_dates=["Timestamp"])
print(f"Registros PI: {len(df_pi)}")

# Agregar diario para dashboard (menos filas, más legible)
df_daily = (
    df_pi[df_pi["Quality"] == "GOOD"]
    .pivot_table(index="Timestamp", columns="Tag", values="Value", aggfunc="mean")
    .resample("1D")
    .mean()
    .reset_index()
)
df_daily["Timestamp"] = df_daily["Timestamp"].dt.strftime("%Y-%m-%d")

# Formato largo para Power BI
dashboard = df_daily.melt(id_vars=["Timestamp"], var_name="Tag", value_name="Valor")
dashboard["Equipo"] = dashboard["Tag"].str.split(".").str[0]

pbi_path = DATA_DIR / "powerbi" / "dashboard_fuente.csv"
pbi_path.parent.mkdir(exist_ok=True)
dashboard.to_csv(pbi_path, index=False)
print(f"Dataset Power BI: {pbi_path}")
dashboard.head()
"""
        ),
        md(
            "## 4. KPIs que podrías calcular en Excel o Power BI\n\n"
            "| KPI | Fórmula conceptual |\n"
            "|-----|-------------------|\n"
            "| Disponibilidad | MTBF / (MTBF + MTTR) |\n"
            "| Eficiencia bomba | Caudal medido / Caudal diseño |\n"
            "| Vibración promedio | PROMEDIO(lecturas 24h) |"
        ),
        code(
            """# KPI ejemplo: vibración promedio PUMP101
vib = df_pi[(df_pi["Tag"] == "PUMP101.VIBRATION_RMS") & (df_pi["Quality"] == "GOOD")]
kpi_vib = vib["Value"].mean()
print(f"KPI Vibración PUMP101: {kpi_vib:.2f} mm/s")
"""
        ),
        md(
            "## 5. Práctica Power BI (manual, 10 min)\n\n"
            "Sigue las instrucciones en `powerbi/instrucciones_dashboard.md`:\n"
            "1. Importar `data/powerbi/dashboard_fuente.csv`\n"
            "2. Crear gráfico de tendencia\n"
            "3. Crear tarjeta KPI de vibración"
        ),
        md(
            "## 6. Resumen y siguiente paso\n\n"
            "- Excel: modelado local; Power BI: visualización corporativa.\n"
            "- Python prepara y exporta datos limpios para ambos.\n"
            "- El CSV generado es la interfaz entre Python y Power BI.\n\n"
            "**Siguiente:** `IV_03_sql_supabase.ipynb`"
        ),
    ]


def nb03() -> list[dict]:
    return [
        md("# IV_03 — SQL y Supabase"),
        md(
            "## 1. Objetivo\n\n"
            "Consultar datos de planta con SQL usando Supabase (PostgreSQL en la nube) "
            "o SQLite local como fallback."
        ),
        md(
            "## 2. Concepto — SQL esencial\n\n"
            "| Comando | Uso en planta |\n"
            "|---------|---------------|\n"
            "| `SELECT` | Leer columnas |\n"
            "| `WHERE` | Filtrar por equipo, fecha, calidad |\n"
            "| `GROUP BY` | Agregar por turno, equipo |\n"
            "| `JOIN` | Unir equipos con eventos o lecturas |"
        ),
        code(SETUP + DB_HELPER),
        md("## 3. Consultas SQL locales (SQLite)"),
        code(
            """# Equipos de la planta
query_sql("SELECT * FROM equipos")
"""
        ),
        code(
            """# Lecturas GOOD de vibración
query_sql(\"\"\"
    SELECT timestamp, tag, valor, unidad
    FROM lecturas_pi
    WHERE quality = 'GOOD' AND tag LIKE '%VIBRATION%'
    ORDER BY timestamp
    LIMIT 10
\"\"\")
"""
        ),
        code(
            """# Equipos con más eventos de mantenimiento (JOIN)
query_sql(\"\"\"
    SELECT e.codigo, e.area, COUNT(ev.equipo_id) AS num_eventos, AVG(ev.mttr_horas) AS mttr_prom
    FROM equipos e
    LEFT JOIN eventos_mantenimiento ev ON e.id = ev.equipo_id
    GROUP BY e.codigo, e.area
    ORDER BY num_eventos DESC
\"\"\")
"""
        ),
        md("## 4. Consultas con Supabase (si .env configurado)"),
        code(
            """client = get_supabase_client()
if client:
    res = client.table("equipos").select("codigo, area, tipo").execute()
    df_supa = pd.DataFrame(res.data)
    print("Datos desde Supabase:")
    display(df_supa)
else:
    print("Sin .env — usando SQLite local. Configura Supabase para producción.")
"""
        ),
        md(
            "## 5. Ejercicio práctico\n\n"
            "Escribe una consulta SQL que devuelva el promedio de `valor` por `tag` "
            "solo para registros con `quality = 'GOOD'`."
        ),
        code(
            """# Solución
query_sql(\"\"\"
    SELECT tag, AVG(valor) AS promedio, COUNT(*) AS n
    FROM lecturas_pi
    WHERE quality = 'GOOD'
    GROUP BY tag
    ORDER BY promedio DESC
\"\"\")
"""
        ),
        md(
            "## 6. Resumen y siguiente paso\n\n"
            "- SQL es el lenguaje universal de bases de datos.\n"
            "- Supabase ofrece PostgreSQL gestionado con API REST.\n"
            "- SQLite local permite practicar sin conexión.\n\n"
            "**Siguiente:** `IV_04_pipeline_python_datos.ipynb`"
        ),
    ]


def nb04() -> list[dict]:
    return [
        md("# IV_04 — Pipeline Python: el pegamento del ecosistema"),
        md(
            "## 1. Objetivo\n\n"
            "Ejecutar un pipeline completo: leer export PI → limpiar → almacenar → "
            "consultar → exportar para Power BI."
        ),
        md(
            "## 2. Concepto\n\n"
            "Python no reemplaza Excel ni Power BI. **Los conecta:**\n"
            "1. Extrae datos del historiador (CSV/API)\n"
            "2. Valida calidad y transforma\n"
            "3. Carga en Supabase\n"
            "4. Genera agregados para dashboards"
        ),
        code(SETUP + DB_HELPER + "\nfrom datetime import datetime\n"),
        md("## 3. Paso 1 — Leer y limpiar export PI"),
        code(
            """raw = pd.read_csv(DATA_DIR / "lecturas_pi_historiador.csv", parse_dates=["Timestamp"])
print(f"Registros brutos: {len(raw)}")

df_clean = raw[raw["Quality"] == "GOOD"].copy()
df_clean = df_clean.dropna(subset=["Value"])
print(f"Registros GOOD: {len(df_clean)}")
df_clean.head()
"""
        ),
        md("## 4. Paso 2 — Transformar para almacenamiento"),
        code(
            """staging = df_clean.rename(columns={
    "Timestamp": "timestamp", "Tag": "tag", "Value": "valor",
    "Unit": "unidad", "Quality": "quality",
})
staging["timestamp"] = staging["timestamp"].astype(str)
staging = staging[["timestamp", "tag", "valor", "unidad", "quality"]]
staging.head()
"""
        ),
        md("## 5. Paso 3 — Consultar datos almacenados"),
        code(
            """resumen = query_sql(\"\"\"
    SELECT tag,
           AVG(valor) AS promedio,
           MAX(valor) AS maximo,
           COUNT(*) AS n
    FROM lecturas_pi
    WHERE quality = 'GOOD'
    GROUP BY tag
\"\"\")
resumen
"""
        ),
        md("## 6. Paso 4 — Exportar para Power BI"),
        code(
            """# Agregado diario para dashboard
agg = (
    df_clean.set_index("Timestamp")
    .groupby("Tag")["Value"]
    .resample("1D")
    .mean()
    .reset_index()
)
agg_pbi = agg.rename(columns={"Timestamp": "Fecha", "Tag": "Tag", "Value": "Valor"})
agg_pbi["Fecha"] = agg_pbi["Fecha"].dt.strftime("%Y-%m-%d")

out_pbi = OUTPUT_DIR / "pipeline_dashboard.csv"
agg_pbi.to_csv(out_pbi, index=False)

out_resumen = OUTPUT_DIR / "pipeline_resumen_tags.csv"
resumen.to_csv(out_resumen, index=False)

print(f"Exportado Power BI: {out_pbi}")
print(f"Exportado resumen: {out_resumen}")
"""
        ),
        md(
            "## 7. Interpretación para mantenimiento\n\n"
            "Un pipeline automatizado reduce errores de copiar/pegar entre Excel y reportes. "
            "La capa SQL (Supabase) permite que operaciones, mantenimiento y gerencia "
            "consulten los mismos datos con una sola fuente de verdad."
        ),
        md(
            "## 8. Resumen y siguiente paso\n\n"
            "- Pipeline: extraer → transformar → cargar → visualizar.\n"
            "- Python es el pegamento entre PI, SQL y Power BI.\n"
            "- Módulo B completo: ecosistema de datos Minería 5.0.\n\n"
            "**Siguiente módulo:** `05_ia_predictiva/IV_05_mantenimiento_predictivo.ipynb`"
        ),
    ]


BUILDERS = {
    "IV_01_flujo_datos_mineria50.ipynb": nb01,
    "IV_02_excel_y_powerbi.ipynb": nb02,
    "IV_03_sql_supabase.ipynb": nb03,
    "IV_04_pipeline_python_datos.ipynb": nb04,
}


def main() -> None:
    for name, builder in BUILDERS.items():
        path = MOD_DIR / name
        save_nb(path, builder())
        print(f"Creado: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
