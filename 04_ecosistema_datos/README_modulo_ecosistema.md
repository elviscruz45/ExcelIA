# Módulo IV-B — Minería 5.0: Transformación Digital y Ecosistema de Datos

**Duración:** 2 horas (4 notebooks × 30 min)

## Objetivo

Entender el flujo de datos desde el sensor hasta la decisión de mantenimiento y el rol de **Excel, Power BI, SQL (Supabase) y Python** en la cadena de valor.

## Ruta de estudio

| # | Notebook | Tema |
|---|----------|------|
| IV_01 | `IV_01_flujo_datos_mineria50.ipynb` | OT/IT, Purdue, flujo de datos |
| IV_02 | `IV_02_excel_y_powerbi.ipynb` | Excel vs Power BI, dataset para dashboard |
| IV_03 | `IV_03_sql_supabase.ipynb` | SQL esencial, consultas Supabase |
| IV_04 | `IV_04_pipeline_python_datos.ipynb` | Pipeline PI → Python → Supabase → Power BI |

## Preparación

```bash
# 1. Datos locales (siempre)
uv run python 04_ecosistema_datos/script_seed_local.py

# 2. Supabase (opcional en aula, requerido para IV_03-04 completos)
cp 04_ecosistema_datos/.env.example 04_ecosistema_datos/.env
# Ejecutar sql/schema_supabase.sql en Supabase SQL Editor
uv run python 04_ecosistema_datos/script_seed_supabase.py
```

## Power BI

Ver [`powerbi/instrucciones_dashboard.md`](powerbi/instrucciones_dashboard.md) para importar `data/powerbi/dashboard_fuente.csv`.

## Fallback sin Supabase

Los notebooks IV_03 e IV_04 usan SQLite local (`data/ecosistema_local.db`) si no hay `.env` configurado.

## Siguiente módulo

**Módulo IV-C:** `05_ia_predictiva/` — IA y Python para Análisis Predictivo de Fallas (2 h).
