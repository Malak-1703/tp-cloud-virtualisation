# TP3 : Docker & Conteneurisation
## Objectif
Conteneuriser une application Flask.
## Fichiers
- `app.py` : Code source de l'application DevOps Monitor.
- `Dockerfile` : Recette de construction (optimisée, non-root).
## Lancement
docker build -t devops-monitor:1.0 .
docker run -d -p 8080:5000 -v monitor-logs:/app/logs devops-monitor:1.0