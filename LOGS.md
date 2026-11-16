
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

Cole abaixo o conteúdo completo gerado pelo comando:

```bash
docker compose logs --no-color
```
