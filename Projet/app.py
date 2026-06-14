from flask import Flask, jsonify
import os, socket, datetime

app = Flask(__name__)
MESSAGE = os.environ.get("APP_MESSAGE", "Bonjour depuis le Projet Fil Rouge !")

@app.route("/")
def home():
    return f"<h1>{MESSAGE}</h1><p>Conteneur: {socket.gethostname()}</p>"

@app.route("/health")
def health():
    return jsonify({"status": "ok", "hostname": socket.gethostname()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)