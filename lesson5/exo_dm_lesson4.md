## DM lesson4

Dans ce dataset: https://raw.githubusercontent.com/fspot/INFMDI-721/master/lesson5/products.csv, chaque ligne correspond à un produit alimentaire mis en vente par un utilisateur.

Objectif: cleaner le dataset.

- On aimerait avoir une colonne de prix unifiés en euros. Problème: la currency n'est pas indiquée pour tous les produits: il va falloir essayer de "deviner" les currency manquantes, en se basant sur l'adresse IP de l'utilisateur.
- La colonne "infos" liste des ingrédients présents dans le produit. On préfèrerait avoir une colonne de type bool par ingrédient, indiquant si le produit contient ou non cet ingrédient.

Voic une liste d'APIs qui peut vous être utile : https://github.com/public-apis/public-apis (mais vous pouvez en utiliser d'autres si vous le voulez).
