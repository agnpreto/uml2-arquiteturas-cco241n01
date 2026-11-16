"""Servico de Notificacao: simula o envio de e-mail ao cliente."""
import logging, os
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format="%(asctime)s [notificacao] %(message)s", datefmt="%H:%M:%S")
app = Flask(__name__)


@app.post("/notificacoes")
def notificar():
    d = request.get_json()
    logging.info("e-mail para %s: %s", d["cliente"], d["mensagem"])
    return jsonify({"enviado": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5004)))
