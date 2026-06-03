#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
package_plugins.py
Empacota cada plugin em um arquivo .zip pronto para upload no Claude Cowork.

USO:
  python3 scripts/package_plugins.py

  # Empacotar apenas plugins específicos:
  python3 scripts/package_plugins.py commercial-legal employment-legal

RESULTADO:
  dist/
    commercial-legal.zip
    employment-legal.zip
    ... (um zip por plugin selecionado)
    todos-os-plugins.zip   ← pacote completo
"""

import sys
import io
import json
import zipfile
import shutil
from pathlib import Path

# Garante saída UTF-8 no Windows (terminal cp1252)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).parent.parent.resolve()
DIST_DIR = REPO_ROOT / "dist"

ALL_PLUGINS = [
    "ai-governance-legal",
    "commercial-legal",
    "corporate-legal",
    "employment-legal",
    "ip-legal",
    "law-student",
    "legal-builder-hub",
    "legal-clinic",
    "litigation-legal",
    "privacy-legal",
    "product-legal",
    "regulatory-legal",
]

# Padrões de arquivo a excluir dos zips
EXCLUDE_PATTERNS = {
    ".git", ".DS_Store", "__pycache__", "*.pyc",
    "*.pyo", "node_modules", ".env", "dist",
}


def should_exclude(path: Path) -> bool:
    for part in path.parts:
        if part in EXCLUDE_PATTERNS:
            return True
        if part.endswith(".pyc") or part.endswith(".pyo"):
            return True
    return False


def zip_plugin(plugin_name: str) -> Path | None:
    plugin_dir = REPO_ROOT / plugin_name
    manifest = plugin_dir / ".claude-plugin" / "plugin.json"

    if not manifest.exists():
        print(f"  ⚠  {plugin_name}: plugin.json não encontrado — pulando")
        return None

    # Lê o nome amigável do manifest
    try:
        meta = json.loads(manifest.read_text(encoding="utf-8"))
        display = meta.get("displayName", plugin_name)
    except Exception:
        display = plugin_name

    zip_path = DIST_DIR / f"{plugin_name}.zip"

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file in sorted(plugin_dir.rglob("*")):
            rel = file.relative_to(REPO_ROOT)
            if should_exclude(rel):
                continue
            if file.is_file():
                zf.write(file, rel)

    size_kb = zip_path.stat().st_size // 1024
    size_str = f"{size_kb} KB" if size_kb < 1024 else f"{size_kb // 1024:.1f} MB"
    print(f"  ✓  {plugin_name}.zip  ({size_str})  — {display}")
    return zip_path


def zip_all(plugins: list[str]) -> Path:
    zip_path = DIST_DIR / "todos-os-plugins.zip"
    total_files = 0

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for plugin_name in plugins:
            plugin_dir = REPO_ROOT / plugin_name
            if not (plugin_dir / ".claude-plugin" / "plugin.json").exists():
                continue
            for file in sorted(plugin_dir.rglob("*")):
                rel = file.relative_to(REPO_ROOT)
                if should_exclude(rel):
                    continue
                if file.is_file():
                    zf.write(file, rel)
                    total_files += 1

    size_kb = zip_path.stat().st_size // 1024
    size_str = f"{size_kb} KB" if size_kb < 1024 else f"{size_kb // 1024:.1f} MB"
    print(f"  ✓  todos-os-plugins.zip  ({size_str})  — {total_files} arquivos")
    return zip_path


def main():
    selected = sys.argv[1:] if len(sys.argv) > 1 else ALL_PLUGINS

    # Valida plugins solicitados
    unknown = [p for p in selected if p not in ALL_PLUGINS]
    if unknown:
        print(f"Plugins desconhecidos: {', '.join(unknown)}")
        print(f"Disponíveis: {', '.join(ALL_PLUGINS)}")
        sys.exit(1)

    # Recria dist/
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    print()
    print("━" * 52)
    print("  Empacotando plugins para distribuição")
    print("━" * 52)
    print()

    created = []
    for plugin in selected:
        path = zip_plugin(plugin)
        if path:
            created.append(path)

    print()
    print("  Criando pacote completo...")
    zip_all(selected)

    print()
    print("━" * 52)
    print(f"  Arquivos criados em: dist/")
    print()
    print("  Como distribuir para seus colegas:")
    print("  1. Envie o .zip pelo e-mail, Teams ou pasta compartilhada")
    print("  2. Colega abre Claude Desktop")
    print("  3. Cowork → Customize → Browse plugins → Upload")
    print("  4. Seleciona o .zip e aguarda a instalação")
    print("━" * 52)
    print()


if __name__ == "__main__":
    main()
