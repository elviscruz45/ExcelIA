"""Genera datos simulados PI para Lab 01 — Historiador."""

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
TAGS = ["PUMP101.BEARING_TEMP", "PUMP101.VIBRATION_RMS", "PUMP101.DISCHARGE_PRESS"]


def main() -> None:
    (LAB_DIR / "outputs").mkdir(exist_ok=True)
    start = datetime(2025, 1, 1)
    end = datetime(2025, 3, 31)

    df = generate_pi_export(TAGS, start, end, freq="1h")
    df = inject_degradation(df, "PUMP101.BEARING_TEMP", slope_per_day=0.08)

    save_pi_csv(df, LAB_DIR / "data" / "datos_exportados_PI.csv")
    save_excel_template(
        LAB_DIR / "excel" / "modelo_ingenieria.xlsx",
        tags_df=default_tags_table(TAGS),
        umbrales_df=default_umbrales_table(TAGS),
    )
    print("Lab 01: datos generados correctamente.")


if __name__ == "__main__":
    main()
