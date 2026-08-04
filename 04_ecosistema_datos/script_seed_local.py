"""Genera CSV locales para Módulo B (sin Supabase)."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pi_simulator import generate_ecosystem_seed  # noqa: E402

LAB_DIR = Path(__file__).resolve().parent


def main() -> None:
    data = generate_ecosystem_seed()
    (LAB_DIR / "data").mkdir(exist_ok=True)
    (LAB_DIR / "data" / "powerbi").mkdir(exist_ok=True)
    (LAB_DIR / "outputs").mkdir(exist_ok=True)

    data["equipos"].to_csv(LAB_DIR / "data" / "equipos.csv", index=False)
    data["lecturas_pi"].to_csv(LAB_DIR / "data" / "lecturas_pi_export.csv", index=False)
    data["eventos_mantenimiento"].to_csv(LAB_DIR / "data" / "eventos_mantenimiento.csv", index=False)
    data["dashboard_fuente"].to_csv(LAB_DIR / "data" / "powerbi" / "dashboard_fuente.csv", index=False)
    data["lecturas_pi_export"].to_csv(LAB_DIR / "data" / "lecturas_pi_historiador.csv", index=False)

    print("CSV generados en 04_ecosistema_datos/data/")


if __name__ == "__main__":
    main()
