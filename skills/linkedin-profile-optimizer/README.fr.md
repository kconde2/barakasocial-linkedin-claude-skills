# LinkedIn Profile Optimizer

[← Tous les skills](../../README.fr.md) · [English](README.md)

Améliore ton titre, ta description ou ta bannière, séparément ou ensemble. Valide chaque élément puis applique toi-même les changements sur LinkedIn.

**Prérequis :** le texte du profil ou des captures. Aucun compte BarakaSocial nécessaire. Une lecture MCP autorisée peut fournir le profil enregistré.

[Installer](#install) · [Utiliser](#use) · [Exemples à copier](#examples) · [Personnaliser](#personalize)

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

**Dans Claude avec import ZIP :** importe l'archive de ce skill dans la gestion des skills. Les ZIP `0.1.0-preview.9` ne sont pas encore publiés. Les sources sont disponibles ici ; le [guide de contribution](../../docs/contributing.fr.md) permet de construire l'archive.

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

**Ce que tu obtiens :** Les éléments choisis avec tes faits et ton objectif, une validation par élément puis un tableau récapitulatif. Le titre et la description sont livrés dans des blocs de texte séparés à copier. La bannière est fournie comme image si un outil de génération est disponible, sinon comme brief clairement identifié.

Avec une lecture BarakaSocial autorisée, le skill indique la date de récupération du profil lorsqu'elle est disponible. Il ne suppose pas que cette copie correspond au profil LinkedIn actuel. Les visuels non consultés et les sections manquantes ne sont pas évalués. Aucun score chiffré, enregistrement automatique ou changement sur LinkedIn.

## Des questions adaptées à ton objectif

Le skill réutilise ce que tu as déjà précisé. Si ton objectif manque, il demande ce que ton profil doit t'aider à obtenir : clients ou missions, emploi, réputation professionnelle, candidats, partenaires ou opportunités ou simplement une présentation plus claire sans objectif commercial immédiat.

Pour les clients, il peut distinguer régie, forfait, conseil et accompagnement. Ce sont des façons de travailler plutôt que des objectifs distincts. Tu peux combiner plusieurs objectifs ou répondre librement. Aucun questionnaire fixe à remplir.

<a id="examples"></a>
## Demandes prêtes à copier

Ces demandes sont à coller dans la conversation après installation. Remplace les éléments entre crochets par tes informations. Ce ne sont pas des commandes de terminal.

### Utiliser le profil enregistré

```text
Utilise linkedin-profile-optimizer.
Lis mon profil enregistré dans BarakaSocial et indique sa date de récupération. Mon objectif : [objectif]. Propose des améliorations de mon titre et de ma description sans rien enregistrer.
```

### Améliorer uniquement le titre

```text
Utilise linkedin-profile-optimizer.
Améliore uniquement mon titre pour trouver des missions en régie comme [rôle]. Voici mon titre actuel : [titre]. Mes compétences et expériences réelles : [faits]. Ne réécris pas les autres sections.
```

### Améliorer la description sans MCP

```text
Utilise linkedin-profile-optimizer.
Travaille uniquement avec le texte ci-dessous. Améliore ma description pour [objectif] auprès de [public]. Garde mon titre : [titre]. Description actuelle :
[description]
Utilise ces expériences comme preuves sans les réécrire : [faits].
```

### Relire une bannière fournie

```text
Utilise linkedin-profile-optimizer.
Examine la bannière jointe et propose des améliorations de son message et de sa lisibilité. Mon titre : [titre]. Mon objectif : [objectif]. Si tu ne peux pas voir l'image, dis-le. Ne modifie pas les autres éléments.
```

La lecture du profil enregistré nécessite le MCP. Les autres exemples utilisent la matière fournie. Le skill n'enregistre rien même avec le MCP. La génération et la retouche de bannière dépendent des outils d'image disponibles dans ton client. Sans outil, il fournit un brief et ne prétend pas avoir créé l'image.

### Retoucher une bannière

```text
Utilise linkedin-profile-optimizer.
Retouche uniquement la bannière jointe. Garde [éléments à conserver] et ajoute [éléments souhaités]. Mon objectif : [objectif]. Génère une proposition avec un outil d'image disponible puis laisse-moi la valider. Ne change pas mon titre ni ma description.
```

### Préparer les 3 éléments ensemble

```text
Utilise linkedin-profile-optimizer.
Améliore mon titre, ma description et ma bannière pour [objectif] auprès de [public]. Voici mon profil et mes éléments visuels : [matière]. Réutilise les informations connues et demande ce qui manque. Fais-moi valider chaque élément puis fournis un tableau récapitulatif, les textes à copier et la bannière si elle a été générée. Je ferai les changements sur LinkedIn moi-même.
```

### Ajuster un élément sans perdre les validations

```text
Utilise linkedin-profile-optimizer.
Je valide le titre et la description que tu viens de proposer. Garde-les tels quels. Pour la bannière, change seulement [retouche souhaitée] puis montre-moi la nouvelle version.
```

<a id="personalize"></a>
## Personnaliser

Tu peux préciser ton public, ton ton et ce que tu veux éviter. Le skill demande uniquement ce qui manque. Cette étape est facultative.

> Personnalise ce skill pour les dirigeants de petites agences. Ton direct, humour léger et aucune question finale automatique. Garde ces choix dans cette conversation.

[Conserver des préférences partagées](../../docs/guide.fr.md#personnaliser-les-skills)

[Lire les instructions du skill](SKILL.md) · [Retour au catalogue](../../README.fr.md)
