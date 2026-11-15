# LinkedIn Post Writer

[← Tous les skills](../../README.fr.md) · [English](README.md)

Transforme tes notes ou ton brouillon en post LinkedIn complet en gardant tes faits et ta voix.

**Prérequis :** un sujet, des notes ou un brouillon. Aucun compte BarakaSocial nécessaire.

[Installer](#install) · [Utiliser](#use) · [Exemples à copier](#examples) · [Personnaliser](#personalize)

<a id="install"></a>
## Installer ce skill

**Dans Claude Code ou Codex**, copie cette demande dans une conversation :

```text
Installe linkedin-post-writer dans mes skills personnels pour ce client.
Dépôt : https://github.com/kconde2/barakasocial-linkedin-claude-skills
Dossier : skills/linkedin-post-writer
Utilise la version du dépôt et copie SKILL.md avec tout le dossier references/.
Lis les instructions avant l'installation. Si ce skill existe déjà,
compare son origine et son contenu avant de le remplacer.
Conserve mes préférences personnelles et ma configuration MCP.
```

**Dans Claude avec import ZIP :** télécharge le [ZIP preview.10](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.10/linkedin-post-writer.zip) puis importe l'archive complète dans la gestion des skills. Elle contient `SKILL.md` et les 2 références communes. [Options d'installation](../../docs/guide.fr.md).

[Voir les options d'installation et de mise à jour](../../docs/guide.fr.md)

<a id="use"></a>
## Utiliser le skill

Après installation, copie cet exemple en remplaçant la matière par la tienne :

```text
Utilise linkedin-post-writer.
Rédige un seul post : un client valide ma maquette puis demande 2 écrans supplémentaires. Je propose un devis séparé. Garde un ton direct et n'invente pas le résultat.
```

**Ce que tu obtiens :** Un post ou des variantes cohérentes selon ta demande. Une accroche choisie est conservée. La matière essentielle manquante est signalée plutôt qu'inventée.

Le skill répond dans la langue demandée. Il n'enregistre ni ne publie de post.

<a id="examples"></a>
## Demandes prêtes à copier

Ces demandes sont à coller dans la conversation après installation. Remplace les éléments entre crochets par tes informations. Ce ne sont pas des commandes de terminal.

### Rédiger un seul post

```text
Utilise linkedin-post-writer.
Rédige un seul post pour [public] à partir de ces notes :
[notes]
Ton : [ton]. N'invente aucun fait. Si la matière est trop pauvre, explique ce qui manque.
```

### Comparer plusieurs versions

```text
Utilise linkedin-post-writer.
Propose 3 versions de ce post avec des angles distincts. Préserve les faits et ma voix. Utilise linkedin-hook-generator s'il est disponible puis choisis une accroche adaptée à chaque version :
[brouillon]
```

### Développer une accroche validée

```text
Utilise linkedin-post-writer.
Garde cette accroche : [accroche validée]. Écris un seul post à partir de cette matière :
[faits et notes]
Si la matière ne permet pas de tenir la promesse de l'accroche, signale-le.
```

### Rédiger un sujet choisi

```text
Utilise linkedin-post-writer. Rédige un seul post à partir du sujet que j'ai choisi avec linkedin-topic-finder.
Garde le public, l'intention, la réaction souhaitée et les faits du brief. Ne recommence pas la recherche de sujets.
```

Le writer reste utilisable sans Topic Finder. Un objectif de discussion, d'enregistrement ou de vente oriente le contenu sans imposer une question finale ou une promotion.

<a id="personalize"></a>
## Personnaliser

Tu peux préciser ton public, ton ton et ce que tu veux éviter. Le skill demande uniquement ce qui manque. Cette étape est facultative.

> Personnalise ce skill pour les dirigeants de petites agences. Ton direct, humour léger et aucune question finale automatique. Garde ces choix dans cette conversation.

[Conserver des préférences partagées](../../docs/guide.fr.md#personnaliser-les-skills)

[Lire les instructions du skill](SKILL.md) · [Retour au catalogue](../../README.fr.md)
