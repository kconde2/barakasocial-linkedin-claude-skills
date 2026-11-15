# LinkedIn Topic Finder

[← Tous les skills](../../README.fr.md) · [English](README.md)

Trouve des sujets précis et des angles pour ton public à partir d'une intention, d'un thème, de notes ou de contenus existants. Prépare un post ou plusieurs sujets complémentaires pour une campagne sans inventer de vécu.

**Prérequis :** ton contexte ou ta matière, complétés par quelques questions utiles si nécessaire. Aucun compte BarakaSocial obligatoire.

[Installer](#install) · [Utiliser](#use) · [Exemples à copier](#examples) · [Personnaliser](#personalize)

<a id="install"></a>
## Installer ce skill

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

**Import ZIP :** preview.10 ne dispose pas encore de release avec les archives. Construis le ZIP depuis ces sources avec le [guide de contribution](../../docs/contributing.fr.md). Importe le paquet complet avec sa référence. [Options d'installation](../../docs/guide.fr.md).

<a id="use"></a>
## Utiliser le skill

```text
Utilise linkedin-topic-finder. Je parle aux dirigeants de petites agences.
Un client valide une maquette puis demande 2 écrans supplémentaires. Je propose un devis séparé. Je n'ai pas encore sa réponse.
Propose 3 sujets pour que les lecteurs se reconnaissent ou discutent de cet arbitrage. Ne rédige pas encore les posts.
```

Tu obtiens un tableau court avec des IDs stables, les sujets et angles, l'intérêt pour le lecteur et la matière disponible ou manquante. Le but et la réaction recherchée apparaissent quand ils aident à choisir. La question traitée et l'apport étayé guident le brief retenu sans surcharger chaque ligne. Un problème n'est pas obligatoire. Le skill recommande une piste sans prédire sa performance. Tu peux demander un autre nombre ou format.

Que tu apportes un sujet ou choisisses un ID proposé, l'assistant reprend ce que tu as déjà dit. Si nécessaire, il te demande ton avis, une observation, une expérience ou ce que tu veux explorer. Choisir un sujet ne signifie pas approuver une conclusion proposée. Pas de nouvel entretien si la matière suffit. Pas d'opinion tranchée, de récit personnel ou de vente imposés.

Choisis un sujet puis demande sa rédaction. Si `linkedin-post-writer` est disponible, il reprend les mêmes décisions sans recommencer les questions. Sinon, l'assistant peut rédiger à partir du brief sur demande. Choisir un sujet seul ne déclenche pas l'écriture.

Le skill peut aussi t'aider à définir le monde de tes lecteurs et proposer de conserver ce contexte dans ton profil privé partagé. Il réutilise ce qu'il sait déjà et distingue les observations des hypothèses. [Voir la sauvegarde et le profil partagé](../../docs/guide.fr.md#construire-et-conserver-le-contexte-partagé).

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
