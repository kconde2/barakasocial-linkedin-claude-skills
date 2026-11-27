# Skills visuels LinkedIn

Statut : validé et implémenté pour publication locale puis GitHub.

Deux skills : linkedin-image-finder orchestre et linkedin-meme-finder cherche sur Imgflip avec les outils web de l'agent. Aucun appel API Imgflip. Le type puis le nombre sont demandés seulement si absents ; cinq propositions par défaut. Chaque candidat montre son image et le texte proposé. Le choix autorise le montage avec les outils disponibles, jamais une publication.

bs-creation-image reste intact. Photo Finder, génération autonome et ProgrammerHumor sont hors périmètre.

## Validation

Parcours essayé dans Codex : recherche de cinq candidats, choix du cinquième et montage. Kaba a validé le résultat. Le chargement d'images pour inspection a été bloqué par Imgflip pendant la recherche ; le test ne prouve donc pas l'inspection de tous les candidats. Ni le fonctionnement dans Claude ni la fidélité pixel à pixel du montage génératif ne sont validés.

## Distribution

Preview.15 contient les deux nouveaux ZIP. Les cinq anciens restent en preview.14. Leurs helpers refusent les noms inconnus : conserver updates.json inchangé. La famille visuelle utilise image-updates.json avec son propre cache et son helper, sans modifier le catalogue historique. Vérifier les octets téléchargés avant activation du nouveau catalogue.
