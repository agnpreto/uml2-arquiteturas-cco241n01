"""Servico de Catalogo: lista os produtos vendidos no marketplace."""
import logging, os
from flask import Flask, jsonify

logging.basicConfig(level=logging.INFO, format="%(asctime)s [catalogo] %(message)s", datefmt="%H:%M:%S")
app = Flask(__name__)

PRODUTOS = {
    1: {"id": 1, "nome": "Teclado mecanico", "preco": 250.00, "vendedor": "TechStore"},
    2: {"id": 2, "nome": "Mouse gamer", "preco": 120.00, "vendedor": "TechStore"},
    3: {"id": 3, "nome": "Monitor 24 pol", "preco": 899.90, "vendedor": "VideoMais"},
}


@app.get("/produtos")
def listar():
    return jsonify(list(PRODUTOS.values()))


@app.get("/produtos/<int:produto_id>")
def obter(produto_id):
    p = PRODUTOS.get(produto_id)
    if not p:
        logging.info("produto %s nao encontrado", produto_id)
        return jsonify({"erro": "produto nao encontrado"}), 404
    logging.info("consulta produto %s (%s)", produto_id, p["nome"])
    return jsonify(p)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5001)))
