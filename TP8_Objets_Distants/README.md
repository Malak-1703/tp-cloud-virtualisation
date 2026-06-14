# TP8 : Invocation d'Objets Distants (Pyro5)
## Objectif
Manipuler le modèle RMI (Remote Method Invocation) en Python.
## Réalisations
- Création d'un `DocumentService` exposé via Pyro5 (Daemon, Name Server, Proxy).
- Mise en place d'une politique d'exposition stricte (décorateur `@expose`).
- Durcissement du service : validation des paramètres et masquage des exceptions (erreurs sûres).