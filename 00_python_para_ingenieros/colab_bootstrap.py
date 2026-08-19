"""Bootstrap del Módulo 0 para Jupyter local y Google Colab."""

from __future__ import annotations

import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path


def in_colab() -> bool:
    try:
        import google.colab  # noqa: F401

        return True
    except ImportError:
        return False


def _instalar_dependencias(*paquetes: str) -> None:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-q", *paquetes],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def ensure_datos_turno(data_dir: Path) -> Path:
    """Crea lecturas_turno.csv si no existe (útil en Colab sin subir data/)."""
    path = data_dir / "lecturas_turno.csv"
    if path.exists():
        return path

    import numpy as np
    import pandas as pd

    rng = np.random.default_rng(42)
    start = datetime(2025, 3, 1, 8, 0)
    rows: list[dict] = []
    for h in range(24):
        ts = start + timedelta(hours=h)
        for var, unidad, base, noise in [
            ("TEMP_RODAMIENTO", "°C", 70.0, 3.0),
            ("VIBRACION_RMS", "mm/s", 2.5, 0.3),
        ]:
            valor = round(base + rng.normal(0, noise), 2)
            quality = "BAD" if rng.random() < 0.03 else "GOOD"
            rows.append(
                {
                    "Timestamp": ts,
                    "Equipo": "PUMP101",
                    "Variable": var,
                    "Valor": valor,
                    "Unidad": unidad,
                    "Quality": quality,
                }
            )
    pd.DataFrame(rows).to_csv(path, index=False)
    print(f"Datos de práctica generados: {path}")
    return path


def setup_modulo0(*, instalar_pandas: bool = False) -> tuple[Path, Path, Path]:
    """Configura rutas del módulo. Devuelve (MOD_DIR, DATA_DIR, OUTPUT_DIR)."""
    if instalar_pandas:
        try:
            import pandas  # noqa: F401
            import matplotlib  # noqa: F401
        except ImportError:
            _instalar_dependencias("pandas", "matplotlib")

    if in_colab():
        candidatos = [
            Path("/content/ExcelA/00_python_para_ingenieros"),
            Path("/content/drive/MyDrive/ExcelA/00_python_para_ingenieros"),
            Path("/content/drive/MyDrive/Colab Notebooks/ExcelA/00_python_para_ingenieros"),
            Path("/content/00_python_para_ingenieros"),
            Path.cwd(),
        ]
        mod_dir = next(
            (p for p in candidatos if (p / "README_modulo0.md").exists() or (p / "data").is_dir()),
            Path("/content/00_python_para_ingenieros"),
        )
        print("Entorno detectado: Google Colab")
    else:
        mod_dir = Path.cwd()
        print("Entorno detectado: Jupyter local")

    mod_dir.mkdir(parents=True, exist_ok=True)
    data_dir = mod_dir / "data"
    output_dir = mod_dir / "outputs"
    data_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    os.chdir(mod_dir)
    print(f"Directorio del módulo: {mod_dir}")
    return mod_dir, data_dir, output_dir


if __name__ == "__main__":
    mod, data, out = setup_modulo0()
    ensure_datos_turno(data)
    print(f"DATA_DIR={data}")
    print(f"OUTPUT_DIR={out}")
