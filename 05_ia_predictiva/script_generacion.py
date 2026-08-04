"""Genera dataset predictivo para Módulo C."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pi_simulator import generate_predictive_dataset  # noqa: E402

LAB_DIR = Path(__file__).resolve().parent


def main() -> None:
    (LAB_DIR / "data").mkdir(exist_ok=True)
    (LAB_DIR / "outputs").mkdir(exist_ok=True)
    df = generate_predictive_dataset(n_hours=500, failure_rate=0.08)
    path = LAB_DIR / "data" / "dataset_predictivo.csv"
    df.to_csv(path, index=False)
    print(f"Dataset generado: {path} ({len(df)} filas, {df['falla'].sum()} fallas)")


if __name__ == "__main__":
    main()
