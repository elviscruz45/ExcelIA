"""
Exporta datos desde Supabase hacia un CSV compatible con el dataset que espera Power BI.

Formato de salida (mismo estilo de `data/powerbi/dashboard_fuente.csv`):
Timestamp,Tag,Valor,Equipo

Supuestos (coherentes con el repo):
- La tabla `lecturas_pi` contiene: timestamp, tag, valor, quality.
- Los valores de calidad usan 'GOOD'/'BAD'.
- 'Equipo' se deriva del prefijo de 'tag' antes del primer punto (ej. PUMP101.*).
"""

from __future__ import annotations

import argparse
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv


LAB_DIR = Path(__file__).resolve().parent


def get_supabase_client():
    load_dotenv(LAB_DIR / ".env")
    url, key = os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise SystemExit(
            "Configura SUPABASE_URL y SUPABASE_KEY en 04_ecosistema_datos/.env (basado en .env.example)."
        )
    from supabase import create_client

    return create_client(url, key)


def fetch_lecturas_good(client, start_iso: str, end_iso: str, page_size: int) -> pd.DataFrame:
    """
    Descarga filas desde Supabase con paginacion.
    Nota: el volumen real depende del tamano de la demo; mantenlo acotado con --days.
    """

    rows: list[dict] = []
    offset = 0

    while True:
        res = (
            client.table("lecturas_pi")
            .select("timestamp,tag,valor,quality")
            .eq("quality", "GOOD")
            .gte("timestamp", start_iso)
            .lte("timestamp", end_iso)
            .order("timestamp", desc=False)
            .range(offset, offset + page_size - 1)
            .execute()
        )

        batch = res.data or []
        if not batch:
            break

        rows.extend(batch)

        if len(batch) < page_size:
            break

        offset += page_size

    if not rows:
        return pd.DataFrame(columns=["timestamp", "tag", "valor", "quality"])

    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Exportar lecturas GOOD desde Supabase para Power BI.")
    parser.add_argument("--days", type=int, default=30, help="Rango de dias a exportar (hacia atras desde ahora).")
    parser.add_argument(
        "--page-size",
        type=int,
        default=5000,
        help="Tamaño de pagina para descarga. Ajusta si hay problemas con volumen.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=str(LAB_DIR / "data" / "powerbi" / "dashboard_fuente_supabase.csv"),
        help="Ruta de salida CSV para Power BI.",
    )
    args = parser.parse_args()

    end = datetime.now(timezone.utc)
    start = end - timedelta(days=args.days)

    start_iso = start.isoformat()
    end_iso = end.isoformat()

    client = get_supabase_client()

    df = fetch_lecturas_good(client, start_iso=start_iso, end_iso=end_iso, page_size=args.page_size)
    if df.empty:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(out_path, index=False)
        print(f"No hubo datos. CSV vacio exportado: {out_path}")
        return

    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
    df = df.dropna(subset=["timestamp"])

    # Derivar equipo desde el tag (prefijo antes del primer punto)
    df["Equipo"] = df["tag"].astype(str).str.split(".").str[0]
    df["Timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%d")

    # Agregar diario para que coincida con el dataset consumido por Power BI
    agg = (
        df.groupby(["Timestamp", "tag", "Equipo"], as_index=False)["valor"]
        .mean()
        .rename(columns={"tag": "Tag", "valor": "Valor"})
    )

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    agg = agg[["Timestamp", "Tag", "Valor", "Equipo"]]
    agg.to_csv(out_path, index=False)

    print(f"Exportado {len(agg)} filas para Power BI: {out_path}")


if __name__ == "__main__":
    main()

