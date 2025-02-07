# Projet Splash Page Wi-Fi

## Introduction

Ce projet a pour but de servir des pages d'accueil Wi-Fi (splash pages) dynamiques avec des encarts publicitaires personnalisés. Les pages sont générées à l'aide d'un serveur Express.js et utilisent un moteur de templates pour dynamiser le contenu.

## Structure du Projet

- **proxy.js** : Fichier principal du serveur Node.js utilisant Express pour gérer les requêtes et servir les pages.
- **splash_original.html** : Modèle HTML de la splash page avec des encarts publicitaires intégrés.
- **views/splash.ejs** : (Non utilisé dans la version actuelle, mais pourrait être utilisé pour dynamiser les pages avec EJS).

## Fonctionnement des Fichiers

### proxy.js

- **Description** : Ce fichier configure un serveur Express qui sert des pages HTML et fournit une API pour récupérer des publicités.
- **Fonctionnalités** :
  - **API des Publicités** : `/ads` renvoie une liste de publicités filtrées selon les préférences utilisateur.
  - **Serveur de Pages** : Sert la page `splash_original.html` à la racine (`/`).
- **Exécution** : Le serveur écoute sur le port 5000.

### splash_original.html

- **Description** : Page HTML statique qui sert de modèle pour la splash page Wi-Fi.
- **Fonctionnalités** :
  - **Encarts Publicitaires** : Intègre des publicités dynamiques récupérées via l'API.
  - **Formulaires** : Contient des formulaires pour la connexion et la collecte d'informations.
- **Personnalisation** : Les publicités sont insérées dynamiquement à l'aide de JavaScript.


## Instructions pour Lancer le Projet

1. **Prérequis** :
   - Node.js et npm doivent être installés sur votre machine.

2. **Installation des Dépendances** :
   - Exécutez la commande suivante pour installer les dépendances nécessaires :
     ```bash
     npm install express cors
     ```

3. **Démarrage du Serveur** :
   - Lancez le serveur Express en exécutant la commande suivante dans le répertoire du projet :
     ```bash
     node proxy.js
     ```
   - Le serveur sera actif sur `http://0.0.0.0:5000`.

4. **Accès à la Splash Page** :
   - Ouvrez un navigateur et accédez à `http://localhost:5000` pour voir la splash page avec les publicités dynamiques.

## Personnalisation et Extension

- **Ajout de Publicités** : Vous pouvez ajouter de nouvelles publicités dans le tableau `ads` dans `proxy.js`.
- **Personnalisation des Pages** : Modifiez les fichiers HTML pour ajuster le style et le contenu selon vos besoins.
- **Utilisation d'un Moteur de Templates** : Pour dynamiser davantage les pages, envisagez d'utiliser EJS ou un autre moteur de templates.

## Remarques

- Assurez-vous que le serveur est en cours d'exécution et que l'API des publicités est accessible pour que les encarts s'affichent correctement.
