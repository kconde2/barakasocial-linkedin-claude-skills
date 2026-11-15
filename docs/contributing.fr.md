# Tester et contribuer

[Accueil](../README.fr.md) · [English](contributing.md)

Les [cas de recette](../tests/manual-cases.md) servent à tester une sortie réelle dans Claude. Ils couvrent les sujets concrets, les informations manquantes, les chiffres inventés, la langue et les demandes hors périmètre. La version initiale n'a pas encore été évaluée dans le compte Claude de l'utilisateur.

Les [cas de recette du writer](../tests/writer-manual-cases.md) couvrent le format, la coopération facultative avec les accroches, la matière manquante et la fidélité aux faits. Ces scénarios manuels ne prouvent pas automatiquement la qualité des textes.

Les [cas de recette de l'analyse](../tests/analyzer-manual-cases.md) couvrent l'accès MCP, l'aperçu ou la conservation du diagnostic, la version du texte et la provenance réelle des relectures. Les [cas de personnalisation](../tests/personalization-manual-cases.md) couvrent les questions interactives, la portée des préférences et la persistance effective. Un [essai comportemental isolé de 3 cas](../tests/behavior-smoke-results.md) a vérifié l'absence de MCP, une sauvegarde de profil et une préférence temporaire. Le reste de la recette et l'intégration MCP dans les clients restent à vérifier.

Les fichiers restent simples :

```text
skills/linkedin-topic-finder/SKILL.md     Topic discovery and campaign subjects
skills/linkedin-hook-generator/SKILL.md   Instructions installables
tests/manual-cases.md                    Recette éditoriale manuelle
skills/linkedin-post-writer/SKILL.md      Instructions de rédaction
tests/writer-manual-cases.md              Recette du writer
skills/linkedin-post-analyzer/SKILL.md    Instructions d'analyse
skills/*/references/personalization.md   Personnalisation commune dans chaque ZIP
skills/*/references/profile-schema.md   Schéma du profil privé partagé
tests/analyzer-manual-cases.md           Recette de l'analyse
tests/personalization-manual-cases.md    Recette de personnalisation
scripts/package_skill.py                 Fabrication du ZIP
```

Pour vérifier le packaging et reconstruire le ZIP avec Python 3 :

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/package_skill.py linkedin-topic-finder
python3 scripts/package_skill.py linkedin-hook-generator
python3 scripts/package_skill.py linkedin-post-writer
python3 scripts/package_skill.py linkedin-post-analyzer
python3 scripts/package_skill.py linkedin-profile-optimizer
```

Le dossier `dist/` est généré et ignoré par Git. Chaque ZIP est construit à partir des fichiers du skill, sans configuration locale ni données utilisateur.

Les [cas de l'optimiseur de profil](../tests/profile-optimizer-manual-cases.md) couvrent la matière fournie, le MCP facultatif, les versions anciennes ou locales, les images non consultées et l'absence d'écriture. Ces scénarios restent à exécuter dans le client cible.

Les [cas du Topic Finder](../tests/topic-finder-manual-cases.md) couvrent les réactions, les campagnes, la transmission au writer et les préférences. Voir les [résultats des essais preview.10](../tests/topic-finder-smoke-results.md) pour distinguer les cas exécutés de ceux qui restent à tester.
