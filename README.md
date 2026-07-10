# LITRevu

Application web Django permettant de demander et publier des critiques de livres/articles entre utilisateurs abonnés les uns aux autres.

## Fonctionnalités

- Inscription, connexion (formulaire intégré à la page d'accueil) et déconnexion
- Création d'un ticket (demande de critique sur un livre ou article, avec image optionnelle)
- Publication d'une critique en réponse à un ticket existant
- Création d'un ticket et de sa critique en une seule action
- Modification et suppression de ses propres tickets et critiques (page « Posts »)
- Suivi / arrêt du suivi d'autres utilisateurs
- Flux personnalisé : tickets et critiques de l'utilisateur et de ses abonnements, triés par date

## Stack technique

- Python 3.14, Django 6
- Base de données SQLite (par défaut)
- Tailwind CSS 4 via [django-tailwind](https://github.com/timonweb/django-tailwind) (compilation autonome, sans Node requis)

## Installation

```bash
# 1. Cloner le dépôt puis se placer dedans
git clone <url-du-repo>
cd Dev-Django

# 2. Créer et activer un environnement virtuel
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS / Linux

# 3. Installer les dépendances Python
pip install -r requirements.txt

# 4. Appliquer les migrations
python manage.py migrate

# 5. (optionnel) créer un compte administrateur
python manage.py createsuperuser

# 6. Compiler le CSS Tailwind
python manage.py tailwind build

# 7. Lancer le serveur de développement
python manage.py runserver
```

L'application est ensuite accessible sur http://127.0.0.1:8000.

Pendant le développement, `python manage.py tailwind start` recompile le CSS automatiquement à chaque changement des templates.

## Structure du projet

| App | Rôle |
|---|---|
| `LITRevu_project/` | Configuration Django (settings, URLs racine) |
| `authentication/` | Inscription et déconnexion |
| `reviews/` | Modèles `Ticket`, `Review`, `UserFollows` ; flux, posts, création/édition/suppression, abonnements |
| `home/` | Page d'accueil : formulaire de connexion et appel à l'inscription pour les visiteurs, redirection vers le flux pour les utilisateurs connectés |
| `theme/` | Configuration Tailwind CSS, logo et template de base (`base.html`) |
| `litrevu/` | Ancienne app conservée uniquement pour l'historique des migrations (modèles déplacés vers `reviews`) |
