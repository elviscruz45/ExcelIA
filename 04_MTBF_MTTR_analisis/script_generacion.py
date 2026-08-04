"""Genera datos simulados PI para Lab 04 — MTBF/MTTR."""

import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pi_simulator import (  # noqa: E402
    default_tags_table,
    default_umbrales_table,
    generate_failure_log,
    generate_pi_export,
    save_excel_template,
    save_pi_csv,
)

LAB_DIR = Path(__file__).resolve().parent
TAGS = ["PUMP101.VIBRATION_RMS", "PUMP102.VIBRATION_RMS"]
EQUIPOS = ["PUMP101", "PUMP102"]


def main() -> None:
    (LAB_DIR / "outputs").mkdir(exist_ok=True)
    df = generate_pi_export(TAGS, datetime(2024, 1, 1), datetime(2025, 3, 31), freq="6h")
    eventos = generate_failure_log(EQUIPOS, n_failures=10)

    save_pi_csv(df, LAB_DIR / "data" / "datos_exportados_PI.csv")
    save_excel_template(
        LAB_DIR / "excel" / "modelo_ingenieria.xlsx",
        tags_df=default_tags_table(TAGS, asset_path="Planta/Molienda"),
        umbrales_df=default_umbrales_table(TAGS),
        eventos_df=eventos,
    )
    print("Lab 04: datos generados correctamente.")


if __name__ == "__main__":
    main()
