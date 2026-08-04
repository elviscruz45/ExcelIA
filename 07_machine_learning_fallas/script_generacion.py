"""Genera datos simulados PI para Lab 07 — Machine Learning."""

import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pi_simulator import (  # noqa: E402
    default_tags_table,
    default_umbrales_table,
    generate_pi_export,
    inject_degradation,
    inject_failures,
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
    df = generate_pi_export(TAGS, datetime(2024, 9, 1), datetime(2025, 3, 31), freq="1h")
    df = inject_degradation(df, "PUMP101.VIBRATION_RMS", slope_per_day=0.06, start_fraction=0.4)
    df = inject_failures(
        df,
        [
            {"timestamp": datetime(2025, 2, 10, 14), "tag": "PUMP101.VIBRATION_RMS", "duration_hours": 6, "spike": 4.0},
            {"timestamp": datetime(2025, 3, 5, 8), "tag": "PUMP101.BEARING_TEMP", "duration_hours": 4, "spike": 8.0},
        ],
    )

    save_pi_csv(df, LAB_DIR / "data" / "datos_exportados_PI.csv")
    save_excel_template(
        LAB_DIR / "excel" / "modelo_ingenieria.xlsx",
        tags_df=default_tags_table(TAGS),
        umbrales_df=default_umbrales_table(TAGS),
    )
    print("Lab 07: datos generados correctamente.")


if __name__ == "__main__":
    main()
