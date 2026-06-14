# Projet Fil Rouge : API DevOps Monitor Conteneurisée
## Objectif
Démontrer la capacité à packager une application distribuée (API REST) dans un conteneur Docker sécurisé, en respectant les bonnes pratiques de cybersécurité et d'orchestration.

## Architecture
- **Backend** : API Flask (Python) exposant un endpoint de santé (`/health`) et une page d'accueil.
- **Conteneurisation** : Image basée sur `python:3.11-slim` pour réduire la surface d'attaque.
- **Sécurité** : Exécution en tant qu'utilisateur non-root (`appuser`) à l'intérieur du conteneur.

## Lancement
### Construire l'image
docker build -t projet-fil-rouge:1.0 .

### Lancer le conteneur
docker run -d -p 8080:5000 -e APP_MESSAGE="Projet ENSA 2026" projet-fil-rouge:1.0

### Tester
curl http://localhost:8080/health