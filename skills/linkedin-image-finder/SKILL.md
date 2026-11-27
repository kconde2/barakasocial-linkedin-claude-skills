---
name: linkedin-image-finder
description: Proposer des pistes visuelles pour un post LinkedIn en orientant vers un spécialiste disponible. Utiliser pour trouver une image adaptée au message ; le premier spécialiste fourni est linkedin-meme-finder pour les mèmes.
metadata:
  version: "0.1.0-preview.15"
  author: BarakaSocial
---

# Trouver un visuel pour un post

Reprendre le post actif et la demande sans imposer de questionnaire. Si le texte manque, demander le post ou le lire avec le connecteur disponible quand l'utilisateur a autorisé cette lecture. Pour « mon dernier post publié », filtrer les publications et trier par date de publication décroissante. Ne pas choisir le dernier brouillon modifié.

Identifier brièvement le message, le lecteur et ce que le visuel doit faire ressentir ou comprendre : contraste, reconnaissance, humour, émotion ou explication. Distinguer une hypothèse sur le lecteur d'une information donnée. Préserver le texte et la liberté créative de l'auteur.

## Choisir le type et le nombre

Si le type n'est pas déjà précisé, demander quel visuel l'utilisateur veut avec la seule option disponible : « Mème ». Ne pas inventer d'autres options pour remplir une interface. Utiliser un outil de question natif s'il est disponible et accepte ce choix ; sinon poser la question dans le chat. Attendre la réponse avant la recherche.

Demander ensuite « Combien de propositions veux-tu ? Cinq par défaut. » Accepter un entier positif personnalisé, notamment dix. Utiliser un outil de question natif si disponible, sinon le chat. Ne pas redemander un type ou un nombre déjà précisé. Transmettre le nombre au spécialiste et ne pas répéter cette question dans celui-ci.

## Orienter

Pour une recherche de mèmes, charger le skill installé `linkedin-meme-finder` et suivre ses instructions en lui transmettant le texte, le contraste utile, le ton et les contraintes de l'utilisateur. Le fichier voisin `../linkedin-meme-finder/SKILL.md` convient lorsque les deux dossiers sont installés ensemble. Sinon utiliser le catalogue de skills de l'environnement. Si le spécialiste manque, le signaler sans prétendre l'avoir exécuté.

Pour une demande générale, proposer la piste mème si elle sert le post. C'est le seul spécialiste fourni dans cette première version. Si une photo documentaire ou une autre approche est nécessaire, expliquer la limite au lieu de forcer un mème. Ne pas inventer un spécialiste photo ou génération installé.

Le routage consiste à charger des instructions : il ne nécessite pas de sous-agent ni une API d'invocation de skills.

## Restituer

Présenter le nombre choisi de candidats distincts, cinq par défaut, avec aperçu inspecté, source, raison du choix et éventuelle légende proposée. Recommander le plus pertinent. S'il existe moins de candidats vérifiés pertinents que demandé, présenter ceux disponibles et expliquer la limite sans compléter avec de faux résultats.

Afficher les aperçus directement dans la conversation, pas seulement une liste de liens. Laisser l'utilisateur choisir un candidat et son texte ou demander d'autres pistes. Le choix d'un candidat dans ce parcours autorise la préparation locale du mème avec le texte proposé, sauf si l'utilisateur demande seulement une comparaison ou réserve le montage pour plus tard. Suivre alors l'étape de montage du spécialiste. Ne pas préparer tous les candidats avant le choix.

Ne pas réécrire le post ni associer ou publier un média sur LinkedIn ou BarakaSocial.

## Mises à jour

Suivre [le contrôle partagé](references/updates.md) à l'invocation quand les outils le permettent, sans bloquer le travail.
