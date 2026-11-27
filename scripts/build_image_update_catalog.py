"""Build the isolated visual-skills catalog without breaking preview.14 clients."""
import argparse
import json
from pathlib import Path
import build_update_catalog as builder
import image_skill_updates as updater
from package_skill import ROOT

# Reuse packaging verification with the visual family's own strict allowlist.
builder.SKILLS = updater.SKILLS
builder.read_identity = updater.read_identity
builder.validate_catalog = updater.validate_catalog
builder.unpack = updater.unpack

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-published', action='store_true')
    args = parser.parse_args()
    public = ROOT / 'image-updates.json'
    previous = json.loads(public.read_text()) if public.exists() else {'schema_version': 1, 'skills': {}}
    result = builder.build(previous, ROOT / 'dist', args.verify_published)
    for item in result['skills'].values():
        item['releases'][item['latest']]['notes'] = 'Recherche web de mèmes, aperçus et textes proposés. Montage du candidat choisi avec les outils disponibles. Cinq propositions par défaut.'
    output = public if args.verify_published else ROOT / 'dist/image-updates.json'
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(output)

if __name__ == '__main__':
    main()
