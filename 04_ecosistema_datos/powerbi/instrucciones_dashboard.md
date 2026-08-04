# Power BI — Dashboard de línea de molienda

## Datos fuente

Importar el archivo generado por el notebook IV_02 o por:

```bash
uv run python 04_ecosistema_datos/script_seed_local.py
```

Archivo: `04_ecosistema_datos/data/powerbi/dashboard_fuente.csv`

Columnas: `Timestamp`, `Tag`, `Valor`, `Equipo`

## Pasos en Power BI Desktop (10 min)

1. **Obtener datos** → Texto/CSV → seleccionar `dashboard_fuente.csv`
2. **Transformar datos** (opcional): asegurar que `Timestamp` sea tipo Fecha
3. **Cerrar y aplicar**

### Visual 1 — Tendencia temporal

- Tipo: **Gráfico de líneas**
- Eje X: `Timestamp`
- Eje Y: `Valor`
- Leyenda: `Tag` o `Equipo`
- Título: "Tendencia sensores línea molienda"

### Visual 2 — KPI card

- Tipo: **Tarjeta**
- Campo: `Valor` (promedio o último valor)
- Filtro: `Tag` = `PUMP101.VIBRATION_RMS`
- Título: "Vibración actual PUMP101 (mm/s)"

### Medida DAX opcional (concepto)

```dax
Disponibilidad = DIVIDE([MTBF], [MTBF] + [MTTR])
```

En este dataset de sensores, la medida ilustra el concepto; los valores MTBF/MTTR vienen del módulo A (Lab 04).

## Relación con el ecosistema

| Herramienta | Rol en este dashboard |
|-------------|----------------------|
| PI System | Origen de tags y timestamps |
| Python | Limpieza y exportación a CSV |
| Supabase | Almacenamiento centralizado (Módulo B, IV_03) |
| Power BI | Visualización para jefatura de mantenimiento |
