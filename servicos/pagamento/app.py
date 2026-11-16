"""Servico de Pagamento: simula um gateway de pagamento.
Regra da simulacao: cartoes terminados em 0000 sao recusados."""
import logging, os, uuid
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format="%(asctime)s [pagamento] %(message)s", datefmt="%H:%M:%S")
app = Flask(__name__)


@app.post("/pagamentos")
def pagar():
    d = request.get_json()
    cartao = str(d["cartao"])
    if cartao.endswith("0000"):
        logging.info("pedido %s: pagamento RECUSADO (valor %.2f)", d["pedido_id"], d["valor"])
        return jsonify({"status": "recusado"}), 402
    transacao = uuid.uuid4().hex[:8]
    logging.info("pedido %s: pagamento APROVADO (valor %.2f, transacao %s)", d["pedido_id"], d["valor"], transacao)
    return jsonify({"status": "aprovado", "transacao": transacao})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5003)))
