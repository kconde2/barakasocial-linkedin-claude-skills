"""Package one self-contained skill as a reproducible ZIP. Python standard library only."""
import argparse
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def package_skill(name, destination):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("Invalid skill name")
    source = ROOT / "skills" / name
    entry = source / "SKILL.md"
    content = entry.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        raise ValueError("Missing YAML frontmatter")
    frontmatter = content.split("---", 2)[1]
    if f"name: {name}\n" not in frontmatter or not re.search(r"^description: .+", frontmatter, re.M):
        raise ValueError("Missing or mismatched name/description")
    files = sorted(p for p in source.rglob("*") if p.is_file())
    if any(p.is_symlink() for p in [source, *source.rglob("*")]):
        raise ValueError("Symlinks are not packaged")
    if any(p.name.startswith(".") or p.suffix not in {".md", ".yaml"} for p in files):
        raise ValueError("Unexpected file in this text-only skill")
    # Repository landing pages are for readers, not installed skill instructions.
    files = [p for p in files if p.relative_to(source).as_posix() not in {"README.md", "README.fr.md"}]
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            info = zipfile.ZipInfo(str(Path(name) / path.relative_to(source)))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name")
    args = parser.parse_args()
    print(package_skill(args.name, ROOT / "dist" / f"{args.name}.zip"))
