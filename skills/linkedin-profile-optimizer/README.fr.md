# LinkedIn Profile Optimizer

[← Tous les skills](../../README.fr.md) · [English](README.md)

Rends ton profil LinkedIn plus clair pour les personnes que tu veux toucher. Obtiens des constats ciblés et des textes à copier.

**Prérequis :** le texte du profil ou des captures. Aucun compte BarakaSocial nécessaire. Une lecture MCP autorisée peut fournir le profil enregistré.

[Installer](#install) · [Utiliser](#use) · [Personnaliser](#personalize)

<a id="install"></a>
## Installer ce skill

**Dans Claude Code ou Codex**, copie cette demande dans une conversation :

```text
Installe linkedin-profile-optimizer dans mes skills personnels pour ce client.
Dépôt : https://github.com/kconde2/barakasocial-linkedin-claude-skills
Dossier : skills/linkedin-profile-optimizer
Utilise la version du dépôt et copie SKILL.md avec tout le dossier references/.
Lis les instructions avant l'installation. Si ce skill existe déjà,
compare son origine et son contenu avant de le remplacer.
Conserve mes préférences personnelles et ma configuration MCP.
```

**Dans Claude avec import ZIP :** importe l'archive de ce skill dans la gestion des skills. Les ZIP `0.1.0-preview.8` ne sont pas encore publiés. Les sources sont disponibles ici ; le [guide de contribution](../../docs/contributing.fr.md) permet de construire l'archive.

Une carte du client qui ne prend en charge que `SKILL.md` ne peut pas installer ce paquet complet. Utilise le ZIP ou un client avec accès aux fichiers. Le dossier `references/` ne doit pas être omis.

[Voir les options d'installation et de mise à jour](../../docs/guide.fr.md)

<a id="use"></a>
## Utiliser le skill

Après installation, copie cet exemple en remplaçant la matière par la tienne :

```text
Utilise linkedin-profile-optimizer.
Relis mon titre et ma section Infos pour des fondateurs de startup qui cherchent un développeur freelance. Garde mes affirmations factuelles et signale les preuves manquantes :
[colle les sections actuelles]
```

**Ce que tu obtiens :** Un tableau de constats appuyés sur ta matière et jusqu'à 3 priorités avec des textes prêts à copier. Tu peux aussi demander une seule section.

Avec une lecture BarakaSocial autorisée, le skill indique la date de récupération du profil lorsqu'elle est disponible. Il ne suppose pas que cette copie correspond au profil LinkedIn actuel. Les visuels non consultés et les sections manquantes ne sont pas évalués. Aucun score chiffré, enregistrement automatique ou changement sur LinkedIn.

## Des questions adaptées à ton objectif

Le skill réutilise ce que tu as déjà précisé. Si ton objectif manque, il demande ce que ton profil doit t'aider à obtenir : clients ou missions, emploi, réputation professionnelle, candidats, partenaires ou opportunités ou simplement une présentation plus claire sans objectif commercial immédiat.

Pour les clients, il peut distinguer régie, forfait, conseil et accompagnement. Ce sont des façons de travailler plutôt que des objectifs distincts. Tu peux combiner plusieurs objectifs ou répondre librement. Aucun questionnaire fixe à remplir.

<a id="personalize"></a>
## Personnaliser

Tu peux préciser ton public, ton ton et ce que tu veux éviter. Le skill demande uniquement ce qui manque. Cette étape est facultative.

> Personnalise ce skill pour les dirigeants de petites agences. Ton direct, humour léger et aucune question finale automatique. Garde ces choix dans cette conversation.

[Conserver des préférences partagées](../../docs/guide.fr.md#personnaliser-les-skills)

[Lire les instructions du skill](SKILL.md) · [Retour au catalogue](../../README.fr.md)
