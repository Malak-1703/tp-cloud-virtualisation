# TP8 : Sécurité des Objets Distants (Pyro5)

## 1. Politique d'Exposition (Whitelisting)
Seules les méthodes métier nécessaires sont décorées avec `@Pyro5.api.expose`. 
Les méthodes d'administration (ex: `_internal_reset_cache`) ou d'accès DB (`_get_db_connection`) ne le sont PAS. Cela réduit la surface d'attaque.

## 2. Validation et Erreurs Sûres
- **Validation** : Le `doc_id` est vérifié par Regex (`^[a-zA-Z0-9_]+$`) pour empêcher le Path Traversal (`../../etc/passwd`).
- **Erreurs** : Le serveur lève des exceptions avec des messages génériques ("Identifiant invalide"). Le traceback complet (fichiers, lignes, variables) reste dans les logs internes du serveur et n'est jamais renvoyé au client (Prevention of Information Disclosure).

## 3. Sérialisation
Pyro5 utilise par défaut le sérialiseur **Serpent**, qui est sûr et n'exécute pas de code. L'utilisation de `pickle` est strictement interdite dans ce TP pour éviter les risques d'exécution de code à distance (RCE).