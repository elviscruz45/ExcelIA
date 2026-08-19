# Glosario — Planta ↔ Tecnología

Consulta este archivo cuando aparezca un término nuevo. **No hace falta leerlo entero de una vez.**

---

## A

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Activo / Asset** | Equipo físico (bomba, molino, motor) | Registro en el modelo de datos con tags asociados |
| **Alerta** | Aviso de condición anormal (vibración alta, temperatura) | Regla o modelo que dispara notificación automática |
| **Anomalía** | Comportamiento fuera de lo normal en un sensor | Valor estadísticamente raro detectado por un algoritmo |
| **Asset Framework (AF)** | Jerarquía de equipos y componentes de la planta | Modelo de AVEVA PI que organiza tags por activo |

---

## B

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Big Data** | Miles de lecturas por segundo de cientos de sensores | Volúmenes de datos que superan lo manejable solo con Excel |
| **BOM** | Lista de materiales / repuestos de un equipo | Tabla maestra de componentes |
| **Browser / Navegador** | — | Programa para ver páginas web (Chrome, Edge) |

---

## C

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Celda (Jupyter)** | — | Bloque de código o texto en un notebook; se ejecuta con Shift+Enter |
| **CMMS** | Sistema de gestión de mantenimiento (órdenes de trabajo) | Software IT para planificar y registrar intervenciones |
| **Colab** | — | Google Colaboratory: Python en el navegador, sin instalar nada |
| **CSV** | Exportar lecturas a archivo de texto | Formato de archivo con columnas separadas por comas; lo lee pandas |
| **Cloud / Nube** | — | Servidores remotos (Google, Supabase) accesibles por internet |

---

## D

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Dashboard** | Tablero de indicadores del turno | Pantalla visual (Power BI) con gráficos y KPIs en tiempo casi real |
| **DCS** | Sistema de control distribuido del proceso | Plataforma OT de control y supervisión |
| **Disponibilidad** | % de tiempo que el equipo estuvo operativo | MTBF / (MTBF + MTTR) |

---

## E

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **ETL** | Preparar datos de sensores para análisis | Extract (extraer), Transform (limpiar), Load (cargar a base de datos) |
| **Evento** | Falla, parada, cambio de modo operativo | Registro puntual con fecha/hora (distinto de serie continua) |

---

## F

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Feature** | Variable de condición medible (vibración, temp.) | Columna de entrada para un modelo de ML |
| **Flotación / Molienda** | Áreas del proceso en concentradora | Contexto del caso de estudio PUMP101 |

---

## G

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **GOOD / BAD (Quality)** | Dato confiable vs dato inválido del sensor | Campo de calidad en export PI; filtrar BAD antes de analizar |

---

## H

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Historiador** | Archivo central de todas las lecturas de proceso | AVEVA PI Data Archive; millones de registros timestamp + valor |
| **HMI / SCADA** | Pantalla de supervisión en sala de control | Nivel 2 del modelo Purdue; visualización OT |

---

## I

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **IA (Inteligencia Artificial)** | Sistema que recomienda acciones de mantenimiento | Modelos que aprenden patrones de falla a partir de datos históricos |
| **IT** | — | Tecnología de información: bases de datos, reportes, dashboards |
| **Internet** | Red que conecta oficina con sistemas remotos | Infraestructura para acceder a Colab, Supabase, correo |

---

## J

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Jupyter / Notebook** | — | Documento interactivo con texto + código; extensión `.ipynb` |

---

## K

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **KPI** | Indicador clave (MTBF, OEE, vibración promedio) | Métrica calculada para seguimiento y decisiones |

---

## M

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Machine Learning (ML)** | Detectar patrones antes de la falla | Algoritmo que aprende de datos históricos (ej. Random Forest) |
| **Minería 5.0** | Planta conectada digitalmente | Integración OT + IT para mantenimiento predictivo |
| **MTBF** | Tiempo promedio entre fallas | Mean Time Between Failures |
| **MTTR** | Tiempo promedio de reparación | Mean Time To Repair |

---

## N

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Notebook** | — | Ver Jupyter / `.ipynb` |

---

## O

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **OT** | Tecnología de operaciones: PLC, sensores, control | Sistemas de tiempo real en planta (niveles 0–3 Purdue) |
| **OT/IT** | Unir datos de piso de planta con sistemas de oficina | Objetivo central de Minería 5.0 |

---

## P

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **pandas** | — | Librería Python para tablas de datos (como Excel programable) |
| **Pareto** | Priorizar los equipos que más impacto tienen | Ranking 80/20 de riesgos o fallas |
| **PI System** | Historiador de la planta (AVEVA) | Software que almacena tags, timestamps y calidad |
| **PLC** | Controlador lógico programable del equipo | Dispositivo OT que lee sensores y ejecuta lógica de control |
| **Predictivo** | Mantenimiento basado en condición real | Usar datos de vibración/temp. para intervenir antes de la falla |
| **Prescriptivo** | Mantenimiento con recomendación optimizada | IA sugiere cuándo y qué reparar según riesgo y costo |
| **print()** | Mostrar un valor en pantalla | Función Python equivalente a "ver resultado" en una celda |
| **Purdue (modelo)** | Capas de la planta: sensor → control → historiador → IT | Modelo de referencia OT/IT (niveles 0 a 5) |
| **Python** | — | Lenguaje de programación para análisis de datos industriales |

---

## Q

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Quality (calidad de dato)** | Señal buena vs señal con fallo de sensor | Campo `GOOD`, `BAD`, `QUESTIONABLE` en export PI |

---

## R

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Random Forest** | — | Algoritmo de ML usado en el curso para clasificar riesgo de falla |
| **Reactivo** | Reparar después de la falla | Nivel más bajo de madurez de mantenimiento |
| **Resampleo** | Promediar lecturas cada 5 min en lugar de cada 1 s | Agrupar series temporales por intervalo (pandas) |
| **ROC / Matriz de confusión** | — | Métricas para evaluar si un modelo detecta fallas correctamente |
| **RUL** | Horas restantes antes de falla estimada | Remaining Useful Life; salida de modelos predictivos |

---

## S

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Sensor** | Instrumento que mide temp., vibración, presión | Nivel 0 Purdue; origen del dato |
| **Serie temporal** | Historial de un tag a lo largo del tiempo | Columna Timestamp + Value en un DataFrame |
| **SQL** | Consultar historial de fallas o lecturas | Lenguaje para bases de datos (SELECT, WHERE, JOIN) |
| **Supabase** | — | Base de datos en la nube (PostgreSQL) usada en Módulo B |
| **Shift + Enter** | — | Atajo para ejecutar una celda en Jupyter/Colab |

---

## T

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Tag** | Punto de medición (ej. `PUMP101.BEARING_TEMP`) | Identificador único en PI System |
| **Timestamp** | Fecha y hora exacta de la lectura | Columna de tiempo en exports CSV/PI |
| **Turno** | Jornada de operación (día/noche) | Contexto para reportes y filtros de datos |

---

## U

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Umbral** | Límite de alerta (ej. vibración > 7 mm/s) | Valor de corte en condicionales `if` o reglas PI |

---

## V

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Variable** | Magnitud medida o calculada | Nombre en Python que guarda un valor (`temperatura = 72.5`) |
| **Vibración RMS** | Nivel de vibración del rodamiento | Tag típico de condición en PUMP101; mm/s |

---

## Z

| Término | En planta | En tecnología |
|---------|-----------|---------------|
| **Z-score** | Desviación respecto al comportamiento normal | Método estadístico para detectar anomalías |

---

## Siglas rápidas

| Sigla | Significado |
|-------|-------------|
| AF | Asset Framework |
| CSV | Comma-Separated Values |
| ETL | Extract, Transform, Load |
| IA | Inteligencia Artificial |
| IT | Information Technology |
| KPI | Key Performance Indicator |
| ML | Machine Learning |
| MTBF | Mean Time Between Failures |
| MTTR | Mean Time To Repair |
| OT | Operational Technology |
| PI | Plant Information (AVEVA PI System) |
| PLC | Programmable Logic Controller |
| RUL | Remaining Useful Life |
| SCADA | Supervisory Control and Data Acquisition |

---

**Ver también:** [`GUIA_MAPA_CURSO_MINERIA50.md`](GUIA_MAPA_CURSO_MINERIA50.md) · [`GUIA_00_antes_de_empezar.md`](00_python_para_ingenieros/GUIA_00_antes_de_empezar.md)
