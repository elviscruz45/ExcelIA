"""Genera datos simulados PI para Lab 05 — Weibull."""

import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pi_simulator import (  # noqa: E402
    default_tags_table,
    default_umbrales_table,
    generate_pi_export,
    generate_weibull_lifetimes,
    save_excel_template,
    save_pi_csv,
)

LAB_DIR = Path(__file__).resolve().parent
TAGS = ["PUMP101.BEARING_TEMP", "PUMP101.VIBRATION_RMS"]


def main() -> None:
    (LAB_DIR / "outputs").mkdir(exist_ok=True)
    df = generate_pi_export(TAGS, datetime(2024, 6, 1), datetime(2025, 1, 31), freq="12h")
    vidas = generate_weibull_lifetimes(n=50, shape=2.2, scale=5000)

    save_pi_csv(df, LAB_DIR / "data" / "datos_exportados_PI.csv")
    save_excel_template(
        LAB_DIR / "excel" / "modelo_ingenieria.xlsx",
        tags_df=default_tags_table(TAGS),
        umbrales_df=default_umbrales_table(TAGS),
        extra_sheets={"Vidas_Weibull": vidas},
    )
    print("Lab 05: datos generados correctamente.")


if __name__ == "__main__":
    main()
