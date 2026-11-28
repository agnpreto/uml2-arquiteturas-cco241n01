"""Servico de Pedidos: orquestra o fluxo de compra chamando os demais servicos (SOA).
Fluxo: catalogo -> estoque (reserva) -> pagamento -> notificacao.
Se o pagamento falha, o estoque reservado e devolvido (compensacao)."""
import logging, os
import requests
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format="%(asctime)s [pedidos] %(message)s", datefmt="%H:%M:%S")
app = Flask(__name__)

CATALOGO = os.getenv("CATALOGO_URL", "http://localhost:5001")
ESTOQUE = os.getenv("ESTOQUE_URL", "http://localhost:5002")
PAGAMENTO = os.getenv("PAGAMENTO_URL", "http://localhost:5003")
NOTIFICACAO = os.getenv("NOTIFICACAO_URL", "http://localhost:5004")

PEDIDOS = {}
proximo_id = 1


def notificar(cliente, mensagem):
    try:
        requests.post(f"{NOTIFICACAO}/notificacoes", json={"cliente": cliente, "mensagem": mensagem}, timeout=5)
    except requests.RequestException:
        logging.info("notificacao indisponivel, seguindo sem ela")


@app.post("/pedidos")
def criar():
    global proximo_id
    d = request.get_json()
    pedido_id = proximo_id
    proximo_id += 1
    pedido = {"id": pedido_id, "cliente": d["cliente"], "produto_id": d["produto_id"],
              "quantidade": d["quantidade"], "status": "CRIADO"}
    PEDIDOS[pedido_id] = pedido
    logging.info("pedido %s recebido de %s", pedido_id, d["cliente"])

    r = requests.get(f"{CATALOGO}/produtos/{d['produto_id']}", timeout=5)
    if r.status_code != 200:
        pedido["status"] = "CANCELADO"
        pedido["motivo"] = "produto inexistente"
        logging.info("pedido %s cancelado: produto inexistente", pedido_id)
        return jsonify(pedido), 404
    produto = r.json()
    pedido["valor"] = round(produto["preco"] * d["quantidade"], 2)

    r = requests.post(f"{ESTOQUE}/estoque/reservar",
                      json={"produto_id": d["produto_id"], "quantidade": d["quantidade"]}, timeout=5)
    if r.status_code != 200:
        pedido["status"] = "CANCELADO"
        pedido["motivo"] = "estoque insuficiente"
        logging.info("pedido %s cancelado: estoque insuficiente", pedido_id)
        notificar(d["cliente"], f"Pedido {pedido_id} cancelado: estoque insuficiente.")
        return jsonify(pedido), 409

    r = requests.post(f"{PAGAMENTO}/pagamentos",
                      json={"pedido_id": pedido_id, "valor": pedido["valor"], "cartao": d["cartao"]}, timeout=5)
    if r.status_code != 200:
        requests.post(f"{ESTOQUE}/estoque/liberar",
                      json={"produto_id": d["produto_id"], "quantidade": d["quantidade"]}, timeout=5)
        pedido["status"] = "CANCELADO"
        pedido["motivo"] = "pagamento recusado"
        logging.info("pedido %s cancelado: pagamento recusado, estoque devolvido", pedido_id)
        notificar(d["cliente"], f"Pedido {pedido_id} cancelado: pagamento recusado.")
        return jsonify(pedido), 402

    pedido["status"] = "PAGO"
    pedido["transacao"] = r.json()["transacao"]
    logging.info("pedido %s PAGO (R$ %.2f)", pedido_id, pedido["valor"])
    notificar(d["cliente"], f"Pedido {pedido_id} confirmado! Total R$ {pedido['valor']:.2f}.")
    return jsonify(pedido), 201


@app.get("/pedidos/<int:pedido_id>")
def obter(pedido_id):
    p = PEDIDOS.get(pedido_id)
    return (jsonify(p), 200) if p else (jsonify({"erro": "pedido nao encontrado"}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
