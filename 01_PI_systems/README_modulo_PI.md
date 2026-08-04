# Módulo IV-A — Integración de Sistemas PY (PI Systems)

**Duración en aula:** 2 horas (4 bloques × 30 min)

Guía docente para la ruta condensada del curso. Los laboratorios completos están en las carpetas `01_` a `08_` en la raíz del proyecto.

## Ruta de 2 horas

| Bloque | Tiempo | Notebook | Secciones prioritarias |
|--------|--------|----------|------------------------|
| A1 | 30 min | `01_PI_historiador_introduccion/01_PI_historiador_introduccion.ipynb` | §1-4, §6 tendencia, §7 exportación |
| A2 | 30 min | `02_PI_asset_framework/02_PI_asset_framework.ipynb` | §3-5 agrupación por componente, §6 dashboard |
| A3 | 30 min | `03_excel_modelamiento_ingenieria/03_excel_modelamiento_ingenieria.ipynb` | §5 KPIs eficiencia, §6 comparación diseño vs medido |
| A4 | 30 min | `04_MTBF_MTTR_analisis/04_MTBF_MTTR_analisis.ipynb` | §5 MTBF/MTTR/disponibilidad, §6 timeline |

## Si el tiempo apremia — omitir

| Lab | Celdas opcionales |
|-----|-------------------|
| 01 | Estadísticas detalladas por tag; segunda visualización de calidad |
| 02 | Exploración extendida; hoja Tags en Excel de salida |
| 03 | Exploración completa; hojas Umbrales/Modelo en export |
| 04 | Timeline detallado; exploración PI de vibración |

## Antes de empezar

1. Completar **Módulo 0** (`00_python_para_ingenieros/`) o equivalente en Python/pandas.
2. Ejecutar `script_generacion.py` de cada lab antes de abrir el notebook.
3. Kernel Jupyter: **ExcelA (uv)**.

```bash
uv run python 01_PI_historiador_introduccion/script_generacion.py
uv run python 02_PI_asset_framework/script_generacion.py
uv run python 03_excel_modelamiento_ingenieria/script_generacion.py
uv run python 04_MTBF_MTTR_analisis/script_generacion.py
```

## Material de extensión (post-curso)

| Lab | Tema | Cuándo asignar |
|-----|------|----------------|
| 05 | Weibull y confiabilidad | Curso de confiabilidad |
| 06 | Vibración predictiva | Monitoreo de condición |
| 07 | Machine Learning fallas | Previo a Módulo C IA |
| 08 | IA en mantenimiento | Integración predictiva avanzada |

## Siguiente módulo

**Módulo IV-B:** `04_ecosistema_datos/` — Transformación Digital y Ecosistema de Datos (2 h).
