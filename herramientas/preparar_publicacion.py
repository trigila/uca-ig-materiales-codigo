from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from comun import load_json


def main() -> int:
    parser = argparse.ArgumentParser(description="Informa cambios Git locales sin crear commits ni publicar.")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--strict", action="store_true", help="Falla ante eliminaciones o renombres que requieren revisión.")
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    known = {entry["relative_path"].replace("/", "\\") for entry in manifest.get("entries", [])}
    result = subprocess.run(
        ["git", "status", "--porcelain=v1"], cwd=args.root, check=True, text=True, capture_output=True
    )
    requires_review = False
    for line in result.stdout.splitlines():
        status, path = line[:2], line[3:]
        print(f"CAMBIO {status} {path}")
        if ("D" in status or "R" in status) and path.replace("/", "\\") in known:
            print(f"REVISION_REQUERIDA archivo_referenciado={path}")
            requires_review = True
    if not result.stdout:
        print("SIN_CAMBIOS_GIT")
    print("No se creó ningún commit ni se publicó contenido.")
    return 1 if args.strict and requires_review else 0


if __name__ == "__main__":
    raise SystemExit(main())
