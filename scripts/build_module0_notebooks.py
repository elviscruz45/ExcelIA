"""Genera los 8 notebooks del Módulo 0 — Python desde cero para ingenieros."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOD_DIR = ROOT / "00_python_para_ingenieros"

# Compatible con Jupyter local (uv) y Google Colab
KERNEL = {"display_name": "Python 3", "language": "python", "name": "python3"}

COLAB_INTRO = (
    "> **Google Colab:** Ejecuta primero la celda **Configuración del entorno**. "
    "Detecta Colab automáticamente, instala dependencias si faltan y prepara carpetas `data/` y `outputs/`.\n"
    "> **Jupyter local:** La misma celda funciona con el entorno ExcelA (`uv sync`)."
)

SETUP = """import os
import sys
from pathlib import Path

def _in_colab():
    try:
        import google.colab  # noqa: F401
        return True
    except ImportError:
        return False

IN_COLAB = _in_colab()

if IN_COLAB:
    _candidatos = [
        Path("/content/ExcelA/00_python_para_ingenieros"),
        Path("/content/drive/MyDrive/ExcelA/00_python_para_ingenieros"),
        Path("/content/drive/MyDrive/Colab Notebooks/ExcelA/00_python_para_ingenieros"),
        Path("/content/00_python_para_ingenieros"),
        Path.cwd(),
    ]
    MOD_DIR = next(
        (p for p in _candidatos if (p / "README_modulo0.md").exists() or (p / "data").is_dir()),
        Path("/content/00_python_para_ingenieros"),
    )
    print("Entorno: Google Colab")
else:
    MOD_DIR = Path.cwd()
    print("Entorno: Jupyter local")

MOD_DIR.mkdir(parents=True, exist_ok=True)
os.chdir(MOD_DIR)
OUTPUT_DIR = MOD_DIR / "outputs"
DATA_DIR = MOD_DIR / "data"
OUTPUT_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)
print(f"Directorio del módulo: {MOD_DIR}")
"""

SETUP_PANDAS = """import os
import sys
import subprocess
from pathlib import Path

def _in_colab():
    try:
        import google.colab  # noqa: F401
        return True
    except ImportError:
        return False

IN_COLAB = _in_colab()

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "pandas", "matplotlib"])
    import pandas as pd
    import matplotlib.pyplot as plt

if IN_COLAB:
    try:
        get_ipython().run_line_magic("matplotlib", "inline")
    except NameError:
        pass

if IN_COLAB:
    _candidatos = [
        Path("/content/ExcelA/00_python_para_ingenieros"),
        Path("/content/drive/MyDrive/ExcelA/00_python_para_ingenieros"),
        Path("/content/drive/MyDrive/Colab Notebooks/ExcelA/00_python_para_ingenieros"),
        Path("/content/00_python_para_ingenieros"),
        Path.cwd(),
    ]
    MOD_DIR = next(
        (p for p in _candidatos if (p / "README_modulo0.md").exists() or (p / "data").is_dir()),
        Path("/content/00_python_para_ingenieros"),
    )
    print("Entorno: Google Colab")
else:
    MOD_DIR = Path.cwd()
    print("Entorno: Jupyter local")

MOD_DIR.mkdir(parents=True, exist_ok=True)
os.chdir(MOD_DIR)
OUTPUT_DIR = MOD_DIR / "outputs"
DATA_DIR = MOD_DIR / "data"
OUTPUT_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

DATA_PATH = DATA_DIR / "lecturas_turno.csv"
if not DATA_PATH.exists():
    import numpy as np
    from datetime import datetime, timedelta
    rng = np.random.default_rng(42)
    start = datetime(2025, 3, 1, 8, 0)
    rows = []
    for h in range(24):
        ts = start + timedelta(hours=h)
        for var, unidad, base, noise in [("TEMP_RODAMIENTO", "°C", 70.0, 3.0), ("VIBRACION_RMS", "mm/s", 2.5, 0.3)]:
            rows.append({
                "Timestamp": ts, "Equipo": "PUMP101", "Variable": var,
                "Valor": round(base + rng.normal(0, noise), 2), "Unidad": unidad,
                "Quality": "BAD" if rng.random() < 0.03 else "GOOD",
            })
    pd.DataFrame(rows).to_csv(DATA_PATH, index=False)
    print(f"Datos generados en Colab: {DATA_PATH}")

print(f"Directorio del módulo: {MOD_DIR}")
"""


def colab_config_cell() -> list[dict]:
    return [
        md("## Configuración del entorno\n\n" + COLAB_INTRO),
        code(SETUP),
    ]


def colab_config_pandas() -> list[dict]:
    return [
        md("## Configuración del entorno\n\n" + COLAB_INTRO),
        code(SETUP_PANDAS),
    ]


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
            "colab": {"provenance": []},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def save_nb(path: Path, cells: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notebook(cells), indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def objetivo(texto: str) -> dict:
    return md(f"## 1. Objetivo\n\n{texto}")


def concepto(texto: str) -> dict:
    return md(f"## 2. Concepto\n\n{texto}")


def puente_excel(texto: str) -> dict:
    return md(f"### Si vienes de Excel...\n\n{texto}")


def desde_cero(texto: str) -> dict:
    return md(f"### Desde cero\n\n{texto}")


def ejercicio(titulo: str, enunciado: str, solucion: str) -> list[dict]:
    return [
        md(f"## 5. Ejercicio práctico — {titulo}\n\n{enunciado}"),
        code(solucion),
    ]


def resumen(texto: str, siguiente: str) -> dict:
    return md(f"## 6. Resumen y siguiente paso\n\n{texto}\n\n**Siguiente lección:** {siguiente}")


def nb01() -> list[dict]:
    return [
        md("# Lección 00_01 — Bienvenida y entorno Python"),
        objetivo(
            "Entender qué es Python, cómo se usa en mantenimiento predictivo de plantas concentradoras "
            "y ejecutar tu primera línea de código en Jupyter."
        ),
        concepto(
            "**Python** es un lenguaje de programación legible que usan ingenieros para analizar datos de sensores, "
            "calcular indicadores (MTBF, disponibilidad) y automatizar reportes.\n\n"
            "En una planta concentradora, Python puede procesar miles de lecturas de bombas, molinos y celdas de flotación "
            "más rápido que hacerlo manualmente en Excel."
        ),
        desde_cero(
            "Un **programa** es una lista de instrucciones. En Jupyter o Google Colab, cada **celda de código** "
            "es una instrucción que ejecutas con **Shift + Enter** (Colab) o el botón ▶."
        ),
        *colab_config_cell(),
        md("## 3. Ejemplos guiados"),
        code('print("Monitoreo PUMP101 activo — turno día iniciado")'),
        code(
            """# Mostrar información del entorno de trabajo
print("Directorio de trabajo:", MOD_DIR)
print("Carpeta de datos:", DATA_DIR)
print("Carpeta de salidas:", OUTPUT_DIR)
"""
        ),
        md(
            "## 4. Errores comunes\n\n"
            "- **Olvidar ejecutar la celda:** El código no corre solo; presiona Shift + Enter.\n"
            "- **SyntaxError:** Revisa comillas, paréntesis y dos puntos (`:`).\n"
            "- **NameError:** Ejecutaste celdas fuera de orden; vuelve arriba y ejecuta desde el inicio.\n"
            "- **En Colab:** Si cambias de notebook, vuelve a ejecutar la celda de configuración."
        ),
        *ejercicio(
            "Tu primer reporte de turno",
            "Imprime un mensaje que indique el equipo, el turno y el estado operativo. "
            "Ejemplo: `PUMP101 | Turno Día | Estado: En servicio`",
            'equipo = "PUMP101"\nturno = "Día"\nestado = "En servicio"\nprint(f"{equipo} | Turno {turno} | Estado: {estado}")',
        ),
        resumen(
            "- Python se ejecuta celda a celda en Jupyter o Colab.\n"
            "- `print()` muestra texto en pantalla.\n"
            "- La celda de configuración prepara carpetas `data/` y `outputs/`.",
            "`00_02_variables_y_unidades.ipynb`",
        ),
    ]


def nb02() -> list[dict]:
    return [
        md("# Lección 00_02 — Variables y tipos de datos"),
        objetivo(
            "Crear variables para almacenar mediciones de planta (temperatura, horas de operación, tags) "
            "y distinguir los tipos básicos: entero, decimal, texto y booleano."
        ),
        concepto(
            "Una **variable** es un nombre que guarda un valor. En ingeniería usamos nombres descriptivos "
            "con unidades implícitas: `temp_rodamiento_c`, `caudal_m3h`."
        ),
        puente_excel(
            "En Excel, una celda con valor `75.4` es como una variable. "
            "En Python escribes: `temp_rodamiento = 75.4`"
        ),
        *colab_config_cell(),
        md("## 3. Ejemplos guiados"),
        code(
            """# Entero: horas de operación acumuladas
horas_operacion = 7200
print(type(horas_operacion), "→", horas_operacion)
"""
        ),
        code(
            """# Decimal (float): temperatura de rodamiento en °C
temp_rodamiento_c = 75.4
print(type(temp_rodamiento_c), "→", temp_rodamiento_c)
"""
        ),
        code(
            """# Texto (str): tag del sensor en PI System
tag_bomba = "PUMP101.BEARING_TEMP"
print(type(tag_bomba), "→", tag_bomba)
"""
        ),
        code(
            """# Booleano (bool): ¿la bomba está en servicio?
bomba_en_servicio = True
print(type(bomba_en_servicio), "→", bomba_en_servicio)
"""
        ),
        code(
            """# Convención ingenieril: incluir unidad en el nombre
presion_descarga_bar = 12.3
vibracion_rms_mms = 2.8
print(f"Presión: {presion_descarga_bar} bar | Vibración: {vibracion_rms_mms} mm/s")
"""
        ),
        *ejercicio(
            "Ficha técnica de equipo",
            "Crea variables para el molino MILL201: potencia nominal (float, kW), nombre del equipo (str) "
            "y si está operativo (bool). Imprime una línea de resumen.",
            'potencia_kw = 4500.0\nequipo = "MILL201"\noperativo = True\nprint(f"{equipo}: {potencia_kw} kW | Operativo: {operativo}")',
        ),
        resumen(
            "- `int`, `float`, `str` y `bool` son los tipos básicos.\n"
            "- Usa nombres claros con unidad: `temp_c`, `caudal_m3h`.\n"
            "- `type()` muestra el tipo de una variable.",
            "`00_03_operadores_y_strings.ipynb`",
        ),
    ]


def nb03() -> list[dict]:
    return [
        md("# Lección 00_03 — Operadores y cadenas de texto"),
        objetivo(
            "Realizar cálculos de ingeniería (potencia, caudal), comparar valores con umbrales "
            "y formatear mensajes de alerta para reportes de turno."
        ),
        concepto(
            "Los **operadores** permiten calcular y comparar. Las **f-strings** (`f\"...\"`) insertan variables "
            "en texto para generar alertas legibles."
        ),
        puente_excel(
            "`=A1*B1` en Excel equivale a `corriente_a * tension_v` en Python. "
            "`=A1>70` devuelve VERDADERO/FALSO; en Python es `temp > 70`."
        ),
        *colab_config_cell(),
        md("## 3. Ejemplos guiados"),
        code(
            """# Potencia del motor del molino: P = I × V
corriente_a = 320
tension_v = 6600
potencia_kw = (corriente_a * tension_v) / 1000
print(f"Potencia estimada: {potencia_kw:,.0f} kW")
"""
        ),
        code(
            """# Comparaciones con umbrales de vibración
vibracion_rms = 5.2
umbral_alerta = 4.5
print("¿Supera alerta?", vibracion_rms > umbral_alerta)
print("¿Dentro de rango normal?", vibracion_rms <= umbral_alerta)
"""
        ),
        code(
            """# f-string para alerta de mantenimiento
equipo = "PUMP101"
temp_rodamiento_c = 78.5
umbral_critico_c = 80

mensaje = f"ALERTA {equipo}: temperatura rodamiento {temp_rodamiento_c} °C (umbral {umbral_critico_c} °C)"
print(mensaje)
"""
        ),
        code(
            """# Reporte de turno con múltiples variables
turno = "Noche"
operador = "J. Pérez"
paradas_h = 1.5

reporte = (
    f"Reporte turno {turno} | Operador: {operador} | "
    f"Paradas no programadas: {paradas_h} h"
)
print(reporte)
"""
        ),
        *ejercicio(
            "Alerta de presión de descarga",
            "La bomba PUMP102 tiene presión de descarga 9.8 bar y umbral mínimo 10 bar. "
            "Crea variables y un f-string que indique si hay riesgo de cavitación.",
            'equipo = "PUMP102"\npresion_bar = 9.8\numbral_min_bar = 10.0\nriesgo = presion_bar < umbral_min_bar\nprint(f"{equipo}: presión {presion_bar} bar | Riesgo cavitación: {riesgo}")',
        ),
        resumen(
            "- Operadores `+ - * /` para cálculos; `> < >= <=` para comparar.\n"
            "- f-strings formatean alertas: `f\"Temp {t} °C\"`.\n"
            "- Las comparaciones devuelven `True` o `False`.",
            "`00_04_listas_y_diccionarios.ipynb`",
        ),
    ]


def nb04() -> list[dict]:
    return [
        md("# Lección 00_04 — Listas y diccionarios"),
        objetivo(
            "Almacenar múltiples lecturas de sensores (lista) y representar un tag PI como diccionario "
            "con tag, valor y unidad."
        ),
        concepto(
            "Una **lista** guarda varios valores en orden (ej. 24 lecturas horarias de vibración). "
            "Un **diccionario** guarda pares clave-valor (como un tag PI con sus atributos)."
        ),
        puente_excel(
            "Un rango `A1:A24` en Excel es similar a una lista en Python. "
            "Una fila con columnas Tag | Valor | Unidad es similar a un diccionario."
        ),
        *colab_config_cell(),
        md("## 3. Ejemplos guiados"),
        code(
            """# 24 lecturas horarias de vibración (mm/s) — turno de un día
lecturas_vibracion = [
    2.1, 2.3, 2.0, 2.4, 2.2, 2.5, 2.8, 3.1,
    2.9, 2.7, 2.6, 2.4, 2.3, 2.5, 2.8, 3.0,
    3.2, 3.5, 3.8, 4.1, 4.0, 3.9, 3.7, 3.5,
]
print("Lecturas:", len(lecturas_vibracion))
print("Mínimo:", min(lecturas_vibracion), "| Máximo:", max(lecturas_vibracion))
print("Promedio:", round(sum(lecturas_vibracion) / len(lecturas_vibracion), 2))
"""
        ),
        code(
            """# Lista de bombas en la línea de molienda
bombas_linea = ["PUMP101", "PUMP102", "PUMP103", "PUMP104"]
print("Equipos en línea:", bombas_linea)
print("Primera bomba:", bombas_linea[0])
print("Última bomba:", bombas_linea[-1])
"""
        ),
        code(
            """# Diccionario: mini-registro estilo PI System
tag_pi = {
    "tag": "PUMP101.VIBRATION_RMS",
    "valor": 3.2,
    "unidad": "mm/s",
    "quality": "GOOD",
}
print(tag_pi["tag"], "=", tag_pi["valor"], tag_pi["unidad"])
"""
        ),
        code(
            """# Lista de diccionarios: varios sensores de una bomba
sensores_pump101 = [
    {"variable": "TEMP_RODAMIENTO", "valor": 72.1, "unidad": "°C"},
    {"variable": "VIBRACION_RMS", "valor": 2.8, "unidad": "mm/s"},
    {"variable": "CAUDAL", "valor": 118.5, "unidad": "m3/h"},
]
for sensor in sensores_pump101:
    print(f"  {sensor['variable']}: {sensor['valor']} {sensor['unidad']}")
"""
        ),
        *ejercicio(
            "Estadísticas de turno",
            "Dada la lista `lecturas_temp = [71.2, 72.0, 73.5, 74.1, 75.0]`, calcula el promedio "
            "y determina si alguna lectura supera 74 °C.",
            "lecturas_temp = [71.2, 72.0, 73.5, 74.1, 75.0]\npromedio = sum(lecturas_temp) / len(lecturas_temp)\nsupera_umbral = max(lecturas_temp) > 74\nprint(f\"Promedio: {promedio:.1f} °C | Supera 74 °C: {supera_umbral}\")",
        ),
        resumen(
            "- Listas: `[]`, acceso por índice `[0]`, funciones `min`, `max`, `sum`, `len`.\n"
            "- Diccionarios: `{}`, acceso por clave `['tag']`.\n"
            "- Combinar ambos modela sensores y equipos de planta.",
            "`00_05_condicionales.ipynb`",
        ),
    ]


def nb05() -> list[dict]:
    return [
        md("# Lección 00_05 — Condicionales (if / elif / else)"),
        objetivo(
            "Clasificar el estado operativo de un equipo (Normal / Alerta / Crítico) según umbrales "
            "de vibración y temperatura, como haría un sistema de monitoreo."
        ),
        concepto(
            "Las **condicionales** ejecutan código solo si se cumple una condición. "
            "En planta: si vibración > umbral → generar alerta."
        ),
        puente_excel(
            "`=SI(A1>4,5;\"Alerta\";\"Normal\")` en Excel equivale a:\n"
            "```python\nif vibracion > 4.5:\n    estado = \"Alerta\"\nelse:\n    estado = \"Normal\"\n```"
        ),
        *colab_config_cell(),
        md("## 3. Ejemplos guiados"),
        code(
            """def clasificar_vibracion(rms, umbral_alerta=4.5, umbral_critico=7.1):
    if rms >= umbral_critico:
        return "Critico"
    elif rms >= umbral_alerta:
        return "Alerta"
    else:
        return "Normal"

# Probar con distintos valores
for valor in [2.5, 5.0, 8.0]:
    print(f"Vibración {valor} mm/s → {clasificar_vibracion(valor)}")
"""
        ),
        code(
            """# Condición compuesta: alerta si temperatura Y vibración altas
temp_c = 76.0
vib_mms = 5.2

if temp_c > 75 and vib_mms > 4.5:
    print("ALERTA COMBINADA: revisar rodamiento y lubricación")
elif temp_c > 75 or vib_mms > 4.5:
    print("Alerta simple: monitorear tendencia")
else:
    print("Operación normal")
"""
        ),
        code(
            """# Clasificar varios equipos con if/elif/else
equipos_estado = [
    ("PUMP101", 2.8, 68.0),
    ("PUMP102", 5.5, 72.0),
    ("PUMP103", 8.2, 78.0),
]

for nombre, vib, temp in equipos_estado:
    estado = clasificar_vibracion(vib)
    print(f"{nombre}: vib={vib} mm/s, temp={temp} °C → {estado}")
"""
        ),
        *ejercicio(
            "Estado del molino",
            "Si la potencia del molino supera 4800 kW, imprime 'Sobrecarga'. "
            "Si está entre 4000 y 4800, imprime 'Operación nominal'. Si no, 'Baja carga'.",
            "potencia_kw = 4650\nif potencia_kw > 4800:\n    print('Sobrecarga')\nelif potencia_kw >= 4000:\n    print('Operación nominal')\nelse:\n    print('Baja carga')",
        ),
        resumen(
            "- `if / elif / else` controlan el flujo según condiciones.\n"
            "- `and` y `or` combinan múltiples umbrales.\n"
            "- Base de cualquier sistema de alertas en planta.",
            "`00_06_bucles.ipynb`",
        ),
    ]


def nb06() -> list[dict]:
    return [
        md("# Lección 00_06 — Bucles (for y while)"),
        objetivo(
            "Recorrer listas de equipos y lecturas de sensores con `for`, "
            "y usar `while` para acumular horas hasta una inspección programada."
        ),
        concepto(
            "Un **bucle** repite instrucciones. `for` recorre una lista; `while` repite mientras se cumpla una condición."
        ),
        puente_excel(
            "`=PROMEDIO(A1:A24)` procesa 24 celdas. En Python, un `for` recorre la lista y tú decides qué calcular."
        ),
        *colab_config_cell(),
        md("## 3. Ejemplos guiados"),
        code(
            """# for: imprimir estado de cada bomba en servicio
bombas = ["PUMP101", "PUMP102", "PUMP103"]
estados = ["En servicio", "En servicio", "Parada programada"]

for i in range(len(bombas)):
    print(f"{bombas[i]}: {estados[i]}")
"""
        ),
        code(
            """# for: detectar picos de vibración en lecturas horarias
lecturas = [2.1, 2.5, 3.0, 5.8, 2.3, 2.1, 6.2, 2.0]
umbral_pico = 5.0
picos = []

for i, valor in enumerate(lecturas):
    if valor > umbral_pico:
        picos.append((i, valor))
        print(f"  Hora {i}: PICO detectado — {valor} mm/s")

print(f"Total picos: {len(picos)}")
"""
        ),
        code(
            """# Acumulador: sumar horas de parada no programada
paradas_horas = [0.5, 1.2, 0.0, 2.3, 0.8]
total_paradas = 0

for horas in paradas_horas:
    total_paradas += horas

print(f"Horas totales de parada en la semana: {total_paradas} h")
"""
        ),
        code(
            """# while: simular horas hasta próxima inspección
horas_restantes = 72
horas_transcurridas = 0

while horas_transcurridas < horas_restantes:
    horas_transcurridas += 8  # cada iteración = un turno de 8 h
    print(f"  Turno completado. Faltan {horas_restantes - horas_transcurridas} h para inspección")

print("Inspección programada alcanzada.")
"""
        ),
        *ejercicio(
            "Conteo de alertas",
            "Recorre `temperaturas = [68, 72, 76, 81, 74]` y cuenta cuántas superan 75 °C.",
            "temperaturas = [68, 72, 76, 81, 74]\ncontador = 0\nfor t in temperaturas:\n    if t > 75:\n        contador += 1\nprint(f'Lecturas en alerta: {contador}')",
        ),
        resumen(
            "- `for elemento in lista:` recorre colecciones.\n"
            "- `while condicion:` repite hasta que la condición sea falsa.\n"
            "- Los acumuladores (`total += valor`) son clave en reportes.",
            "`00_07_funciones.ipynb`",
        ),
    ]


def nb07() -> list[dict]:
    return [
        md("# Lección 00_07 — Funciones"),
        objetivo(
            "Crear funciones reutilizables para cálculos de mantenimiento: disponibilidad, "
            "clasificación de vibración y conversión de unidades."
        ),
        concepto(
            "Una **función** encapsula lógica con nombre, parámetros y valor de retorno. "
            "Evita repetir el mismo código en cada análisis de turno."
        ),
        puente_excel(
            "Una **función personalizada** o **macro** en Excel es similar a `def mi_funcion():` en Python. "
            "La ventaja: puedes combinarlas en pipelines de análisis."
        ),
        *colab_config_cell(),
        md("## 3. Ejemplos guiados"),
        code(
            """def calcular_disponibilidad(mtbf_horas, mttr_horas):
    \"\"\"Disponibilidad = MTBF / (MTBF + MTTR)\"\"\"
    return mtbf_horas / (mtbf_horas + mttr_horas)

disp_pump101 = calcular_disponibilidad(mtbf_horas=500, mttr_horas=12)
print(f"Disponibilidad PUMP101: {disp_pump101:.1%}")
"""
        ),
        code(
            """def clasificar_vibracion(rms, umbral_alerta=4.5, umbral_critico=7.1):
    if rms >= umbral_critico:
        return "Critico"
    elif rms >= umbral_alerta:
        return "Alerta"
    return "Normal"

# Reutilizar la función para varios equipos
equipos_vib = {"PUMP101": 3.2, "PUMP102": 5.8, "PUMP103": 7.5}
for equipo, rms in equipos_vib.items():
    print(f"{equipo}: {clasificar_vibracion(rms)}")
"""
        ),
        code(
            """def bar_a_psi(presion_bar):
    \"\"\"Convierte presión de bar a psi.\"\"\"
    return presion_bar * 14.5038

presion_succion = 2.5  # bar
print(f"Presión succión: {presion_succion} bar = {bar_a_psi(presion_succion):.1f} psi")
"""
        ),
        *ejercicio(
            "Función de eficiencia de bomba",
            "Crea `calcular_eficiencia(caudal_medido, caudal_diseno)` que devuelva el porcentaje. "
            "Pruébala con caudal medido 115 y diseño 130 m3/h.",
            "def calcular_eficiencia(caudal_medido, caudal_diseno):\n    return (caudal_medido / caudal_diseno) * 100\n\neficiencia = calcular_eficiencia(115, 130)\nprint(f'Eficiencia: {eficiencia:.1f}%')",
        ),
        resumen(
            "- `def nombre(parametros):` define una función.\n"
            "- `return` devuelve el resultado.\n"
            "- Las funciones evitan duplicar lógica en análisis repetitivos.",
            "`00_08_intro_pandas_planta.ipynb`",
        ),
    ]


def nb08() -> list[dict]:
    return [
        md("# Lección 00_08 — Archivos e introducción a pandas"),
        objetivo(
            "Leer un archivo CSV de lecturas de turno, explorar datos con pandas, filtrar por calidad "
            "y crear un gráfico de tendencia — preparación directa para el Lab 01 de PI System."
        ),
        concepto(
            "**pandas** es la librería estándar para tablas de datos en Python. "
            "Un `DataFrame` es como una hoja de Excel en memoria: filas, columnas y operaciones vectorizadas."
        ),
        puente_excel(
            "`pd.read_csv('archivo.csv')` carga un CSV como DataFrame. "
            "`.head()` es como ver las primeras filas; `.describe()` como estadísticas descriptivas."
        ),
        *colab_config_pandas(),
        md("## 3. Ejemplos guiados"),
        code(
            """# Leer CSV de lecturas de turno
df = pd.read_csv(DATA_PATH, parse_dates=["Timestamp"])
print(f"Registros cargados: {len(df)}")
df.head()
"""
        ),
        code(
            """# Exploración básica
print("Columnas:", df.columns.tolist())
print("\\nEstadísticas:")
df["Valor"].describe()
"""
        ),
        code(
            """# Filtrar solo datos con calidad GOOD (como en PI System)
df_good = df[df["Quality"] == "GOOD"]
print(f"Registros GOOD: {len(df_good)} de {len(df)}")

# Filtrar temperatura de rodamiento de PUMP101
df_temp = df_good[
    (df_good["Equipo"] == "PUMP101") & (df_good["Variable"] == "TEMP_RODAMIENTO")
]
df_temp.head()
"""
        ),
        code(
            """# Gráfico de tendencia de temperatura
serie = df_temp.set_index("Timestamp")["Valor"]

plt.figure(figsize=(10, 4))
plt.plot(serie.index, serie.values, marker="o", markersize=3, color="steelblue")
plt.axhline(75, color="orange", linestyle="--", label="Umbral alerta 75 °C")
plt.title("PUMP101 — Temperatura de rodamiento (turno)")
plt.xlabel("Hora")
plt.ylabel("°C")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

grafico_path = OUTPUT_DIR / "tendencia_temp_pump101.png"
plt.savefig(grafico_path, dpi=150)
print(f"Gráfico guardado: {grafico_path}")
"""
        ),
        code(
            """# Exportar resumen a CSV
resumen = df_good.groupby(["Equipo", "Variable"])["Valor"].agg(["mean", "max", "min"]).reset_index()
resumen_path = OUTPUT_DIR / "resumen_turno.csv"
resumen.to_csv(resumen_path, index=False)
print(f"Resumen exportado: {resumen_path}")
resumen
"""
        ),
        *ejercicio(
            "Filtrar vibración crítica",
            "Filtra registros GOOD de PUMP101 con variable VIBRACION_RMS y calcula el máximo. "
            "Si supera 4.5 mm/s, imprime una alerta.",
            'df_vib = df_good[(df_good["Equipo"]=="PUMP101") & (df_good["Variable"]=="VIBRACION_RMS")]\nmax_vib = df_vib["Valor"].max()\nprint(f"Vibración máxima: {max_vib} mm/s")\nif max_vib > 4.5:\n    print("ALERTA: vibración supera umbral de alerta")',
        ),
        resumen(
            "- `pd.read_csv()` carga datos tabulares.\n"
            "- Filtrar con `df[condicion]` es equivalente a filtros en Excel.\n"
            "- Ya puedes leer exports PI y graficar tendencias.",
            "**Lab 01 — `01_PI_historiador_introduccion.ipynb`** (siguiente módulo del curso)",
        ),
    ]


BUILDERS = {
    "00_01_bienvenida_y_entorno.ipynb": nb01,
    "00_02_variables_y_unidades.ipynb": nb02,
    "00_03_operadores_y_strings.ipynb": nb03,
    "00_04_listas_y_diccionarios.ipynb": nb04,
    "00_05_condicionales.ipynb": nb05,
    "00_06_bucles.ipynb": nb06,
    "00_07_funciones.ipynb": nb07,
    "00_08_intro_pandas_planta.ipynb": nb08,
}


def main() -> None:
    (MOD_DIR / "outputs").mkdir(exist_ok=True)
    for filename, builder in BUILDERS.items():
        path = MOD_DIR / filename
        save_nb(path, builder())
        print(f"Notebook creado: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
