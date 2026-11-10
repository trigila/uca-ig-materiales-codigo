from __future__ import annotations

import argparse
import ast
import hashlib
from pathlib import Path

from comun import NAME_PATTERN, code_blocks, document_entries, load_json, safe_target


def fail(message: str) -> None:
    raise ValueError(message)


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida nombres, contenido y correspondencia de ejemplos Python.")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--html", type=Path, help="Si se indica, compara cada archivo con su bloque <pre>.")
    parser.add_argument("--document-code", help="Limita la validación a un documento.")
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    entries = manifest.get("entries", [])
    if args.document_code:
        entries = document_entries(manifest, args.document_code)
    if not entries:
        fail("El manifiesto no contiene entradas para validar.")

    paths: set[str] = set()
    blocks = code_blocks(args.html) if args.html else []
    for entry in entries:
        required = {"document_code", "example_id", "variant", "file_name", "relative_path", "source", "links"}
        missing = required.difference(entry)
        if missing:
            fail(f"Entrada incompleta: faltan {sorted(missing)}.")
        if not NAME_PATTERN.fullmatch(entry["file_name"]):
            fail(f"Nombre inválido: {entry['file_name']}.")
        if entry["relative_path"] in paths:
            fail(f"Ruta duplicada: {entry['relative_path']}.")
        paths.add(entry["relative_path"])
        if Path(entry["relative_path"]).name != entry["file_name"]:
            fail(f"Nombre y ruta no coinciden: {entry['relative_path']}.")

        target = safe_target(args.root, entry["relative_path"])
        if not target.is_file():
            fail(f"Archivo faltante: {entry['relative_path']}.")
        content = target.read_text(encoding="utf-8")
        if "\t" in content:
            fail(f"Tabulación no permitida: {entry['relative_path']}.")
        ast.parse(content, filename=str(target))
        expected_hash = entry.get("content_sha256")
        if expected_hash and hashlib.sha256(target.read_bytes()).hexdigest().upper() != expected_hash.upper():
            fail(f"SHA-256 distinto del manifiesto: {entry['relative_path']}.")

        if args.html:
            index = entry["source"].get("pre_index")
            if not isinstance(index, int) or not 1 <= index <= len(blocks):
                fail(f"pre_index inválido para {entry['file_name']}.")
            if content.strip("\r\n") != blocks[index - 1]:
                fail(f"Contenido distinto del HTML: {entry['file_name']}.")
        print(f"OK {entry['relative_path']}")

    print(f"VALIDACION_CORRECTA entradas={len(entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
