# Snacks à la Réunion
Ce projet a pour but de recenser les différents snacks à la Réunion. L'objectif est de fournir une carte interactive et une liste des snacks, ainsi que des informations sur chaque snack, telles que l'adresse, les horaires d'ouverture et les spécialités proposées.

## Données
Les données ont été collectées à partir de différents sites web et auprès des propriétaires des snacks. Elles ont été stockées dans une base de données MongoDB.

## Visualisation des données
Les données ont été visualisées à l'aide de Dash, un framework Python pour la création d'applications web interactives. La carte interactive a été créée à l'aide de Mapbox, une plateforme de cartographie en ligne.

## Comment utiliser l'application
L'application peut être exécutée localement en utilisant les commandes suivantes :


```shell
$ git clone https://github.com/username/snacks-a-la-reunion.git
$ cd snacks-a-la-reunion
$ pip install -r requirements.txt
$ python app.py
```

Une fois l'application en cours d'exécution, elle peut être consultée en ouvrant un navigateur web et en accédant à l'URL suivante :


```
http://127.0.0.1:8050/
```

L'utilisateur peut rechercher des snacks sur la carte en utilisant la barre de recherche ou en parcourant la liste des snacks à droite de la carte. Lorsque l'utilisateur clique sur un snack, des informations supplémentaires sur le snack s'affichent dans une fenêtre contextuelle.

## Contribution
Les contributions sont les bienvenues ! Si vous souhaitez ajouter un nouveau snack ou améliorer l'application, veuillez créer une demande d'extraction (pull request).

## Auteurs
Ce projet a été réalisé par @ajrunislnd.
