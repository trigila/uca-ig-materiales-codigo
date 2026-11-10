from __future__ import annotations

import argparse
import hashlib
import re
import urllib.request
from pathlib import Path
from urllib.parse import unquote, urlparse

from comun import load_json, safe_target


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida consistencia local de enlaces publicados.")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--require-public", action="store_true", help="Falla si falta un enlace público validado.")
    parser.add_argument("--check-downloads", action="store_true", help="Descarga cada URL y verifica nombre y SHA-256.")
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    config = load_json(args.config)
    repository = config.get("repository", {})
    owner = repository.get("owner")
    repo = repository.get("name")
    branch = repository.get("branch")
    link_generation = config.get("link_generation", {})
    view_template = link_generation.get("view_template")
    download_template = link_generation.get("download_template")
    pending = 0

    for entry in manifest.get("entries", []):
        safe_target(args.root, entry["relative_path"])
        links = entry.get("links", {})
        view = links.get("view")
        download = links.get("download")
        if owner and repo and branch and view_template and view:
            expected = view_template.format(owner=owner, repository=repo, branch=branch, path=entry["relative_path"])
            if view != expected:
                raise SystemExit(f"Vista no coincide con la configuración: {entry['relative_path']}.")
        if owner and repo and branch and download_template and download:
            expected = download_template.format(
                owner=owner, repository=repo, branch=branch, path=entry["relative_path"], filename=entry["file_name"]
            )
            if download != expected:
                raise SystemExit(f"Descarga no coincide con la configuración: {entry['relative_path']}.")
        if not view or not download:
            pending += 1
            print(f"PENDIENTE {entry['relative_path']}")
        else:
            print(f"OK {entry['relative_path']}")
            if args.check_downloads:
                expected_hash = entry.get("content_sha256")
                if not expected_hash:
                    raise SystemExit(f"Falta content_sha256: {entry['relative_path']}.")
                with urllib.request.urlopen(download, timeout=30) as response:
                    payload = response.read()
                    disposition = response.headers.get("Content-Disposition", "")
                    final_url = response.geturl()
                filename = re.search(r'filename="?([^";]+)', disposition, flags=re.IGNORECASE)
                downloaded_name = filename.group(1) if filename else unquote(urlparse(final_url).path.rsplit("/", 1)[-1])
                if downloaded_name != entry["file_name"]:
                    raise SystemExit(f"Nombre de descarga no verificable o incorrecto: {entry['relative_path']}.")
                actual_hash = hashlib.sha256(payload).hexdigest().upper()
                if actual_hash != expected_hash.upper():
                    raise SystemExit(f"Bytes descargados distintos: {entry['relative_path']}.")
                print(f"DESCARGA_OK {entry['relative_path']}")

    if pending:
        print(f"ENLACES_PENDIENTES entradas={pending}")
        return 1 if args.require_public else 0
    print("ENLACES_CONFIGURADOS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
