from __future__ import annotations

import argparse
import ast
import hashlib
import subprocess
import sys
from pathlib import Path

from comun import NAME_PATTERN, code_blocks, document_entries, load_json, safe_target


def fail(message: str) -> None:
    raise ValueError(message)


def normalized(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip("\r\n").splitlines())


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida nombres, contenido y correspondencia de ejemplos Python.")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--html", type=Path, help="Si se indica, verifica cada bloque <pre> en su archivo descargable.")
    parser.add_argument("--document-code", help="Limita la validación a un documento.")
    parser.add_argument("--run", action="store_true", help="Ejecuta los programas autónomos y verifica su salida esperada.")
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
            block = blocks[index - 1]
            autonomous_context = entry["source"].get("downloadable_context") == "autonomo_minimo"
            if autonomous_context and normalized(block) not in normalized(content):
                fail(f"Bloque académico ausente del programa autónomo: {entry['relative_path']}.")
            if not autonomous_context and content.strip("\r\n") != block:
                fail(f"Contenido distinto del HTML: {entry['file_name']}.")
        if args.run:
            execution = entry.get("execution", {})
            if execution.get("mode") != "programa_autonomo":
                fail(f"No está declarado como programa autónomo: {entry['relative_path']}.")
            completed = subprocess.run(
                [sys.executable, str(target)],
                text=True,
                capture_output=True,
                timeout=10,
                check=False,
            )
            if completed.returncode != 0:
                fail(f"Ejecución fallida: {entry['relative_path']}: {completed.stderr.strip()}")
            output = completed.stdout.strip()
            if not output:
                fail(f"La ejecución no produjo salida: {entry['relative_path']}.")
            for expected_output in execution.get("expected_output_contains", []):
                if expected_output not in output:
                    fail(f"Salida inesperada: {entry['relative_path']}: falta {expected_output!r}.")
            print(f"EJECUCION_OK {entry['relative_path']}")
        print(f"OK {entry['relative_path']}")

    print(f"VALIDACION_CORRECTA entradas={len(entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
