# Outils MCP BarakaSocial

[Accueil](../README.fr.md) · [English](mcp-tools.md)

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
