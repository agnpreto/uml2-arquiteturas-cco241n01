"""Servico de Estoque: consulta, reserva e libera unidades."""
import logging, os
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format="%(asctime)s [estoque] %(message)s", datefmt="%H:%M:%S")
app = Flask(__name__)

ESTOQUE = {1: 10, 2: 5, 3: 2}


@app.get("/estoque/<int:produto_id>")
def consultar(produto_id):
    if produto_id not in ESTOQUE:
        return jsonify({"erro": "produto nao encontrado"}), 404
    return jsonify({"produto_id": produto_id, "disponivel": ESTOQUE[produto_id]})


@app.post("/estoque/reservar")
def reservar():
    d = request.get_json()
    pid, qtd = d["produto_id"], d["quantidade"]
    if ESTOQUE.get(pid, 0) < qtd:
        logging.info("reserva negada: produto %s, pedido de %s, disponivel %s", pid, qtd, ESTOQUE.get(pid, 0))
        return jsonify({"erro": "estoque insuficiente"}), 409
    ESTOQUE[pid] -= qtd
    logging.info("reservadas %s unidade(s) do produto %s (restam %s)", qtd, pid, ESTOQUE[pid])
    return jsonify({"reservado": True, "restante": ESTOQUE[pid]})


@app.post("/estoque/liberar")
def liberar():
    d = request.get_json()
    pid, qtd = d["produto_id"], d["quantidade"]
    ESTOQUE[pid] = ESTOQUE.get(pid, 0) + qtd
    logging.info("liberadas %s unidade(s) do produto %s (restam %s)", qtd, pid, ESTOQUE[pid])
    return jsonify({"liberado": True, "restante": ESTOQUE[pid]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5002)))
