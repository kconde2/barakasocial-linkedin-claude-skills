# LinkedIn Post Analyzer

[← Tous les skills](../../README.fr.md) · [English](README.md)

Comprends ce qui fonctionne dans un brouillon et l'amélioration la plus utile avec l'analyse BarakaSocial.

**Prérequis :** un compte BarakaSocial et son connecteur MCP accessibles dans ton client. Installer le skill ne connecte pas le compte.

[Installer](#install) · [Utiliser](#use) · [Personnaliser](#personalize)

<a id="install"></a>
## Installer ce skill

**Dans Claude Code ou Codex**, copie cette demande dans une conversation :

```text
Installe linkedin-post-analyzer dans mes skills personnels pour ce client.
Dépôt : https://github.com/kconde2/barakasocial-linkedin-claude-skills
Dossier : skills/linkedin-post-analyzer
Utilise la version du dépôt et copie SKILL.md avec tout le dossier references/.
Lis les instructions avant l'installation. Si ce skill existe déjà,
compare son origine et son contenu avant de le remplacer.
Conserve mes préférences personnelles et ma configuration MCP.
```

**Dans Claude avec import ZIP :** importe l'archive de ce skill dans la gestion des skills. Les ZIP `0.1.0-preview.7` ne sont pas encore publiés. Les sources sont disponibles ici ; le [guide de contribution](../../docs/contributing.fr.md) permet de construire l'archive.

[Voir les options d'installation et de mise à jour](../../docs/guide.fr.md)

<a id="use"></a>
## Utiliser le skill

Après installation, copie cet exemple en remplaçant la matière par la tienne :

```text
Utilise linkedin-post-analyzer.
Analyse ce brouillon sans rien enregistrer. Garde le texte inchangé et identifie l'amélioration la plus utile : [colle le post].
```

**Ce que tu obtiens :** Les points forts, le défaut principal, les retouches proposées et le score renvoyé par BarakaSocial. L'assistant évalue le texte puis BarakaSocial calcule le score. Cette note ne prédit pas la portée.

Par défaut, aucun diagnostic n'est enregistré et le texte reste inchangé. Demande explicitement une correction ou la sauvegarde du diagnostic si tu le souhaites. Sans MCP, le skill explique ce qui manque puis s'arrête. Il ne crée ni ne publie de post.

<a id="personalize"></a>
## Personnaliser

Tu peux préciser ton public, ton ton et ce que tu veux éviter. Le skill demande uniquement ce qui manque. Cette étape est facultative.

> Personnalise ce skill pour les dirigeants de petites agences. Ton direct, humour léger et aucune question finale automatique. Garde ces choix dans cette conversation.

[Conserver des préférences partagées](../../docs/guide.fr.md#personnaliser-les-3-skills)

[Lire les instructions du skill](SKILL.md) · [Retour au catalogue](../../README.fr.md)
