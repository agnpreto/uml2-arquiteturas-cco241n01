"""Cliente de teste: executa o fluxo principal de compra contra o servico de pedidos.
Uso: python fluxo.py   (o sistema precisa estar no ar em localhost:5000)"""
import json
import urllib.error
import urllib.request

BASE = "http://localhost:5000"


def comprar(titulo, corpo):
    req = urllib.request.Request(f"{BASE}/pedidos", data=json.dumps(corpo).encode(),
                                 headers={"Content-Type": "application/json"})
    print(f"\n=== {titulo} ===")
    try:
        with urllib.request.urlopen(req) as r:
            print(r.status, json.dumps(json.load(r), ensure_ascii=False))
    except urllib.error.HTTPError as e:
        print(e.code, json.dumps(json.load(e), ensure_ascii=False))


comprar("1. Compra com sucesso", {"cliente": "pedro@exemplo.com", "produto_id": 1, "quantidade": 2, "cartao": "4111111111111111"})
comprar("2. Pagamento recusado (estoque e devolvido)", {"cliente": "eduardo@exemplo.com", "produto_id": 2, "quantidade": 1, "cartao": "4111111111110000"})
comprar("3. Estoque insuficiente", {"cliente": "pedro@exemplo.com", "produto_id": 3, "quantidade": 5, "cartao": "4111111111111111"})
