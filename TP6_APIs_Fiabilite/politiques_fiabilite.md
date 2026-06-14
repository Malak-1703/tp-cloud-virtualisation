# TP6 : Politiques de Fiabilité et Idempotence

## 1. Matrice des Timeouts et Retries
| Service | Timeout | Max Retries | Backoff | Idempotence |
|---|---|---|---|---|
| Auth (Login) | 5s | 1 | 1s + Jitter | Non (Génération token) |
| Documents (GET) | 10s | 2 | 1s + Jitter | Oui (Lecture) |
| Documents (POST) | 15s | 0 (Pas de retry auto) | - | Non (Nécessite Idempotency-Key) |
| Search (Query) | 8s | 2 | 1s + Jitter | Oui (Lecture) |

## 2. Analyse des Scénarios de Panne
- **S1 (Latence élevée)** : Risque d'effet cascade. Solution : Circuit Breaker côté client + Timeout strict (10s). Fallback : retourner un cache périmé.
- **S2 (Erreurs 503 intermittentes)** : Problème transitoire (rolling update). Solution : Retry avec Backoff Exponentiel + Jitter pour éviter le Retry Storm.
- **S3 (Double clic utilisateur)** : Risque de doublon. Solution : Le client génère un `Idempotency-Key` (UUID) envoyé dans le header. Le serveur stocke la clé et retourne la réponse précédente sans re-traiter.