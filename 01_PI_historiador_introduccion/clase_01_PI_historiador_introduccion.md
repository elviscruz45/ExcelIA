# Clase 01 — PI Historiador: Introducción

## Contexto industrial

El historiador AVEVA PI Data Archive almacena millones de registros de proceso en plantas mineras y de procesos. Los ingenieros de mantenimiento exportan series temporales para análisis de condición.

## Conceptos PI System

- **Tag:** Identificador único del punto de medición (ej. `PUMP101.BEARING_TEMP`).
- **Timestamp:** Marca de tiempo del valor registrado.
- **Quality:** Estado de validez (`GOOD`, `BAD`, `QUESTIONABLE`).

## Objetivos de aprendizaje

1. Leer un export CSV del historiador PI.
2. Filtrar por calidad de dato.
3. Resamplear series temporales.
4. Interpretar tendencias para mantenimiento.

## Pasos del laboratorio

1. Ejecutar `script_generacion.py` para crear datos simulados.
2. Abrir `01_PI_historiador_introduccion.ipynb`.
3. Ejecutar todas las celdas en orden.
4. Revisar outputs en `outputs/`.

## Preguntas de reflexión

- ¿Qué impacto tiene excluir registros con `Quality=BAD`?
- ¿Cómo definirías una alerta automática en PI para temperatura de rodamiento?
