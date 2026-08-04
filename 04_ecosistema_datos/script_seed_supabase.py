"""Pobla tablas Supabase desde datos simulados. Requiere .env configurado."""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pi_simulator import generate_ecosystem_seed  # noqa: E402

LAB_DIR = Path(__file__).resolve().parent
load_dotenv(LAB_DIR / ".env")

BATCH_SIZE = 100


def main() -> None:
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise SystemExit("Configura SUPABASE_URL y SUPABASE_KEY en 04_ecosistema_datos/.env")

    from supabase import create_client

    client = create_client(url, key)
    data = generate_ecosystem_seed()

    # Limpiar tablas (orden por FK)
    for table in ("eventos_mantenimiento", "lecturas_pi", "equipos"):
        client.table(table).delete().neq("id", 0).execute()

    equipos_rows = data["equipos"].to_dict(orient="records")
    client.table("equipos").insert(equipos_rows).execute()
    print(f"Insertados {len(equipos_rows)} equipos")

    lecturas = data["lecturas_pi"].copy()
    lecturas["timestamp"] = lecturas["timestamp"].astype(str)
    lecturas_rows = lecturas.drop(columns=["equipo_codigo"], errors="ignore").to_dict(orient="records")

    for i in range(0, len(lecturas_rows), BATCH_SIZE):
        batch = lecturas_rows[i : i + BATCH_SIZE]
        client.table("lecturas_pi").insert(batch).execute()
    print(f"Insertadas {len(lecturas_rows)} lecturas_pi")

    eventos = data["eventos_mantenimiento"].copy()
    eventos["inicio"] = eventos["inicio"].astype(str)
    eventos["fin"] = eventos["fin"].astype(str)
    eventos_rows = eventos.to_dict(orient="records")
    client.table("eventos_mantenimiento").insert(eventos_rows).execute()
    print(f"Insertados {len(eventos_rows)} eventos_mantenimiento")

    print("Supabase poblado correctamente.")


if __name__ == "__main__":
    main()
