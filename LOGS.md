
# Logs do fluxo principal

O fluxo executa três cenários: compra aprovada, pagamento recusado e estoque insuficiente.

## Fluxo

```text
=== 1. Compra com sucesso ===
201 {"cliente": "pedro@exemplo.com", "id": 1, "produto_id": 1, "quantidade": 2, "status": "PAGO", "transacao": "1096a886", "valor": 500.0}

=== 2. Pagamento recusado (estoque e devolvido) ===
402 {"cliente": "eduardo@exemplo.com", "id": 2, "motivo": "pagamento recusado", "produto_id": 2, "quantidade": 1, "status": "CANCELADO", "valor": 120.0}

=== 3. Estoque insuficiente ===
409 {"cliente": "pedro@exemplo.com", "id": 3, "motivo": "estoque insuficiente", "produto_id": 3, "quantidade": 5, "status": "CANCELADO", "valor": 4499.5}
```

## Logs dos serviços Docker

Saída completa do comando `docker compose logs --no-color` (também disponível em [docker-logs.txt](docker-logs.txt)):

```text
catalogo-1     |  * Serving Flask app 'app'
notificacao-1  |  * Serving Flask app 'app'
notificacao-1  |  * Debug mode: off
notificacao-1  | 03:08:58 [notificacao] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
notificacao-1  |  * Running on all addresses (0.0.0.0)
notificacao-1  |  * Running on http://127.0.0.1:5004
notificacao-1  |  * Running on http://172.18.0.5:5004
notificacao-1  | 03:08:58 [notificacao] Press CTRL+C to quit
notificacao-1  |  * Serving Flask app 'app'
notificacao-1  |  * Debug mode: off
notificacao-1  | 03:13:31 [notificacao] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
notificacao-1  |  * Running on all addresses (0.0.0.0)
notificacao-1  |  * Running on http://127.0.0.1:5004
pedidos-1      |  * Serving Flask app 'app'
notificacao-1  |  * Running on http://172.18.0.4:5004
notificacao-1  | 03:13:31 [notificacao] Press CTRL+C to quit
notificacao-1  | 03:14:26 [notificacao] e-mail para pedro@exemplo.com: Pedido 1 confirmado! Total R$ 500.00.
estoque-1      |  * Serving Flask app 'app'
estoque-1      |  * Debug mode: off
estoque-1      | 03:08:58 [estoque] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
estoque-1      |  * Running on all addresses (0.0.0.0)
notificacao-1  | 03:14:26 [notificacao] 172.18.0.6 - - [16/Nov/2026 03:14:26] "POST /notificacoes HTTP/1.1" 200 -
notificacao-1  | 03:14:26 [notificacao] e-mail para eduardo@exemplo.com: Pedido 2 cancelado: pagamento recusado.
notificacao-1  | 03:14:26 [notificacao] 172.18.0.6 - - [16/Nov/2026 03:14:26] "POST /notificacoes HTTP/1.1" 200 -
notificacao-1  | 03:14:27 [notificacao] e-mail para pedro@exemplo.com: Pedido 3 cancelado: estoque insuficiente.
notificacao-1  | 03:14:27 [notificacao] 172.18.0.6 - - [16/Nov/2026 03:14:27] "POST /notificacoes HTTP/1.1" 200 -
estoque-1      |  * Running on http://127.0.0.1:5002
estoque-1      |  * Running on http://172.18.0.2:5002
estoque-1      | 03:08:58 [estoque] Press CTRL+C to quit
estoque-1      |  * Serving Flask app 'app'
estoque-1      |  * Debug mode: off
estoque-1      | 03:13:31 [estoque] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
estoque-1      |  * Running on all addresses (0.0.0.0)
pedidos-1      |  * Debug mode: off
estoque-1      |  * Running on http://127.0.0.1:5002
pagamento-1    |  * Serving Flask app 'app'
pagamento-1    |  * Debug mode: off
pedidos-1      | 03:08:59 [pedidos] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
pedidos-1      |  * Running on all addresses (0.0.0.0)
pedidos-1      |  * Running on http://127.0.0.1:5000
pedidos-1      |  * Running on http://172.18.0.6:5000
pedidos-1      | 03:08:59 [pedidos] Press CTRL+C to quit
catalogo-1     |  * Debug mode: off
catalogo-1     | 03:08:58 [catalogo] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
estoque-1      |  * Running on http://172.18.0.3:5002
estoque-1      | 03:13:31 [estoque] Press CTRL+C to quit
estoque-1      | 03:14:26 [estoque] reservadas 2 unidade(s) do produto 1 (restam 8)
pedidos-1      |  * Serving Flask app 'app'
pedidos-1      |  * Debug mode: off
estoque-1      | 03:14:26 [estoque] 172.18.0.6 - - [16/Nov/2026 03:14:26] "POST /estoque/reservar HTTP/1.1" 200 -
catalogo-1     |  * Running on all addresses (0.0.0.0)
pagamento-1    | 03:08:58 [pagamento] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
pedidos-1      | 03:13:31 [pedidos] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
pedidos-1      |  * Running on all addresses (0.0.0.0)
pedidos-1      |  * Running on http://127.0.0.1:5000
pedidos-1      |  * Running on http://172.18.0.6:5000
pedidos-1      | 03:13:31 [pedidos] Press CTRL+C to quit
pedidos-1      | 03:14:26 [pedidos] pedido 1 recebido de pedro@exemplo.com
pedidos-1      | 03:14:26 [pedidos] pedido 1 PAGO (R$ 500.00)
pagamento-1    |  * Running on all addresses (0.0.0.0)
pedidos-1      | 03:14:26 [pedidos] 172.18.0.1 - - [16/Nov/2026 03:14:26] "POST /pedidos HTTP/1.1" 201 -
pedidos-1      | 03:14:26 [pedidos] pedido 2 recebido de eduardo@exemplo.com
pedidos-1      | 03:14:26 [pedidos] pedido 2 cancelado: pagamento recusado, estoque devolvido
pedidos-1      | 03:14:26 [pedidos] 172.18.0.1 - - [16/Nov/2026 03:14:26] "POST /pedidos HTTP/1.1" 402 -
pagamento-1    |  * Running on http://127.0.0.1:5003
catalogo-1     |  * Running on http://127.0.0.1:5001
pedidos-1      | 03:14:26 [pedidos] pedido 3 recebido de pedro@exemplo.com
pedidos-1      | 03:14:27 [pedidos] pedido 3 cancelado: estoque insuficiente
pedidos-1      | 03:14:27 [pedidos] 172.18.0.1 - - [16/Nov/2026 03:14:27] "POST /pedidos HTTP/1.1" 409 -
pagamento-1    |  * Running on http://172.18.0.4:5003
estoque-1      | 03:14:26 [estoque] reservadas 1 unidade(s) do produto 2 (restam 4)
estoque-1      | 03:14:26 [estoque] 172.18.0.6 - - [16/Nov/2026 03:14:26] "POST /estoque/reservar HTTP/1.1" 200 -
estoque-1      | 03:14:26 [estoque] liberadas 1 unidade(s) do produto 2 (restam 5)
estoque-1      | 03:14:26 [estoque] 172.18.0.6 - - [16/Nov/2026 03:14:26] "POST /estoque/liberar HTTP/1.1" 200 -
estoque-1      | 03:14:27 [estoque] reserva negada: produto 3, pedido de 5, disponivel 2
estoque-1      | 03:14:27 [estoque] 172.18.0.6 - - [16/Nov/2026 03:14:27] "POST /estoque/reservar HTTP/1.1" 409 -
catalogo-1     |  * Running on http://172.18.0.3:5001
catalogo-1     | 03:08:58 [catalogo] Press CTRL+C to quit
catalogo-1     |  * Serving Flask app 'app'
catalogo-1     |  * Debug mode: off
pagamento-1    | 03:08:58 [pagamento] Press CTRL+C to quit
pagamento-1    |  * Serving Flask app 'app'
catalogo-1     | 03:13:31 [catalogo] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
catalogo-1     |  * Running on all addresses (0.0.0.0)
catalogo-1     |  * Running on http://127.0.0.1:5001
catalogo-1     |  * Running on http://172.18.0.2:5001
catalogo-1     | 03:13:31 [catalogo] Press CTRL+C to quit
catalogo-1     | 03:14:26 [catalogo] consulta produto 1 (Teclado mecanico)
catalogo-1     | 03:14:26 [catalogo] 172.18.0.6 - - [16/Nov/2026 03:14:26] "GET /produtos/1 HTTP/1.1" 200 -
catalogo-1     | 03:14:26 [catalogo] consulta produto 2 (Mouse gamer)
catalogo-1     | 03:14:26 [catalogo] 172.18.0.6 - - [16/Nov/2026 03:14:26] "GET /produtos/2 HTTP/1.1" 200 -
catalogo-1     | 03:14:26 [catalogo] consulta produto 3 (Monitor 24 pol)
catalogo-1     | 03:14:26 [catalogo] 172.18.0.6 - - [16/Nov/2026 03:14:26] "GET /produtos/3 HTTP/1.1" 200 -
pagamento-1    |  * Debug mode: off
pagamento-1    | 03:13:31 [pagamento] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
pagamento-1    |  * Running on all addresses (0.0.0.0)
pagamento-1    |  * Running on http://127.0.0.1:5003
pagamento-1    |  * Running on http://172.18.0.5:5003
pagamento-1    | 03:13:31 [pagamento] Press CTRL+C to quit
pagamento-1    | 03:14:26 [pagamento] pedido 1: pagamento APROVADO (valor 500.00, transacao 1096a886)
pagamento-1    | 03:14:26 [pagamento] 172.18.0.6 - - [16/Nov/2026 03:14:26] "POST /pagamentos HTTP/1.1" 200 -
pagamento-1    | 03:14:26 [pagamento] pedido 2: pagamento RECUSADO (valor 120.00)
pagamento-1    | 03:14:26 [pagamento] 172.18.0.6 - - [16/Nov/2026 03:14:26] "POST /pagamentos HTTP/1.1" 402 -
```
