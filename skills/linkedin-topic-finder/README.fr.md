# LinkedIn Topic Finder

[← Tous les skills](../../README.fr.md) · [English](README.md)

Trouve des sujets précis et des angles pour ton public à partir d'une intention, d'un thème, de notes ou de contenus existants. Prépare un post ou plusieurs sujets complémentaires pour une campagne sans inventer de vécu.

**Prérequis :** ton contexte ou ta matière, complétés par quelques questions utiles si nécessaire. Aucun compte BarakaSocial obligatoire.

[Installer](#install) · [Mettre à jour](#update) · [Utiliser](#use) · [Exemples à copier](#examples) · [Personnaliser](#personalize)

<a id="install"></a>
## Installer ce skill

**Version distribuée : preview.12.** Elle contient le parcours thèmes → idée ou objectif du post → traitement → sujets. Importe le ZIP versionné ci-dessous dans Claude Desktop, depuis Customize > Skills. Le mode Code n'est pas nécessaire. Les installations existantes ne sont pas mises à jour automatiquement.


Dans Claude Code ou Codex, copie cette demande :

```text
Installe linkedin-topic-finder dans mes skills personnels pour ce client.
Dépôt : https://github.com/kconde2/barakasocial-linkedin-claude-skills
Dossier : skills/linkedin-topic-finder
Utilise la version du dépôt et copie SKILL.md avec tout le dossier references/.
Lis les instructions avant l'installation. Si ce skill existe déjà,
compare son origine et son contenu avant de le remplacer.
Conserve mes préférences personnelles et ma configuration MCP.
```

**Dans Claude avec import ZIP :** télécharge le [ZIP preview.12](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.12/linkedin-topic-finder.zip) puis importe l'archive complète dans la gestion des skills. Elle contient `SKILL.md` et les 2 références communes. [Options d'installation](../../docs/guide.fr.md).

<a id="update"></a>
## Mettre à jour ce skill

Si tu as installé le skill localement, copie cette demande dans Claude Code ou Codex.

```text
Mets à jour mon linkedin-topic-finder depuis la branche main.
Dépôt : https://github.com/kconde2/barakasocial-linkedin-claude-skills
Dossier source : skills/linkedin-topic-finder
Identifie la copie installée. Si elle contient des modifications personnelles
ou vient d'une autre source, montre-moi les différences et demande mon accord
avant de la remplacer. Si les fichiers sont déjà identiques, dis-le-moi.
Sinon, mets à jour le même dossier avec SKILL.md et tout references/.
Conserve mon profil éditorial, mes préférences et ma configuration MCP.
Indique la version installée.
```

Si ton skill est synchronisé depuis Claude.ai, mets à jour l'original dans Claude avec le ZIP indiqué plus haut. [Comment Claude synchronise les skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

<a id="use"></a>
## Utiliser le skill

Lance `/linkedin-topic-finder` seul pour choisir ton point de départ. Tu peux explorer sans idée précise, partir d'un thème ou de notes ou choisir un objectif pour un post ou une campagne. Le skill pose les questions utiles puis te laisse ajuster les critères, les sources, les mots à utiliser souvent et le format. Pour un tableau, tu peux choisir la disposition ou laisser le skill décider. Tu peux aussi donner une demande prête à exécuter.

```text
Utilise linkedin-topic-finder. Je parle aux dirigeants de petites agences.
Un client valide une maquette puis demande 2 écrans supplémentaires. Je propose un devis séparé. Je n'ai pas encore sa réponse.
Propose 3 sujets pour que les lecteurs se reconnaissent ou discutent de cet arbitrage. Ne rédige pas encore les posts.
```

Tu obtiens un tableau court avec des IDs stables, les sujets et angles, la raison de les lire maintenant et la matière disponible ou manquante. Une situation qui revient ou une curiosité durable peut donner envie de lire. Le but et la réaction recherchée apparaissent quand ils aident à choisir. La question traitée et l'apport étayé guident le brief retenu sans surcharger chaque ligne. Le skill recommande une piste sans prédire sa performance. Tu peux demander un autre nombre ou format.

Que tu apportes un sujet ou choisisses un ID proposé, l'assistant reprend ce que tu as déjà dit. Si nécessaire, il te demande ton avis, une observation, une expérience ou ce que tu veux explorer. Choisir un sujet ne signifie pas approuver une conclusion proposée. Pas de nouvel entretien si la matière suffit. Pas d'opinion tranchée, de récit personnel ou de vente imposés.

Choisis un sujet puis demande sa rédaction. Si `linkedin-post-writer` est disponible, il reprend les mêmes décisions sans recommencer les questions. Sinon, l'assistant peut rédiger à partir du brief sur demande. Choisir un sujet seul ne déclenche pas l'écriture.

Le skill peut aussi t'aider à définir le monde de tes lecteurs et proposer de conserver ce contexte dans ton profil privé partagé. Il réutilise ce qu'il sait déjà et distingue les observations des hypothèses. [Voir la sauvegarde et le profil partagé](../../docs/guide.fr.md#construire-et-conserver-le-contexte-partagé).

## Partir de tes thèmes sans remplir une stratégie

Les thèmes et le public sont tes repères. L'objectif peut changer pour chaque post. Le skill peut t'aider à définir tes grandes idées, mais ne l'impose pas avant les sujets. Il réutilise le contexte et propose des pistes si tu ne sais pas encore préciser ton public. Les questions utilisent les contrôles natifs uniquement s'ils sont disponibles, sinon le chat.

```text
Utilise linkedin-topic-finder. Mon thème est [thème] et mon public est [public].
Voici mon idée : [idée ou observation]. Pour ce post, je veux [objectif].
Aide-moi à la préciser et propose un traitement adapté à ma matière.
Ne me demande pas de définir une stratégie globale ou des messages centraux.
```

```text
Je n'ai pas d'idée. Dans le thème [thème], aide-moi à trouver des sujets
pour [public] afin de [objectif de ce post]. Voici ce que je peux apporter :
[matière]. Si une précision est indispensable, pose une question.
```

Pour revenir sur une grande idée, demande un nouvel exemple, une objection ou une démonstration. Le skill vérifie l'apport différent dans les contenus accessibles. Il ne promet pas une nouveauté absolue ni une performance.

<a id="examples"></a>
## Demandes prêtes à copier

Remplace les éléments entre crochets. Ce sont des demandes dans le chat, pas des commandes de terminal.

### Je n'ai aucune idée

```text
Utilise linkedin-topic-finder. Je travaille dans [domaine] et je veux toucher [public] pour [objectif].
Aide-moi à trouver de la matière dans mon passé, mes observations, les questions reçues ou mes ressources. Demande seulement ce qui manque avant de proposer des sujets. N'invente pas mon vécu.
```

### Passer d'un thème à des sujets précis

```text
Utilise linkedin-topic-finder. Thème : [thème]. Lecteur : [lecteur].
Voici ma matière : [notes ou ressources]. Je veux un contenu utile à enregistrer et à envoyer à un collègue.
Propose 3 angles concrets. Signale les preuves manquantes.
```

### Trouver des sujets qui divisent vraiment

```text
Utilise linkedin-topic-finder. Trouve 3 sujets qui divisent vraiment, nouveaux par rapport à notre conversation et aux contenus fournis. Garde mes lecteurs et mon intention.
Pour chacun, montre le désaccord réel entre 2 positions défendables et ce qui les étaye. Ne me prête aucune expérience ou opinion que je n'ai pas validée. Propose les sujets sans rédiger les posts.
```

Après avoir choisi les sujets :

```text
Montre-moi les posts pour [IDs choisis]. Reprends ma matière et mon point de vue. S'il manque ma position sur un désaccord, demande-la avant de rédiger.
```

### Voir directement des brouillons sur ces désaccords

```text
Utilise linkedin-topic-finder. Trouve 3 sujets nouveaux qui divisent vraiment les freelances et les dirigeants d'agences. Garde mon intention.
Écarte les sujets déjà abordés dans cette conversation ou dans mes contenus fournis. Pour chacun, montre le désaccord concret puis rédige un brouillon d'opinion à discuter.
N'invente aucun vécu et ne présente pas ces positions comme les miennes.
```

### Préparer une campagne de vente

```text
Utilise linkedin-topic-finder. Prépare les sujets de 3 posts de vente pour [offre] auprès de [public].
Voici ce que l'offre apporte réellement : [contenu et limites]. Preuves disponibles : [matière].
Propose des angles complémentaires sans témoignage inventé ni fausse urgence. Pas de rédaction ou de programmation pour l'instant.
```

### Changer la réaction puis rédiger

```text
Garde ma matière et mon public. Pour ce post seulement, privilégie une discussion utile plutôt que l'enregistrement.
Choisis le sujet le mieux étayé puis rédige un post avec linkedin-post-writer s'il est disponible. N'enregistre pas cette préférence.
```

### Chercher dans mon compte

```text
Utilise linkedin-topic-finder. Lis mes posts BarakaSocial avec les outils MCP disponibles pour trouver 3 nouveaux angles pour [public et objectif].
Lis les posts retenus avant de proposer de les réutiliser. Signale les accès ou statistiques manquants. N'enregistre et ne publie rien.
```

L'accès au compte est facultatif et dépend des outils connectés. Les sources externes utilisées sont attribuées. Les exemples et hypothèses restent distincts des faits vérifiés. Aucun message automatique au public, analyse payante, enregistrement d'idée ou publication.

<a id="personalize"></a>
## Personnaliser

Réutilise le même profil privé d'auteur que les autres skills. Précise seulement ce qui aide : public, objectif, voix, expertise, piliers éventuels, offres ou réactions souhaitées. Une campagne reste temporaire sauf demande explicite de conserver ses réglages.

```text
Personnalise ces skills pour [auteur et public]. Ma direction est [direction].
Je souhaite que les lecteurs [réaction]. Garde ces choix dans cette conversation pour l'instant.
```

[Préférences partagées](../../docs/guide.fr.md#personnaliser-les-skills) · [Instructions du skill](SKILL.md)
