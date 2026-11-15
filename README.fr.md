# Claude Skills for LinkedIn · BarakaSocial

Des skills gratuits pour travailler ses contenus LinkedIn avec Claude. Commencer par une tâche précise, tester le résultat puis améliorer le skill.

[English](README.md) | **Français**

Donne-lui un post complet ou des notes. Il travaille avec la matière disponible et pose une question ciblée seulement si nécessaire.

Les instructions du skill sont en anglais. Les accroches et leurs explications suivent la langue de ta demande sauf si tu choisis explicitement une autre langue.

**Sources de test : `0.1.0-preview.7` pour les 3 skills. Pas encore de release GitHub avec les ZIP de cette version.** La version publiée du générateur d'accroches reste `0.1.0-preview.5`. Elle ne contient pas la nouvelle personnalisation commune. Construis les ZIP ci-dessous pour tester les candidats localement.

## Les skills

| Skill | Catégorie | Ce qu'il fait | Prérequis |
| --- | --- | --- | --- |
| [LinkedIn Hook Generator](skills/linkedin-hook-generator/SKILL.md) | Écriture | Propose des accroches cohérentes avec ton sujet ou ton brouillon, sans inventer de faits. | Le texte ou le sujet à travailler. Aucun compte BarakaSocial requis. |
| [LinkedIn Post Writer](skills/linkedin-post-writer/SKILL.md) | Écriture | Rédige un post complet ou des variantes cohérentes à partir de ta matière. | Des notes ou un brouillon. Aucun compte ni autre skill requis. |
| [LinkedIn Post Analyzer](skills/linkedin-post-analyzer/SKILL.md) | Analyse | Relit un post avec les critères actuels de BarakaSocial et son calcul officiel du score. | Un post et un compte MCP BarakaSocial connecté. |

- [Lire le SKILL.md](skills/linkedin-hook-generator/SKILL.md)
- [Ouvrir le Markdown brut](https://raw.githubusercontent.com/kconde2/barakasocial-linkedin-claude-skills/main/skills/linkedin-hook-generator/SKILL.md)
- [Télécharger le ZIP des accroches déjà publié (preview.5)](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.5/linkedin-hook-generator.zip)
- [Voir la version publiée des accroches (preview.5)](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/tag/v0.1.0-preview.5)

## Installer dans Claude Code

Un dossier contenant `SKILL.md` peut être installé dans `~/.claude/skills/` pour un usage personnel ou `.claude/skills/` dans un projet. [Documentation officielle](https://code.claude.com/docs/en/skills).

Pour installer la version des accroches déjà publiée, copie cette demande dans Claude Code :

```text
Installe le skill linkedin-hook-generator du dépôt public
https://github.com/kconde2/barakasocial-linkedin-claude-skills
à partir de la version v0.1.0-preview.5 dans mes skills personnels.
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
Propose des accroches sobres sans inventer de chiffres ni de résultats clients.
```

Par défaut, le skill compare trois accroches dans un tableau : l'ouverture, la raison de lire la suite et son avis éditorial. Il recommande ensuite une option. Tu peux demander un autre nombre ou format. Si ton accroche fonctionne déjà, il peut recommander de la conserver plutôt que de la remplacer sans raison. Il ne garantit pas une portée, un taux d'engagement ou une performance mesurée.

## Comment ça fonctionne

| Tu fournis | Le skill travaille sur | Tu reçois |
| --- | --- | --- |
| Un post complet | L'ouverture existante et ce que le corps apporte réellement. | 3 accroches comparées et une recommandation, qui peut être de garder l'originale. |
| Des notes ou un sujet | La matière disponible, sans inventer d'histoire. | Des ouvertures adaptées et, si nécessaire, une question ciblée ou un élément à développer. |
| Un retour sur une option | L'accroche choisie, en conservant les faits. | Une retouche ciblée, sans réécrire tout le post. |

Il choisit des angles déjà présents dans ta matière : identification, contraste, conséquence, injustice, découverte, dilemme ou utilité pratique. Ce sont des possibilités, pas des cases à cocher pour chaque post.

Il privilégie une narration orale et active. En français, le présent de narration ou le passé composé servent la scène, tout en préservant la chronologie et les effets littéraires voulus. Les quantités s'écrivent en chiffres (2 appels, 6 mois). Les articles comme « un client » et les citations exactes sont préservés.

Aucun compte ni MCP n'est requis. Si tu demandes explicitement le contexte BarakaSocial, le skill utilise uniquement les outils de lecture disponibles et autorisés. Il signale les accès manquants. Il ne réécrit pas le corps, n'enregistre pas de brouillon et ne programme ni ne publie rien.

## Rédiger un post complet

Les sources de test de `linkedin-post-writer` sont disponibles dans ce dépôt. Construis son ZIP avec la commande ci-dessous pour l'essayer.

```text
Utilise linkedin-post-writer. Rédige un seul post pour les designers freelances.
Un client valide ma maquette puis demande 2 écrans supplémentaires.
Je propose un devis séparé avant de commencer. Garde un ton direct.
N'invente ni sa réponse ni le résultat.
```

Il demande si tu veux 1 post ou plusieurs variantes uniquement quand ce choix manque. Il conserve une accroche déjà choisie. Sinon, il utilise `linkedin-hook-generator` lorsqu'il est disponible, choisit une ouverture puis poursuit la rédaction. Il signale cet usage réel hors du post. Sans ce skill, il travaille l'accroche directement.

Si la matière conduit à un texte générique, il explique ce qui manque et propose des options adaptées : ajouter des détails réels, choisir une forme courte ou mettre le sujet de côté. L'auteur choisit le ton. Une version encore limitée reste un brouillon à enrichir. Il ne sauvegarde rien, ne déclenche pas d'analyse payante et ne programme ni ne publie rien.

## Analyser un post

`linkedin-post-analyzer` nécessite le MCP BarakaSocial. Sans les outils ou les accès requis, il explique ce qui manque puis s'arrête au lieu d'inventer un score officiel. Ses sources de test sont disponibles dans ce dépôt. Construis son ZIP ci-dessous pour l'essayer.

```text
Utilise linkedin-post-analyzer. Analyse ce brouillon sans rien enregistrer.
Garde le texte inchangé et identifie l'amélioration la plus utile :
[colle le post]
```

Par défaut, il lit `get_analysis_criteria`, évalue le texte choisi puis appelle `preview_post_analysis` sans conserver de diagnostic. Si l'utilisateur demande explicitement d'enregistrer le diagnostic, il utilise `submit_post_analysis`. Pour un post identifié dans BarakaSocial, il lit le texte actuel avec `get_post`. Une version retouchée dans le chat ne remplace pas silencieusement la version enregistrée.

Le modèle du client produit l'évaluation éditoriale. BarakaSocial calcule le score officiel à partir de cette évaluation. Ce n'est pas une seconde analyse IA indépendante ni une prédiction de portée. Une demande d'analyse ne réécrit pas le texte. La correction exige une demande correspondante. Le skill distingue la version notée d'une version corrigée ensuite.

Plusieurs relecteurs peuvent contribuer uniquement sur demande explicite et si le client le permet. Ils examinent le même texte avec des périmètres complémentaires puis l'agent principal rassemble leurs observations réelles en une évaluation. Il n'invente pas de relecteurs, ne moyenne pas des scores imaginaires et ne relance pas des boucles de notation. Le skill ne crée, ne modifie, ne programme et ne publie aucun post. Enregistrer un diagnostic n'enregistre pas un post.

## Personnaliser les 3 skills

La personnalisation est commune aux skills. Ce n'est pas un quatrième skill à installer. Chaque ZIP candidat contient `references/personalization.md` pour rester utilisable seul.

Tu peux demander :

```text
Personnalise ces skills LinkedIn pour moi. Réutilise ce que tu sais déjà.
Demande uniquement les préférences manquantes sur mon public, mon ton
et ce que je veux éviter. Garde ces choix dans cette conversation pour l'instant.
```

Le skill peut proposer une configuration facultative au premier usage ou répondre à une demande explicite de personnalisation. Aucun questionnaire n'est obligatoire pour traiter une demande déjà assez précise. Il utilise `AskUserQuestion` dans Claude Code ou `request_user_input` / `request_user_input_async` lorsque l'outil est disponible et autorisé dans le client actuel. Sinon, il pose les questions dans le chat. Il ne prend pas le silence pour une réponse et ne redemande pas les informations déjà fournies.

Tes instructions actuelles priment sur un profil enregistré. Une préférence pour un seul post ne devient pas automatiquement un réglage permanent. Les préférences communes orientent le ton, le public et la présentation. Elles ne remplacent pas les critères d'analyse de BarakaSocial et n'autorisent pas l'accès à un compte.

Pour conserver les préférences entre les sessions, demande leur enregistrement dans un emplacement privé de ton choix. Avec un accès aux fichiers, l'emplacement proposé est `~/.config/barakasocial/editorial-profile.json`, hors du dépôt et des dossiers des skills installés. Les 3 skills peuvent partager ce fichier. Ils n'écrivent pas de profil sans demande. Une mise à jour des instructions doit laisser ce fichier intact. Ne jamais committer de profil personnel ni l'inclure dans un ZIP distribué.

Sans accès à un stockage durable, les préférences restent dans la conversation. L'assistant peut fournir un profil à copier ou télécharger sans prétendre l'avoir enregistré ni promettre de le retrouver automatiquement. La configuration ne modifie pas le MCP et ne lit pas automatiquement les données personnelles du compte. Pour personnaliser après installation, demande explicitement d'installer **et de configurer** le skill ou configure-le au premier usage. Aucun questionnaire universel d'installation n'est supposé.

## Outils MCP BarakaSocial

Les accroches et la rédaction fonctionnent sans outil obligatoire. Elles peuvent utiliser les lectures MCP autorisées quand l'utilisateur demande le contexte du compte. L'analyse nécessite le MCP BarakaSocial connecté. La disponibilité dépend des outils exposés par le connecteur dans le client utilisé.

Le tableau décrit les outils pertinents disponibles. Les accroches et la rédaction utilisent des lectures facultatives plutôt qu'une séquence obligatoire. L'analyse suit le parcours de critères et de calcul décrit plus haut.

| Besoin | Outils | Rôle |
| --- | --- | --- |
| Préparer la rédaction | `get_writing_brief` | Récupérer la méthode publique puis éventuellement le contexte personnel autorisé du sujet. |
| Respecter la voix | `get_writing_context`, `get_config_profile` | Consulter les préférences et les exemples de style autorisés. |
| Comprendre l'auteur | `get_linkedin_profile` | Lire le profil enregistré dans BarakaSocial, sans appel à LinkedIn. |
| Trouver de la matière | `find_reference_posts`, `list_posts`, `get_post` | Retrouver les posts du compte et lire les références retenues. |
| Partir d'une idée | `list_ideas`, `get_idea`, `prepare_post_from_idea` | Lire une idée et éventuellement son contexte de rédaction et ses références autorisées. Aucun post n'est créé. |
| Contrôler le texte | `lint_post` | Vérifier les règles mécaniques sans enregistrement, appel LLM ou crédit. |
| Analyser | `get_analysis_criteria`, `preview_post_analysis`, `submit_post_analysis`, `get_post_analysis` | Lire les critères, calculer un score à partir de l'évaluation du client, conserver ou consulter un diagnostic. |

### Périmètre des skills

| Skill | Usage prévu |
| --- | --- |
| `linkedin-hook-generator` | Accroches à partir du texte fourni. Lectures MCP facultatives pour enrichir le contexte. |
| `linkedin-post-writer` | Post ou variantes à partir de la matière fournie. Lectures MCP facultatives et recours au skill d'accroches s'il est disponible. |
| `linkedin-post-analyzer` | MCP obligatoire. Aperçu par défaut. Diagnostic enregistré uniquement sur demande explicite. |

Pour l'analyse, le modèle client produit l'évaluation selon `get_analysis_criteria`. BarakaSocial applique ensuite le calcul officiel avec `preview_post_analysis` ou `submit_post_analysis`. Ces outils ne déclenchent pas le modèle d'analyse interne du serveur. `submit_post_analysis` conserve le diagnostic avec la provenance `mcp-client`. `get_post_analysis` lit un diagnostic existant sans lancer d'analyse. Ce parcours ne consomme aucun crédit.

Les outils `save_post`, `update_post`, `schedule_post`, `prepare_post_image`, `confirm_post_image` et `cancel_post_image` existent également. Ils restent hors du périmètre des 3 skills. Leur présence dans le connecteur n'autorise pas une sauvegarde, une programmation ou une modification automatique. Ce catalogue ne rend pas chaque outil obligatoire et n'autorise aucune action hors du périmètre demandé.

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

Les [cas de recette du writer](tests/writer-manual-cases.md) couvrent le format, la coopération facultative avec les accroches, la matière manquante et la fidélité aux faits. Ces scénarios manuels ne prouvent pas automatiquement la qualité des textes.

Les [cas de recette de l'analyse](tests/analyzer-manual-cases.md) couvrent l'accès MCP, l'aperçu ou la conservation du diagnostic, la version du texte et la provenance réelle des relectures. Les [cas de personnalisation](tests/personalization-manual-cases.md) couvrent les questions interactives, la portée des préférences et la persistance effective. Un [essai comportemental isolé de 3 cas](tests/behavior-smoke-results.md) a vérifié l'absence de MCP, une sauvegarde de profil et une préférence temporaire. Le reste de la recette et l'intégration MCP dans les clients restent à vérifier.

Les fichiers restent simples :

```text
skills/linkedin-hook-generator/SKILL.md   Instructions installables
tests/manual-cases.md                    Recette éditoriale manuelle
skills/linkedin-post-writer/SKILL.md      Instructions de rédaction
tests/writer-manual-cases.md              Recette du writer
skills/linkedin-post-analyzer/SKILL.md    Instructions d'analyse
skills/*/references/personalization.md   Personnalisation commune dans chaque ZIP
tests/analyzer-manual-cases.md           Recette de l'analyse
tests/personalization-manual-cases.md    Recette de personnalisation
scripts/package_skill.py                 Fabrication du ZIP
```

Pour vérifier le packaging et reconstruire le ZIP avec Python 3 :

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/package_skill.py linkedin-hook-generator
python3 scripts/package_skill.py linkedin-post-writer
python3 scripts/package_skill.py linkedin-post-analyzer
```

Le dossier `dist/` est généré et ignoré par Git. Chaque ZIP est construit à partir des fichiers du skill, sans configuration locale ni données utilisateur.

## BarakaSocial

[BarakaSocial](https://barakasocial.com) aide à préparer et organiser ses contenus LinkedIn. Les accroches et la rédaction fonctionnent indépendamment de l'application. L'analyse nécessite le MCP BarakaSocial. Aucune connexion MCP n'est installée automatiquement.

Le projet est indépendant d'Anthropic et de LinkedIn. Les skills et la documentation de ce dépôt sont distribués sous [licence MIT](LICENSE).
