from __future__ import annotations

import html
import json
import re
from pathlib import Path

NAME_PATTERN = re.compile(
    r"^IG\.A\.\d{2}_EX\d{2,}_(?:ESPERADO|NO_ADMITIDO|ALTERNATIVA)(?:_\d+)?\.py$"
)
PRE_PATTERN = re.compile(r"<pre\b[^>]*>(.*?)</pre>", re.DOTALL | re.IGNORECASE)


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def code_blocks(html_path: Path) -> list[str]:
    source = html_path.read_text(encoding="utf-8")
    return [
        html.unescape(re.sub(r"<[^>]+>", "", block)).strip("\r\n")
        for block in PRE_PATTERN.findall(source)
    ]


def document_entries(manifest: dict, document_code: str) -> list[dict]:
    entries = [entry for entry in manifest.get("entries", []) if entry.get("document_code") == document_code]
    return sorted(entries, key=lambda entry: entry["source"]["pre_index"])


def safe_target(root: Path, relative_path: str) -> Path:
    candidate = root / relative_path
    resolved_root = root.resolve()
    resolved_target = candidate.resolve()
    try:
        resolved_target.relative_to(resolved_root)
    except ValueError as error:
        raise ValueError(f"Ruta fuera del repositorio: {relative_path}") from error
    return candidate
