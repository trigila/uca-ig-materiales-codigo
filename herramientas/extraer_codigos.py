from __future__ import annotations

import argparse
from pathlib import Path

from comun import code_blocks, document_entries, load_json, safe_target


def main() -> int:
    parser = argparse.ArgumentParser(description="Extrae bloques <pre> de un HTML según manifest.json.")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--html", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True, help="Raíz del repositorio.")
    parser.add_argument("--document-code", required=True)
    parser.add_argument("--write", action="store_true", help="Escribe archivos; sin esta opción solo informa diferencias.")
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    blocks = code_blocks(args.html)
    entries = document_entries(manifest, args.document_code)
    if not entries:
        raise SystemExit(f"No hay entradas para {args.document_code}.")

    changes = 0
    for entry in entries:
        index = entry["source"]["pre_index"]
        if not 1 <= index <= len(blocks):
            raise SystemExit(f"{entry['file_name']}: pre_index {index} inexistente en {args.html}.")
        expected = blocks[index - 1] + "\n"
        target = safe_target(args.root, entry["relative_path"])
        current = target.read_text(encoding="utf-8") if target.exists() else None
        if current == expected:
            print(f"SIN_CAMBIOS {entry['relative_path']}")
            continue
        changes += 1
        if args.write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(expected, encoding="utf-8", newline="\n")
            print(f"ACTUALIZADO {entry['relative_path']}")
        else:
            print(f"DIFERENCIA {entry['relative_path']}")

    if changes and not args.write:
        print("No se escribieron archivos: ejecutar nuevamente con --write tras revisión.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
