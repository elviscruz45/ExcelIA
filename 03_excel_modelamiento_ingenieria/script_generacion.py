"""Genera datos simulados PI para Lab 03 — Excel modelamiento."""

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

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
TAGS = ["PUMP101.FLOW_RATE", "PUMP101.DISCHARGE_PRESS", "PUMP101.MOTOR_CURRENT"]


def main() -> None:
    (LAB_DIR / "outputs").mkdir(exist_ok=True)
    df = generate_pi_export(TAGS, datetime(2025, 1, 1), datetime(2025, 2, 15), freq="1h")
    modelo = pd.DataFrame(
        {
            "Parametro": ["Caudal_Diseno", "Presion_Diseno", "Potencia_Nominal"],
            "Valor": [130.0, 12.5, 55.0],
            "Unidad": ["m3/h", "bar", "kW"],
        }
    )

    save_pi_csv(df, LAB_DIR / "data" / "datos_exportados_PI.csv")
    save_excel_template(
        LAB_DIR / "excel" / "modelo_ingenieria.xlsx",
        tags_df=default_tags_table(TAGS),
        umbrales_df=default_umbrales_table(TAGS),
        extra_sheets={"Modelo": modelo},
    )
    print("Lab 03: datos generados correctamente.")


if __name__ == "__main__":
    main()
