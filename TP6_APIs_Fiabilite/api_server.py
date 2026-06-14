import json
import uuid
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

# Base de données simulée en mémoire
DOCUMENTS_DB = {}
VALID_TOKEN = "secret-token-tp6-2026"

class DocumentAPIHandler(BaseHTTPRequestHandler):
    
    def _send_json(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def _check_auth(self):
        auth = self.headers.get("Authorization", "")
        if auth != f"Bearer {VALID_TOKEN}":
            self._send_json(401, {"error": "unauthorized", "message": "Token invalide"})
            return False
        return True

    def do_GET(self):
        # Endpoint santé (pas d'auth requise)
        if self.path == "/health":
            self._send_json(200, {
                "status": "ok",
                "timestamp": datetime.utcnow().isoformat(),
                "request_id": self.headers.get("X-Request-Id", "unknown")
            })
            return
        
        # Liste des documents (Auth requise)
        if self.path == "/api/v1/documents" and self._check_auth():
            self._send_json(200, {"data": list(DOCUMENTS_DB.values()), "total": len(DOCUMENTS_DB)})
            return

        self._send_json(404, {"error": "not_found"})

    def do_POST(self):
        if self.path != "/api/v1/documents":
            self._send_json(404, {"error": "not_found"})
            return

        if not self._check_auth():
            return

        # Lecture et parsing JSON
        content_length = int(self.headers.get("Content-Length", 0))
        if content_length > 1048576:  # Limite 1Mo (Protection DoS)
            self._send_json(413, {"error": "payload_too_large"})
            return

        try:
            body = json.loads(self.rfile.read(content_length))
        except json.JSONDecodeError:
            self._send_json(400, {"error": "invalid_json"})
            return

        # Validation stricte (Fail Closed)
        title = body.get("title", "").strip()
        if not title or len(title) > 200:
            self._send_json(400, {"error": "validation_error", "message": "Titre invalide"})
            return

        # Création (Non idempotent sans clé)
        doc_id = str(uuid.uuid4())
        DOCUMENTS_DB[doc_id] = {
            "id": doc_id,
            "title": title,
            "created_at": datetime.utcnow().isoformat()
        }
        self._send_json(201, DOCUMENTS_DB[doc_id])

    def log_message(self, format, *args):
        pass # Silence les logs par défaut pour la clarté

if __name__ == "__main__":
    print("🚀 Serveur API démarré sur http://127.0.0.1:8080")
    HTTPServer(("127.0.0.1", 8080), DocumentAPIHandler).serve_forever()