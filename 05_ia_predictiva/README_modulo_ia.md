# Módulo IV-C — Minería 5.0: IA y Python para Análisis Predictivo de Fallas

**Duración:** 2 horas (4 notebooks × 30 min)

## Objetivo

Aplicar machine learning e IA al monitoreo de condición en plantas concentradoras: clasificar fallas, detectar anomalías, estimar RUL y priorizar alertas.

## Ruta de estudio

| # | Notebook | Tema |
|---|----------|------|
| IV_05 | `IV_05_mantenimiento_predictivo.ipynb` | Escalera predictivo, features |
| IV_06 | `IV_06_ml_clasificacion_fallas.ipynb` | Random Forest, matriz confusión, ROC |
| IV_07 | `IV_07_anomalias_y_rul.ipynb` | Z-score, Isolation Forest, RUL |
| IV_08 | `IV_08_caso_integrado_alertas.ipynb` | Pipeline completo, Pareto |

## Preparación

```bash
uv run python 05_ia_predictiva/script_generacion.py
```

## Relación con Labs existentes

| Lab | Contenido relacionado |
|-----|----------------------|
| 06 Vibración predictiva | Umbrales ISO, tendencias |
| 07 ML fallas | Clasificación binaria (profundización) |
| 08 IA mantenimiento | RUL y scoring (profundización) |

Este módulo **consolida** el caso PUMP101 en un hilo narrativo único.

## Entregables

- `outputs/ml_clasificacion.png`
- `outputs/anomalias_rul.png`
- `outputs/dashboard_riesgo.png`
- `outputs/alertas_priorizadas.csv`

## Prerequisitos

- Módulo 0 (Python básico)
- Módulo A (PI Systems) recomendado
- Módulo B (Ecosistema de Datos) recomendado
