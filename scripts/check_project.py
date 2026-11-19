"""Preverjanja trenutnega mejnika brez zunanjih paketov ali omrežja."""

import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    ".gitignore",
    ".github/workflows/ci.yml",
    "app/README.md",
    "importer/README.md",
    "supabase/README.md",
    "dokumentacija/README.md",
    "dokumentacija/nacrt-dela.md",
    "dokumentacija/zacetne-naloge.md",
    "dokumentacija/mockupi/koncept.png",
    "dokumentacija/EventRadar_Prototipna_Dokumentacija.docx",
)


def main():
    errors = []
    for name in REQUIRED:
        path = ROOT / name
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Manjka zahtevana datoteka ali je prazna: {name}")

    # Pregledava le projektne mape, da lokalna okolja ne vplivajo na CI.
    markdown = [ROOT / "README.md"]
    for folder in ("app", "importer", "supabase", "dokumentacija"):
        markdown.extend((ROOT / folder).rglob("*.md"))
    for path in markdown:
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"Datoteka ni veljaven UTF-8: {path.relative_to(ROOT)}")
            continue
        if not content.startswith("# "):
            errors.append(f"Manjka glavni naslov: {path.relative_to(ROOT)}")
        for target in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", content):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(f"Povezava izven projekta: {target}")
                continue
            # Točno velikost črk preveriva tudi na Windows, ker CI teče na Linuxu.
            current = ROOT
            for part in resolved.relative_to(ROOT).parts:
                if not current.is_dir() or part not in {p.name for p in current.iterdir()}:
                    errors.append(f"Neveljavna povezava v {path.relative_to(ROOT)}: {target}")
                    break
                current /= part

    docx = ROOT / "dokumentacija/EventRadar_Prototipna_Dokumentacija.docx"
    try:
        with zipfile.ZipFile(docx) as archive:
            if archive.testzip() is not None:
                errors.append("Wordov dokument vsebuje poškodovan zapis ZIP.")
            tree = ElementTree.fromstring(archive.read("word/document.xml"))
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            text = " ".join(node.text or "" for node in tree.findall(".//w:t", ns))
            for section in (
                "Opis projekta", "Glavne funkcionalnosti", "Primeri uporabe",
                "Mockupi in navigacija", "podatkovni model", "arhitektura",
            ):
                if section.casefold() not in text.casefold():
                    errors.append(f"V zasnovi manjka razdelek: {section}")
            media = [name for name in archive.namelist() if name.startswith("word/media/")]
            mockup = ROOT / "dokumentacija/mockupi/koncept.png"
            if not media:
                errors.append("Wordov dokument ne vsebuje mockupa.")
            elif mockup.is_file() and mockup.read_bytes() != archive.read("word/media/image1.png"):
                errors.append("Izvoženi mockup se razlikuje od obstoječega dokumenta.")
    except (OSError, zipfile.BadZipFile, KeyError, ElementTree.ParseError) as exc:
        errors.append(f"Wordovega dokumenta ni mogoče preveriti: {exc}")

    if errors:
        for error in errors:
            print(f"NAPAKA: {error}", file=sys.stderr)
        return 1
    print("OK: struktura, dokumentacija, mockup in lokalne povezave.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
