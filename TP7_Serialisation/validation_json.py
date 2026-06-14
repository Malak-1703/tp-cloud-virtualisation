"""
TP7 - Sérialisation JSON sécurisée et Validation stricte
Règle d'or : Ne jamais faire confiance aux données entrantes.
"""
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ALLOWED_CLASSIFICATIONS = {"public", "internal", "confidential"}

def validate_and_deserialize_document(raw_json: str) -> dict:
    """Désérialise et valide un payload JSON avec approche Fail-Closed."""
    
    # 1. Limite de taille (Protection DoS / Bombe JSON)
    if len(raw_json) > 1024 * 1024:  # 1 Mo max
        raise ValueError("Payload trop volumineux")

    # 2. Parsing JSON (Format inerte, pas d'exécution de code)
    try:
        data = json.loads(raw_json)
    except json.JSONDecodeError as e:
        logger.warning(f"JSON invalide: {e}")
        raise ValueError("Format JSON invalide")

    if not isinstance(data, dict):
        raise ValueError("La racine du JSON doit être un objet")

    # 3. Validation des champs obligatoires et types
    errors = []
    
    if "id" not in data or not isinstance(data["id"], int):
        errors.append("Champ 'id' manquant ou non entier")
        
    if "title" not in data or not isinstance(data["title"], str):
        errors.append("Champ 'title' manquant ou non chaîne")
    elif len(data["title"]) > 200:
        errors.append("Champ 'title' trop long")

    # 4. Validation des valeurs (Allowlist)
    classification = data.get("classification", "internal")
    if classification not in ALLOWED_CLASSIFICATIONS:
        errors.append(f"Classification '{classification}' non autorisée")

    # 5. Fail Closed : Rejet total si la moindre erreur
    if errors:
        logger.warning(f"Échec validation: {errors}")
        raise ValueError("Données non conformes au contrat")

    # 6. Nettoyage (Whitelisting des champs retournés)
    return {
        "id": data["id"],
        "title": data["title"].strip(),
        "classification": classification
    }

# --- Tests unitaires ---
if __name__ == "__main__":
    # Cas valide
    valide = '{"id": 42, "title": "Rapport", "classification": "confidential"}'
    print("✅ Valide:", validate_and_deserialize_document(valide))

    # Cas invalide (Injection de classification)
    invalide = '{"id": 43, "title": "Fake", "classification": "top_secret"}'
    try:
        validate_and_deserialize_document(invalide)
    except ValueError as e:
        print("❌ Rejeté (Attendu):", e)