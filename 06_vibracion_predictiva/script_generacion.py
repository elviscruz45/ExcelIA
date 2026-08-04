"""Genera datos simulados PI para Lab 06 — Vibración predictiva."""

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
    save_excel_template,
    save_pi_csv,
)

LAB_DIR = Path(__file__).resolve().parent
TAGS = ["PUMP101.VIBRATION_RMS", "PUMP101.BEARING_TEMP"]


def main() -> None:
    (LAB_DIR / "outputs").mkdir(exist_ok=True)
    df = generate_pi_export(TAGS, datetime(2025, 1, 1), datetime(2025, 4, 30), freq="1h", noise_std=0.15)
    df = inject_degradation(df, "PUMP101.VIBRATION_RMS", slope_per_day=0.12, start_fraction=0.25)

    save_pi_csv(df, LAB_DIR / "data" / "datos_exportados_PI.csv")
    save_excel_template(
        LAB_DIR / "excel" / "modelo_ingenieria.xlsx",
        tags_df=default_tags_table(TAGS),
        umbrales_df=default_umbrales_table(TAGS),
    )
    print("Lab 06: datos generados correctamente.")


if __name__ == "__main__":
    main()
