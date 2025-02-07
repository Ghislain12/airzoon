# Airzoon

## Description
La splash page de Airzoon est un projet de portail captif pour fournir une connexion Wi-Fi aux utilisateurs. Il inclut des fonctionnalités telles que la connexion avec un code, des alertes météorologiques et des formulaires de consentement.

## Structure du projet
- `splash.html` : Page d'accueil principale avec des informations et des formulaires pour les utilisateurs.
- `scraper.py` : Script Flask pour récupérer et afficher des alertes météorologiques.
- `scraper1.py` : Script pour scraper les données météorologiques depuis un site web.
- `new-splash.html` : Nouvelle version de la page d'accueil utilisant Tailwind CSS.
- `404.html` : Page d'erreur 404 personnalisée.
- `.gitignore` : Fichier pour ignorer les fichiers et dossiers spécifiques dans Git.

## Installation (Linux)
1. Cloner le dépôt :
    ```bash
    git clone https://github.com/votre-utilisateur/airzoon.git
    cd airzoon
    ```

2. Créer et activer un environnement virtuel :
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Installer les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## Installation (Windows)
1. Cloner le dépôt :
    ```bash
    git clone https://github.com/votre-utilisateur/airzoon.git
    cd airzoon
    ```

2. Créer et activer un environnement virtuel :
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Installer les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation
1. Lancer le serveur Flask :
    ```bash
    python scraper.py
    ```

2. Accéder à la page d'accueil en ouvrant `splash.html` dans un navigateur.

## Fonctionnalités
- **Connexion Wi-Fi** : Les utilisateurs peuvent se connecter en utilisant un code.
- **Alertes Météorologiques** : Affichage des alertes météorologiques récupérées depuis un site web.
- **Formulaire COVID-19** : Formulaire pour recueillir les informations des utilisateurs dans le cadre des mesures sanitaires.

## Contribuer
Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
