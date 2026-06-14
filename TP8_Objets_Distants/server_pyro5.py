import Pyro5.api
import logging
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# Base de données simulée
_DOCS = {
    "doc_001": "Rapport financier 2025 (Confidentiel)",
    "doc_002": "Guide de sécurité informatique",
}

@Pyro5.api.expose
class DocumentService:
    """Service de gestion documentaire exposé à distance."""
    
    # Token partagé pour l'authentification basique (En prod : JWT/mTLS)
    _SECRET_TOKEN = "pyro5-secure-token-2026"

    def _check_auth(self, token: str):
        """Méthode INTERNE (non exposée) pour vérifier l'authentification."""
        if token != self._SECRET_TOKEN:
            logger.warning(f"Tentative d'accès avec token invalide")
            raise PermissionError("Accès refusé : Token invalide")

    def list_documents(self, token: str) -> list:
        """Liste les identifiants des documents disponibles."""
        self._check_auth(token)
        logger.info("Appel list_documents() réussi")
        return list(_DOCS.keys())

    def get_content(self, doc_id: str, token: str) -> str:
        """Récupère le contenu d'un document avec validation stricte."""
        self._check_auth(token)
        
        # Validation du format (Anti Path Traversal / Injection)
        if not isinstance(doc_id, str) or not re.match(r'^[a-zA-Z0-9_]{1,32}$', doc_id):
            logger.warning(f"Format doc_id suspect reçu: {doc_id!r}")
            raise ValueError("Identifiant de document invalide") # Message générique

        if doc_id not in _DOCS:
            logger.info(f"Document non trouvé: {doc_id}")
            raise KeyError("Document introuvable")

        return _DOCS[doc_id]

    # Méthode interne NON exposée (Pas de @Pyro5.api.expose)
    def _internal_reset_cache(self):
        pass 

def main():
    with Pyro5.api.Daemon() as daemon:
        ns = Pyro5.api.locate_ns()
        uri = daemon.register(DocumentService)
        ns.register("cyberlab.document_service", uri)
        print(f"✅ DocumentService prêt. URI: {uri}")
        daemon.requestLoop()

if __name__ == "__main__":
    main()