# Guide : installer, utiliser et personnaliser

[Accueil](../README.fr.md) · [English](guide.md)

## Installer dans Claude Code

Un dossier contenant `SKILL.md` peut être installé dans `~/.claude/skills/` pour un usage personnel ou `.claude/skills/` dans un projet. [Documentation officielle](https://code.claude.com/docs/en/skills).

Pour installer les sources actuelles des accroches, copie cette demande dans Claude Code. Remplace le nom du skill par `linkedin-post-writer`, `linkedin-post-analyzer` ou `linkedin-profile-optimizer` pour installer un autre skill :

```text
Installe le skill linkedin-hook-generator du dépôt public
https://github.com/kconde2/barakasocial-linkedin-claude-skills
à partir de la branche main dans mes skills personnels.
Copie le dossier complet du skill, y compris references/.
Lis son SKILL.md avant l'installation. Si un skill du même nom existe déjà,
compare son origine et son contenu avant de le remplacer.
Ne modifie pas mes autres skills ni ma configuration MCP.
```

Avec Codex, tu peux demander la même installation en précisant tes skills Codex. L'emplacement et les outils de configuration dépendent du client.

Le chemin source est `skills/linkedin-hook-generator/SKILL.md`. Après installation, demande explicitement d'utiliser `linkedin-hook-generator` ou invoque `/linkedin-hook-generator` dans Claude Code.

## Installer dans Claude

La version source actuelle est `0.1.0-preview.8`. Elle ne possède pas encore de release avec les ZIP. Le [ZIP des accroches preview.5](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.5/linkedin-hook-generator.zip) est une ancienne version sans la personnalisation commune. Pour obtenir un ZIP des sources actuelles, consulte le [guide de contribution](contributing.fr.md).

Quand tu disposes du ZIP souhaité, importe-le dans **Personnaliser / Customize > Skills**, via l'ajout d'un skill. Les capacités requises et les contrôles peuvent varier selon ton espace. [Procédure officielle](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

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

Les sources de test de `linkedin-post-writer` sont disponibles dans ce dépôt. Construis son ZIP avec les commandes du [guide de contribution](contributing.fr.md) pour l'essayer.

```text
Utilise linkedin-post-writer. Rédige un seul post pour les designers freelances.
Un client valide ma maquette puis demande 2 écrans supplémentaires.
Je propose un devis séparé avant de commencer. Garde un ton direct.
N'invente ni sa réponse ni le résultat.
```

Il demande si tu veux 1 post ou plusieurs variantes uniquement quand ce choix manque. Il conserve une accroche déjà choisie. Sinon, il utilise `linkedin-hook-generator` lorsqu'il est disponible, choisit une ouverture puis poursuit la rédaction. Il signale cet usage réel hors du post. Sans ce skill, il travaille l'accroche directement.

Si la matière conduit à un texte générique, il explique ce qui manque et propose des options adaptées : ajouter des détails réels, choisir une forme courte ou mettre le sujet de côté. L'auteur choisit le ton. Une version encore limitée reste un brouillon à enrichir. Il ne sauvegarde rien, ne déclenche pas d'analyse payante et ne programme ni ne publie rien.

## Analyser un post

`linkedin-post-analyzer` nécessite le MCP BarakaSocial. Sans les outils ou les accès requis, il explique ce qui manque puis s'arrête au lieu d'inventer un score officiel. Ses sources de test sont disponibles dans ce dépôt. Construis son ZIP avec le [guide de contribution](contributing.fr.md) pour l'essayer.

```text
Utilise linkedin-post-analyzer. Analyse ce brouillon sans rien enregistrer.
Garde le texte inchangé et identifie l'amélioration la plus utile :
[colle le post]
```

Par défaut, il lit `get_analysis_criteria`, évalue le texte choisi puis appelle `preview_post_analysis` sans conserver de diagnostic. Si l'utilisateur demande explicitement d'enregistrer le diagnostic, il utilise `submit_post_analysis`. Pour un post identifié dans BarakaSocial, il lit le texte actuel avec `get_post`. Une version retouchée dans le chat ne remplace pas silencieusement la version enregistrée.

Le modèle du client produit l'évaluation éditoriale. BarakaSocial calcule le score officiel à partir de cette évaluation. Ce n'est pas une seconde analyse IA indépendante ni une prédiction de portée. Une demande d'analyse ne réécrit pas le texte. La correction exige une demande correspondante. Le skill distingue la version notée d'une version corrigée ensuite.

Plusieurs relecteurs peuvent contribuer uniquement sur demande explicite et si le client le permet. Ils examinent le même texte avec des périmètres complémentaires puis l'agent principal rassemble leurs observations réelles en une évaluation. Il n'invente pas de relecteurs, ne moyenne pas des scores imaginaires et ne relance pas des boucles de notation. Le skill ne crée, ne modifie, ne programme et ne publie aucun post. Enregistrer un diagnostic n'enregistre pas un post.

## Améliorer un profil LinkedIn

[LinkedIn Profile Optimizer](../skills/linkedin-profile-optimizer/README.fr.md) travaille avec du texte ou des captures fournis sans compte obligatoire. Si tu demandes le profil enregistré dans BarakaSocial, il peut utiliser `get_linkedin_profile` et indique la date de récupération lorsqu'elle est disponible. Cette copie peut contenir des changements locaux. Ce n'est pas une lecture en direct de LinkedIn.

```text
Utilise linkedin-profile-optimizer. Relis mon titre et ma section Infos pour des fondateurs de startup qui cherchent un développeur freelance. Propose des changements sans inventer de résultats :
[colle les sections actuelles]
```

Tu reçois des constats appuyés sur la matière fournie et jusqu'à 3 priorités avec des textes à copier. Les sections manquantes et les images non consultées ne sont pas évaluées. Aucun score officiel de profil ni aucune modification du compte. Une demande sur une seule section reste ciblée.

<a id="personnaliser-les-3-skills"></a>
## Personnaliser les skills

La personnalisation est commune aux skills. Ce n'est pas un skill supplémentaire à installer. Chaque ZIP candidat contient `references/personalization.md` pour rester utilisable seul.

Tu peux demander :

```text
Personnalise ces skills LinkedIn pour moi. Réutilise ce que tu sais déjà.
Demande uniquement les préférences manquantes sur mon public, mon ton
et ce que je veux éviter. Garde ces choix dans cette conversation pour l'instant.
```

Le skill peut proposer une configuration facultative au premier usage ou répondre à une demande explicite de personnalisation. Aucun questionnaire n'est obligatoire pour traiter une demande déjà assez précise. Il utilise `AskUserQuestion` dans Claude Code ou `request_user_input` / `request_user_input_async` lorsque l'outil est disponible et autorisé dans le client actuel. Sinon, il pose les questions dans le chat. Il ne prend pas le silence pour une réponse et ne redemande pas les informations déjà fournies.

Tes instructions actuelles priment sur un profil enregistré. Une préférence pour un seul post ne devient pas automatiquement un réglage permanent. Les préférences communes orientent le ton, le public et la présentation. Elles ne remplacent pas les critères d'analyse de BarakaSocial et n'autorisent pas l'accès à un compte.

Pour conserver les préférences entre les sessions, demande leur enregistrement dans un emplacement privé de ton choix. Avec un accès aux fichiers, l'emplacement proposé est `~/.config/barakasocial/editorial-profile.json`, hors du dépôt et des dossiers des skills installés. Les 4 skills peuvent partager ce fichier. Ils n'écrivent pas de profil sans demande. Une mise à jour des instructions doit laisser ce fichier intact. Ne jamais committer de profil personnel ni l'inclure dans un ZIP distribué.

Sans accès à un stockage durable, les préférences restent dans la conversation. L'assistant peut fournir un profil à copier ou télécharger sans prétendre l'avoir enregistré ni promettre de le retrouver automatiquement. La configuration ne modifie pas le MCP et ne lit pas automatiquement les données personnelles du compte. Pour personnaliser après installation, demande explicitement d'installer **et de configurer** le skill ou configure-le au premier usage. Aucun questionnaire universel d'installation n'est supposé.

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
