"""Ejecuta las celdas del notebook en orden, sin interacción."""
import json
import os
from pathlib import Path
os.environ.setdefault("MPLBACKEND", "Agg")
ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
notebook = json.loads((ROOT / "Modelo_Tesis_APC.ipynb").read_text(encoding="utf-8"))
namespace = {"__name__": "__main__"}
for index, cell in enumerate(notebook["cells"], 1):
    if cell["cell_type"] == "code":
        print(f"Ejecutando celda {index}", flush=True)
        exec(compile("".join(cell["source"]), f"celda_{index}", "exec"), namespace)
if not namespace["df_check"]["Estado"].eq("OK").all():
    raise RuntimeError("Los indicadores difieren de la referencia: revisar Reproducibilidad en el Excel.")
print("Ejecución y verificaciones completadas.")
