# TP5 : Architecture du Système de Gestion Documentaire Distribué (SGDD)

## 1. Architecture Logique
Le système est décomposé en microservices indépendants communiquant via API REST (HTTP/JSON) et files de messages asynchrones.

```text
[Client Web/Mobile] 
       │ (HTTPS)
       ▼
┌──────────────────┐
│   API Gateway    │ (Rate Limiting, AuthN, Routing)
──────┬───────────┘
       │ (mTLS / JWT)
       ├──► [Auth Service] ──► [Users DB (PostgreSQL)]
       │
       ├──► [Document Service] ──► [Docs DB (MongoDB)] ──► [Object Storage (MinIO)]
       │
       ──► [Search Service] ◄── [Message Queue (RabbitMQ)] ── [Document Service]
                                  │
                                  ──► [Search Index (Elasticsearch)]