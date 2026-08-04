# Módulo 0 — Python desde cero para ingenieros de planta

Curso introductorio en **8 notebooks Jupyter** para ingenieros de mantenimiento y operaciones de plantas concentradoras. No se requiere experiencia previa en programación.

## Prerequisitos

- Entorno ExcelA configurado (`uv sync` en la raíz del proyecto)
- Jupyter con kernel **ExcelA (uv)**

## Cómo estudiar

1. Abre los notebooks **en orden** (00_01 → 00_08).
2. Lee cada sección Markdown antes de ejecutar el código.
3. Ejecuta las celdas con **Shift + Enter**.
4. Completa el ejercicio práctico al final de cada lección.

```bash
cd ExcelA
uv run jupyter notebook
# Navega a 00_python_para_ingenieros/
```

## Ruta de estudio

| # | Notebook | Tema | Tiempo est. |
|---|----------|------|-------------|
| 00_01 | `00_01_bienvenida_y_entorno.ipynb` | Qué es Python, Jupyter, primer `print` | 25 min |
| 00_02 | `00_02_variables_y_unidades.ipynb` | Variables, tipos, unidades ingenieriles | 30 min |
| 00_03 | `00_03_operadores_y_strings.ipynb` | Operadores, comparaciones, f-strings | 30 min |
| 00_04 | `00_04_listas_y_diccionarios.ipynb` | Listas, dicts, lecturas de sensores | 35 min |
| 00_05 | `00_05_condicionales.ipynb` | if/elif/else, umbrales de alerta | 30 min |
| 00_06 | `00_06_bucles.ipynb` | for, while, acumuladores | 35 min |
| 00_07 | `00_07_funciones.ipynb` | def, return, reutilización | 35 min |
| 00_08 | `00_08_intro_pandas_planta.ipynb` | CSV, pandas, gráfico básico | 40 min |

**Tiempo total estimado:** 4–5 horas

## Audiencia mixta

- **Desde cero:** Sigue las secciones "Desde cero" con analogías de planta (tag, sensor, umbral).
- **Si vienes de Excel:** Busca las cajas "Si vienes de Excel..." que mapean celdas, fórmulas y `SI()` a Python.

## Después del Módulo 0

Al completar la lección 00_08 estarás listo para el **Lab 01 — PI Historiador Introducción**, donde aplicarás pandas a exportaciones reales simuladas de AVEVA PI System.

## Estructura de carpetas

```
00_python_para_ingenieros/
├── README_modulo0.md          # Este archivo
├── 00_01_...ipynb             # 8 notebooks
├── data/
│   └── lecturas_turno.csv     # Datos de práctica (lección 08)
└── outputs/                   # Resultados generados por los notebooks
```
