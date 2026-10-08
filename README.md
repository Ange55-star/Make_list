# TodoFlow

Application de gestion de tâches, notes et productivité développée avec Django et Python.

## Objectif

TodoFlow permet de :
- gérer des tâches avec titre, description et date d’échéance,
- marquer une tâche comme terminée,
- créer des notes rapides,
- consulter un tableau de bord de progression,
- personnaliser les préférences de sommeil, repos et réveil,
- utiliser un minuteur Pomodoro avec alerte sonore.

## Stack technique

- Python
- Django
- SQLite (base de données locale)
- HTML / CSS / JavaScript
- Tailwind CSS via CDN

## Structure du projet

```text
todo_list/
├── README.md
├── env/
├── Todo_list/
│   ├── manage.py
│   ├── Makelist/
│   │   ├── templates/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── form.py
│   │   ├── urls.py
│   │   └── tests.py
│   └── Todo_list/
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
└── db.sqlite3
```

## Prérequis

Assurez-vous d’avoir installé :
- Python 3.10+
- pip
- virtualenv (ou un environnement virtuel déjà créé)

## Installation

1. Ouvrez un terminal dans le dossier du projet.

2. Créez un environnement virtuel si nécessaire :

```bash
python -m venv env
```

3. Activez l’environnement virtuel :

Linux/macOS :

```bash
source env/bin/activate
```

4. Installez les dépendances :

```bash
pip install django
```

5. Vérifiez que Django est bien installé :

```bash
python -m django --version
```

## Base de données

Appliquez les migrations :

```bash
cd Todo_list
python manage.py migrate
```

## Lancer l’application

```bash
cd Todo_list
python manage.py runserver
```

Puis ouvrez dans le navigateur :

```text
http://127.0.0.1:8000/
```

## Comptes de test

Tu peux créer un compte depuis la page d’inscription ou utiliser le système de création utilisateur Django.

## Fonctionnalités principales

### Tâches
- ajouter une tâche,
- modifier une tâche,
- supprimer une tâche,
- marquer une tâche comme terminée,
- utiliser une date d’échéance.

### Notes
- enregistrer des idées rapidement,
- modifier ou supprimer une note,
- garder ses notes séparées des tâches.

### Dashboard
- statistiques générales,
- taux d’avancement,
- récapitulatif des tâches et notes,
- progression visuelle par période.

### Pomodoro
- compteur de 25 minutes,
- bouton démarrer / pause / reset,
- alerte sonore et visuelle à la fin.

## Tests

Pour lancer les tests du projet :

```bash
cd Todo_list
python manage.py test Makelist
```

## Développement futur possible

- système de notifications plus avancé,
- alarmes paramétrables par heure précise,
- catégories de tâches,
- priorité et tags,
- dashboard plus visuel avec graphiques JavaScript,
- authentification plus poussée avec vérification email.

## Auteur

Projet réalisé dans le cadre d’un apprentissage Django / Python.
