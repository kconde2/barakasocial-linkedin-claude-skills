# Outils MCP BarakaSocial

[Accueil](../README.fr.md) · [English](mcp-tools.md)

La recherche de sujets, les accroches et la rédaction fonctionnent sans outil obligatoire. Ces skills peuvent utiliser les lectures MCP autorisées quand l'utilisateur demande le contexte du compte. L'analyse nécessite le MCP BarakaSocial connecté. La disponibilité dépend des outils exposés par le connecteur dans le client utilisé.

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
| `linkedin-topic-finder` | Sujets et angles à partir de la matière disponible. Lectures du compte uniquement sur demande. Aucun enregistrement de sujets ou de campagne. |
| `linkedin-hook-generator` | Accroches à partir du texte fourni. Lectures MCP facultatives pour enrichir le contexte. |
| `linkedin-post-writer` | Post ou variantes à partir de la matière fournie. Lectures MCP facultatives et recours au skill d'accroches s'il est disponible. |
| `linkedin-post-analyzer` | MCP obligatoire. Aperçu par défaut. Diagnostic enregistré uniquement sur demande explicite. |
| `linkedin-profile-optimizer` | Titre, description et bannière avec validation par élément. Lectures du profil et de la voix facultatives et autorisées. Outil d'image du client si disponible. Aucun score ni changement du compte. |

Pour l'analyse, le modèle client produit l'évaluation selon `get_analysis_criteria`. BarakaSocial applique ensuite le calcul officiel avec `preview_post_analysis` ou `submit_post_analysis`. Ces outils ne déclenchent pas le modèle d'analyse interne du serveur. `submit_post_analysis` conserve le diagnostic avec la provenance `mcp-client`. `get_post_analysis` lit un diagnostic existant sans lancer d'analyse. Ce parcours ne consomme aucun crédit.

Les outils `save_post`, `update_post`, `schedule_post`, `prepare_post_image`, `confirm_post_image` et `cancel_post_image` existent également. Ils restent hors du périmètre des 5 skills. Leur présence dans le connecteur n'autorise pas une sauvegarde, une programmation ou une modification automatique. Ce catalogue ne rend pas chaque outil obligatoire et n'autorise aucune action hors du périmètre demandé.

L'optimiseur de profil utilise `get_linkedin_profile` pour une lecture demandée du compte et éventuellement `get_config_profile` pour les préférences de voix autorisées. Les données peuvent dater ou avoir été modifiées localement. `update_linkedin_profile` existe mais reste hors de ce skill : il change uniquement le titre et la description locaux, jamais LinkedIn. Les outils d'analyse de posts ne constituent pas un service de notation du profil.
