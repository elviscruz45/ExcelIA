# Módulo 0 — Python desde cero para ingenieros de planta

Curso introductorio en **8 notebooks Jupyter** para ingenieros de mantenimiento y operaciones de plantas concentradoras. Funciona en **Google Colab** (recomendado para principiantes) y en **Jupyter local** con el entorno ExcelA.

## Antes del Módulo 0

Si **nunca has usado Colab** o tienes poca experiencia con internet y archivos digitales, completa primero estas guías con tu instructor (~45 min):

1. [`GUIA_00_antes_de_empezar.md`](GUIA_00_antes_de_empezar.md) — Colab, navegador, cuentas Google, checklist
2. [`GUIA_MAPA_CURSO_MINERIA50.md`](../GUIA_MAPA_CURSO_MINERIA50.md) — Por qué existe el curso y las 4 etapas
3. [`GLOSARIO_PLANTA_TECNOLOGIA.md`](../GLOSARIO_PLANTA_TECNOLOGIA.md) — Consulta cuando aparezca un término nuevo

## Opción A — Google Colab (recomendado)

No necesitas instalar Python en tu computadora.

### Forma rápida (un solo notebook)

1. Ve a [Google Colab](https://colab.research.google.com/)
2. **Archivo → Subir notebook** y elige por ejemplo `00_01_bienvenida_y_entorno.ipynb`
3. Ejecuta la celda **Configuración del entorno** (primera celda de código)
4. Colab detecta el entorno, crea carpetas y — en la lección 08 — genera los datos si no existen

### Forma completa (toda la carpeta del módulo)

**Opción 1 — Google Drive**

1. Copia la carpeta `00_python_para_ingenieros` a `Mi unidad/ExcelA/` en Google Drive
2. En Colab, abre un notebook desde Drive
3. La celda de configuración detecta la ruta automáticamente

**Opción 2 — Clonar repositorio**

Si el proyecto está en GitHub, ejecuta al inicio del notebook 00_01:

```python
!git clone https://github.com/TU_USUARIO/ExcelA.git /content/ExcelA
%cd /content/ExcelA/00_python_para_ingenieros
```

**Opción 3 — Montar Drive (opcional)**

```python
from google.colab import drive
drive.mount("/content/drive")
# Luego abre notebooks desde /content/drive/MyDrive/ExcelA/00_python_para_ingenieros/
```

### Atajos en Colab

| Acción | Atajo |
|--------|-------|
| Ejecutar celda | `Shift + Enter` |
| Ejecutar y avanzar | `Shift + Enter` |
| Ver gráficos | Automático con `%matplotlib inline` (lección 08) |

## Opción B — Jupyter local (ExcelA + uv)

```bash
cd ExcelA
uv sync
uv run python -m ipykernel install --user --name excela --display-name "ExcelA (uv)"
uv run jupyter notebook
# Navega a 00_python_para_ingenieros/
```

## Cómo estudiar

1. Abre los notebooks **en orden** (00_01 → 00_08)
2. En cada notebook, ejecuta primero **Configuración del entorno**
3. Lee cada sección Markdown antes de ejecutar el código
4. Completa el ejercicio práctico al final

## Ruta de estudio

| # | Notebook | Tema | Tiempo est. |
|---|----------|------|-------------|
| 00_01 | `00_01_bienvenida_y_entorno.ipynb` | Qué es Python, entorno, primer `print` | 25 min |
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

## Archivos de apoyo

| Archivo | Uso |
|---------|-----|
| `GUIA_00_antes_de_empezar.md` | Guía previa: Colab, internet, archivos (leer antes de 00_01) |
| `colab_bootstrap.py` | Script auxiliar de configuración (opcional en Colab) |
| `data/lecturas_turno.csv` | Datos para lección 08 (se auto-genera en Colab si falta) |
| `outputs/` | Gráficos y CSV generados por los notebooks |

## Después del Módulo 0

Al completar la lección 00_08 estarás listo para el **Lab 01 — PI Historiador Introducción**.

## Solución de problemas (Colab)

| Problema | Solución |
|----------|----------|
| `NameError: MOD_DIR` | Ejecuta la celda de configuración primero |
| No encuentra `lecturas_turno.csv` | Re-ejecuta configuración en 00_08; genera datos automáticamente |
| Gráfico no se ve | Re-ejecuta celda de configuración en 00_08 (activa `%matplotlib inline`) |
| Quiero guardar outputs | Descarga desde panel de archivos de Colab o usa Google Drive |

## Estructura de carpetas

```
00_python_para_ingenieros/
├── README_modulo0.md
├── GUIA_00_antes_de_empezar.md
├── colab_bootstrap.py
├── 00_01_...ipynb             # 8 notebooks (compatibles Colab)
├── data/
│   └── lecturas_turno.csv
└── outputs/
```
