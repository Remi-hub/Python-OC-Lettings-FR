## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


### variable d'environnement local

Pour exécuter le site en local nous avons utilisé la librairie dotenv, pour l'utiliser il faut 
créer un fichier .env a la racine du projet et lui passer les variables suivants :
- SECRET_KEY=votre secret key django
- SENTRY_DSN=votre dsn de sentry


## Déploiement

### Configuration requise

Avoir un compte sur les applications suivantes est nécessaire :

- Github
- CircleCI
- Sentry
- DockerHub
- Heroku


### Utilisation de CircleCI

Nous effectuons le déploiement automatique ainsi que le linting et le test de l'application grâce 
à CircleCI. A chaque push de notre projet sur Github, nous effectuons le workflow suivant :

Tout d'abord le workflow suivant :
- checkout (récuperer le code du projet)
- installation des lib listé dans le requirements.txt grâce à pip
- creation d'un environnement pour exécuter le conteneur docker
- nous lançons nos tests grâce à Pytest
- nous effectuons le linting du site grâce à Black

Puis nous pouvons passer aux étapes de déploiement si tous le workflow précédent est validé :
- creation du container avec l'image du projet depuis dockerhub
- déploiement de l'image sur le site heroku

### comment deployer l'application 

#### 1 - Dockerhub
- créer un compte et  se connecter à Docker
- créer un dépôt et lui donner un nom, dans mon cas ocr_p13

#### 2 - Heroku
- créer un compte et se connecter à Heroku
- créer une nouvelle application, dans mon cas oc-lettings-rk

#### 3 - Sentry
- créer un compte et se connecter à Sentry
- créer un nouveau projet sous la plateforme django
- nommer le projet, dans mon cas ocr_p13

#### 4 - CircleCI
- Se connecter sur circleCI grâce à Github
- Choisir notre projet et cliquer sur Set up Project
- accepter la pull request et checkout sur la master, nous avons désormais notre fichier de conf
- dans les option de notre projet, ajouter les variables d'environnement suivant:

`HEROKU_API_KEY` -> entrez en valeur la clef api obtenu sur le site heroku.
`HEROKU_APP_NAME` -> entrez le nom de l'application créer sur heroku.
`HEROKU_TOKEN` -> obtenu grâce à heroku cli, et tapez heroku auth:token.
`SECRET_KEY` -> votre clef secrete django.
`SENTRY DSN` -> votre dsn obtenu lors de la config de sentry.
`docker_hub_password` -> votre mdp docker hub.
`docker_hub_username` -> votre username docker hub.


#### Exécuter l'image docker hub en local 
`docker run --env-file .env -p 8001:8000 -it remi1990/ocr_p13:"tag"`
Le tag correspond au dernier tag de commit que vous pouvez voir sur docker hub
Pensez à créer le fichier .env qui contient vos variables d'environnement