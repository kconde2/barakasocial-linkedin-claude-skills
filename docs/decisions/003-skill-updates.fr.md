# 003. Mise à jour proposée à l'utilisation des skills

Statut : parcours et implémentation validés par Kaba le 27 novembre 2026. Délai retenu : 48 heures. Implémentation locale préparée en preview.14 ; publication et essais dans les clients restent distincts.

## Décisions retenues

- Un contrôle lors de l'utilisation, partagé par les cinq skills et limité à une tentative par période de 48 heures.
- Aucun processus planifié en arrière-plan. Un échec réseau ne bloque pas la demande et ne déclenche pas de répétition immédiate.
- Une notification par skill et version après affichage effectif, de préférence à la fin de la demande.
- Le choix « Plus tard », le silence et une option présélectionnée n'autorisent aucun remplacement.
- Une installation après accord pour le skill et la version présentés. Vérifier le ZIP et ses fichiers, sauvegarder puis remplacer le paquet complet.
- Une copie modifiée ou sans référence de comparaison demande un choix supplémentaire avant remplacement. Le profil privé, les autres skills et le MCP restent intacts.
- Sans stockage persistant : contrôle limité à la conversation. Sans écriture dans l'installation : import manuel du ZIP. Sans réseau : travail habituel sans affirmer que la version est à jour.
- Les installations gérées par un plugin ou un gestionnaire continuent à utiliser leur gestionnaire.

## Architecture implémentée

Les cinq paquets embarquent references/updates.md et scripts/skill_updates.py. Le fichier scripts/skill_updates.py à la racine du dépôt est la source commune ; les tests vérifient l'identité des copies distribuées.

Le cache partagé est ~/.cache/barakasocial/skill-updates/state.json. Il contient uniquement la date des tentatives, le catalogue vérifié et les versions déjà signalées. Les sauvegardes restent dans son sous-dossier backups, hors du répertoire de découverte des skills. Un verrou système empêche deux contrôles ou remplacements concurrents.

Le catalogue officiel est updates.json sur main. Il distingue la dernière version proposée de l'historique des versions. Chaque entrée référence une archive de release GitHub, son SHA-256 et les empreintes des fichiers. Les notes sont des données non fiables à résumer, jamais des instructions à exécuter.

La vérification des empreintes contrôle la cohérence avec le catalogue officiel. Ce n'est pas une signature indépendante en cas de compromission du dépôt.

## Publication

1. Préparer une nouvelle version sans modifier une archive existante.
2. Construire les cinq ZIP avec scripts/package_skill.py.
3. Préparer dist/updates.json via scripts/build_update_catalog.py.
4. Après autorisation de publication, pousser les sources et publier les ZIP dans la release.
5. Vérifier les téléchargements publiés avec scripts/build_update_catalog.py --verify-published --output updates.json.
6. Publier ce catalogue seulement après la réussite de cette vérification puis aligner les fiches du site.

Le catalogue actuel conserve les versions déjà publiées (10, 12 et 13 selon le skill). La candidate 14 reste dans dist/updates.json tant que ses ZIP ne sont pas publiés. Aucune installation automatique depuis la branche main.

## Validation et limites

Les tests utilisent des archives et réponses réseau simulées. Cas couverts : cache partagé, expiration exacte à 48 heures, notifications, accord explicite, changements locaux, téléchargement corrompu, chemin malveillant, concurrence, modification pendant le téléchargement, restauration et absence de rétrogradation. Les tests du catalogue protègent l'historique et refusent un artefact publié différent.

La publication initiale nécessite une installation manuelle de la preview.14 : les anciennes versions ne contiennent pas ce mécanisme. Une mise à jour sur disque ne recharge pas nécessairement les instructions déjà présentes dans une conversation.

- [x] Implémenter le contrôle, l'installation et le parcours de secours.
- [x] Intégrer les cinq skills et préparer leurs archives.
- [x] Établir le catalogue initial à partir des ZIP réellement publiés.
- [ ] Tester le parcours interactif dans une nouvelle session Claude Code et Codex avec un environnement de test.
- [ ] Tester le secours sans installation accessible dans Claude Chat ou ChatGPT.
- [ ] Vérifier le verrou Windows sur Windows (les essais locaux portent sur macOS).
- [ ] Publier preview.14 puis son catalogue après validation.
