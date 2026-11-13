# Claude Skills for LinkedIn · BarakaSocial

Des skills gratuits pour travailler ses contenus LinkedIn avec Claude. Commencer par une tâche précise, tester le résultat puis améliorer le skill.

**Première version de test : `0.1.0-preview.1`.** Un seul skill est disponible. Les autres catégories seront ajoutées quand leurs premiers skills seront prêts.

## Le premier skill

| Skill | Catégorie | Ce qu'il fait | Prérequis |
| --- | --- | --- | --- |
| [LinkedIn Hook Generator](skills/linkedin-hook-generator/SKILL.md) | Écriture | Propose des accroches cohérentes avec ton sujet ou ton brouillon, sans inventer de faits. | Le texte ou le sujet à travailler. Aucun compte BarakaSocial requis. |

- [Lire le SKILL.md](skills/linkedin-hook-generator/SKILL.md)
- [Ouvrir le Markdown brut](https://raw.githubusercontent.com/kconde2/barakasocial-linkedin-claude-skills/main/skills/linkedin-hook-generator/SKILL.md)
- [Télécharger le ZIP de la version de test](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.1/linkedin-hook-generator.zip)
- [Voir la version publiée](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/tag/v0.1.0-preview.1)

## Installer dans Claude Code

Un dossier contenant `SKILL.md` peut être installé dans `~/.claude/skills/` pour un usage personnel ou `.claude/skills/` dans un projet. [Documentation officielle](https://code.claude.com/docs/en/skills).

Demande à copier dans Claude Code :

```text
Installe le skill linkedin-hook-generator du dépôt public
https://github.com/kconde2/barakasocial-linkedin-claude-skills
à partir de la version v0.1.0-preview.1 dans mes skills personnels.
Lis son SKILL.md avant l'installation. Si un skill du même nom existe déjà,
compare son origine et son contenu avant de le remplacer.
Ne modifie pas mes autres skills ni ma configuration MCP.
```

Le chemin source est `skills/linkedin-hook-generator/SKILL.md`. Après installation, demande explicitement d'utiliser `linkedin-hook-generator` ou invoque `/linkedin-hook-generator` dans Claude Code.

## Installer dans Claude

Télécharge le ZIP du skill puis importe-le dans **Personnaliser / Customize > Skills**, via l'ajout d'un skill. Les capacités requises et les contrôles peuvent varier selon ton espace. [Procédure officielle](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

Coller les instructions dans une conversation permet de les essayer. Cela ne constitue pas une installation persistante dans tous les clients.

## Essayer

```text
Utilise linkedin-hook-generator.
Je m'adresse aux freelances. Mon sujet : un client ajoute des demandes
après la validation du devis. Mon idée : préciser le périmètre avant de commencer.
Propose cinq accroches sobres sans inventer de chiffres ni de résultats clients.
```

Le skill fournit des options et explique brièvement son choix. Il ne garantit pas une portée, un taux d'engagement ou une performance mesurée.

## Mettre à jour

Les versions téléchargées ne se mettent pas à jour automatiquement depuis ce dépôt.

Dans Claude Code :

```text
Compare mon skill linkedin-hook-generator avec la dernière version publiée sur
https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases
Indique les changements puis mets-le à jour en conservant mes adaptations locales.
Si mon skill vient d'un autre dépôt, signale-le avant de le remplacer.
Ne touche pas aux autres skills ni à la configuration MCP.
```

Dans Claude, télécharge le ZIP de la nouvelle version et remplace la version installée depuis l'interface de gestion des skills.

## Tester et contribuer

Les [cas de recette](tests/manual-cases.md) servent à tester une sortie réelle dans Claude. Ils couvrent les sujets concrets, les informations manquantes, les chiffres inventés, la langue et les demandes hors périmètre. La version initiale n'a pas encore été évaluée dans le compte Claude de l'utilisateur.

Les fichiers restent simples :

```text
skills/linkedin-hook-generator/SKILL.md   Instructions installables
tests/manual-cases.md                    Recette éditoriale manuelle
scripts/package_skill.py                 Fabrication du ZIP
```

Pour vérifier le packaging et reconstruire le ZIP avec Python 3 :

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/package_skill.py linkedin-hook-generator
```

Le dossier `dist/` est généré et ignoré par Git. Chaque ZIP est construit à partir des fichiers du skill, sans configuration locale ni données utilisateur.

## BarakaSocial

[BarakaSocial](https://barakasocial.com) aide à préparer et organiser ses contenus LinkedIn. Ce premier skill fonctionne indépendamment de l'application. Aucune connexion MCP n'est installée automatiquement.

Le projet est indépendant d'Anthropic et de LinkedIn. Les skills et la documentation de ce dépôt sont distribués sous [licence MIT](LICENSE).
