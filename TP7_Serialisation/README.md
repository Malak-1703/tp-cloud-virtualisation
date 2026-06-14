# TP7 : Sérialisation et Sécurité des Données
## Objectif
Maîtriser les formats d'échange et contrer les vulnérabilités de désérialisation.
## Réalisations
- Comparaison JSON (schema-less) vs Protobuf (schema-based).
- Implémentation d'une validation stricte des entrées (fail-closed).
- Analyse critique de `pickle` et `yaml.load()` : interdiction formelle sur les entrées non fiables (risque RCE).