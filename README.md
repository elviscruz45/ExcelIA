# ExcelA — Curso Minería 5.0 + PI System para Plantas Concentradoras

Programa de **6 horas** (3 módulos × 2h) más prerequisito de Python. Orientado a ingenieros de mantenimiento y operaciones.

## Mapa del programa (6 horas)

| Módulo | Horas | Carpeta | Contenido |
|--------|-------|---------|-----------|
| **IV-A: Integración PI Systems** | 2h | Labs `01_`–`04_` | AVEVA PI, Asset Framework, Excel, MTBF/MTTR |
| **IV-B: Ecosistema de Datos** | 2h | `04_ecosistema_datos/` | Flujo OT/IT, Excel, Power BI, SQL Supabase, Python |
| **IV-C: IA Predictiva de Fallas** | 2h | `05_ia_predictiva/` | ML, anomalías, RUL, pipeline de alertas |

**Prerequisito (fuera de las 6h):** [`00_python_para_ingenieros/`](00_python_para_ingenieros/) (~4–5h)

**Profundización opcional:** Labs `05_`–`08_` (Weibull, vibración, ML, IA)

## Requisitos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- Cuenta [Supabase](https://supabase.com) (Módulo B)
- Power BI Desktop opcional (Módulo B, práctica manual)

## Configuración

```bash
cd ExcelA
uv sync
uv run python -m ipykernel install --user --name excela --display-name "ExcelA (uv)"

# Supabase (Módulo B): copiar credenciales
cp 04_ecosistema_datos/.env.example 04_ecosistema_datos/.env
# Editar .env con SUPABASE_URL y SUPABASE_KEY
```

## Estructura del proyecto

```
ExcelA/
├── 00_python_para_ingenieros/     # Prerequisito Python
├── 01_PI_systems/                  # Guía docente Módulo A (2h)
├── 01_PI_historiador_introduccion/ # Labs PI 01-08
├── ...
├── 04_ecosistema_datos/            # Módulo B (2h)
├── 05_ia_predictiva/               # Módulo C (2h)
└── src/pi_simulator.py
```

## Uso rápido

```bash
uv run jupyter notebook

# Regenerar datos Módulo B
uv run python 04_ecosistema_datos/script_seed_local.py

# Poblar Supabase (requiere .env)
uv run python 04_ecosistema_datos/script_seed_supabase.py

# Regenerar datos Módulo C
uv run python 05_ia_predictiva/script_generacion.py
```

## Guías por módulo

- Prerequisito: [`00_python_para_ingenieros/README_modulo0.md`](00_python_para_ingenieros/README_modulo0.md)
- Módulo A: [`01_PI_systems/README_modulo_PI.md`](01_PI_systems/README_modulo_PI.md)
- Módulo B: [`04_ecosistema_datos/README_modulo_ecosistema.md`](04_ecosistema_datos/README_modulo_ecosistema.md)
- Módulo C: [`05_ia_predictiva/README_modulo_ia.md`](05_ia_predictiva/README_modulo_ia.md)
