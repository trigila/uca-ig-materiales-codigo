from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from comun import document_entries, load_json

PRE_PATTERN = re.compile(r"<pre\b[^>]*>.*?</pre>", re.DOTALL | re.IGNORECASE)
STYLE = """
/* Enlaces de código generados desde manifest.json. */
.ig-code-download { display:inline-block; margin-top:.65rem; color:#1768b5; font-size:.82rem; font-weight:700; line-height:1.35; text-decoration:underline; text-underline-offset:.16em; }
.ig-code-download:hover, .ig-code-download:focus-visible { color:#173f78; outline:2px solid #b9cfe8; outline-offset:3px; border-radius:2px; }
@media print { .ig-code-download { display:inline; margin-top:0; color:#173f78; font-size:.72rem; -webkit-print-color-adjust:exact; print-color-adjust:exact; } }
""".strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Genera una copia HTML con enlaces de descarga desde el manifiesto.")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--html", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--document-code", required=True)
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    config = load_json(args.config)
    anchor_class = config["html"]["anchor_class"]
    anchor_text = config["html"]["anchor_text"]
    entries = document_entries(manifest, args.document_code)
    source = args.html.read_text(encoding="utf-8")
    if anchor_class in source:
        raise SystemExit("El HTML de entrada ya contiene enlaces generados; usar una fuente sin modificar.")

    blocks = list(PRE_PATTERN.finditer(source))
    replacements: list[tuple[int, int, str]] = []
    for entry in entries:
        url = entry.get("links", {}).get("download")
        if not url:
            raise SystemExit(f"Enlace de descarga pendiente: {entry['relative_path']}.")
        index = entry["source"].get("pre_index")
        if not isinstance(index, int) or not 1 <= index <= len(blocks):
            raise SystemExit(f"pre_index inválido para {entry['file_name']}.")
        anchor = (
            f'\n<a class="{html.escape(anchor_class, quote=True)}" '
            f'href="{html.escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">'
            f'{html.escape(anchor_text)}</a>'
        )
        block = blocks[index - 1]
        replacements.append((block.end(), block.end(), anchor))

    updated = source
    for start, end, replacement in sorted(replacements, reverse=True):
        updated = updated[:start] + replacement + updated[end:]
    if "</style>" not in updated:
        raise SystemExit("No se encontró </style> para incorporar la regla visual.")
    updated = updated.replace("</style>", STYLE + "\n</style>", 1)
    if args.output.exists():
        raise SystemExit(f"La salida ya existe: {args.output}. No se sobrescribió.")
    args.output.write_text(updated, encoding="utf-8", newline="\n")
    print(f"HTML_GENERADO {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
