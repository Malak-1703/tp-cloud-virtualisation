"""
TP8 - Client consommateur du DocumentService Pyro5
Gestion des erreurs distantes de manière sûre.
"""
import Pyro5.api

TOKEN = "pyro5-secure-token-2026"

def main():
    try:
        ns = Pyro5.api.locate_ns()
        uri = ns.lookup("cyberlab.document_service")
        
        with Pyro5.api.Proxy(uri) as service:
            # Appel 1 : Liste
            docs = service.list_documents(TOKEN)
            print(f"📄 Documents disponibles : {docs}")
            
            # Appel 2 : Récupération valide
            content = service.get_content("doc_001", TOKEN)
            print(f" Contenu doc_001 : {content}")
            
            # Appel 3 : Test de sécurité (Injection / Format invalide)
            print("\n🛡️ Test de sécurité (Injection '../etc/passwd') :")
            try:
                service.get_content("../etc/passwd", TOKEN)
            except ValueError as e:
                print(f"   ✅ Bloqué par le serveur : {e}")
                
    except Pyro5.errors.NamingError:
        print(" Name Server introuvable. Lancez 'python -m Pyro5.nameserver'")
    except Exception as e:
        print(f"❌ Erreur réseau ou service : {type(e).__name__}")

if __name__ == "__main__":
    main()