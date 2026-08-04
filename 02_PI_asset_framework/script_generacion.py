"""Genera datos simulados PI para Lab 02 — Asset Framework."""

import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pi_simulator import (  # noqa: E402
    default_tags_table,
    default_umbrales_table,
    generate_pi_export,
    save_excel_template,
    save_pi_csv,
)

LAB_DIR = Path(__file__).resolve().parent
TAGS = [
    "PUMP101.BEARING_TEMP",
    "PUMP101.VIBRATION_RMS",
    "PUMP101.DISCHARGE_PRESS",
    "PUMP101.MOTOR_CURRENT",
]


def main() -> None:
    (LAB_DIR / "outputs").mkdir(exist_ok=True)
    df = generate_pi_export(TAGS, datetime(2025, 1, 1), datetime(2025, 2, 28), freq="1h")
    tags_meta = default_tags_table(TAGS, asset_path="Planta/Molienda/PUMP101")

    save_pi_csv(df, LAB_DIR / "data" / "datos_exportados_PI.csv")
    save_excel_template(
        LAB_DIR / "excel" / "modelo_ingenieria.xlsx",
        tags_df=tags_meta,
        umbrales_df=default_umbrales_table(TAGS),
    )
    print("Lab 02: datos generados correctamente.")


if __name__ == "__main__":
    main()
