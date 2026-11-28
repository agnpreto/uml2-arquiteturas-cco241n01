# Logs do fluxo principal

Descrevam em uma frase o fluxo executado e colem abaixo os logs copiados do terminal.

**Fluxo:** 

```
# LOGS — Registros do fluxo principal

## Teste de integração executado localmente

**Ambiente:** quatro processos Python executados localmente, com as mesmas portas e rotas do Compose. **Não foi um teste com Docker**.  
**Data do teste:** 18/11/2026 17:50.

| Verificação | Resultado observado |
|---|---|
| `GET /saude` | HTTP 200 |
| `GET /cardapio` | HTTP 200, três produtos |
| `POST /pedidos` | HTTP 201, pedido 1 confirmado, total R$ 49,80 |
| `GET /pedidos` | HTTP 200, pedido na lista |
| `GET /pedidos/1` | HTTP 200, pedido localizado |

### Trechos reais capturados dos processos locais

```text

# cardapio
2026-11-18 17:50:19,082 [cardapio] GET /cardapio
127.0.0.1 - - [18/Nov/2026 17:50:19] "GET /cardapio HTTP/1.1" 200 -
2026-11-18 17:50:19,094 [cardapio] GET /cardapio
127.0.0.1 - - [18/Nov/2026 17:50:19] "GET /cardapio HTTP/1.1" 200 -

# pagamentos
2026-11-18 17:50:19,096 [pagamentos] POST /autorizar -> aprovado (simulacao)
127.0.0.1 - - [18/Nov/2026 17:50:19] "POST /autorizar HTTP/1.1" 200 -

# pedidos
2026-11-18 17:50:19,085 [pedidos] consultando produtos no cardapio
2026-11-18 17:50:19,094 [pedidos] solicitando autorizacao ao servico pagamentos
2026-11-18 17:50:19,096 [pedidos] pedido 1 confirmado; total=49.80
127.0.0.1 - - [18/Nov/2026 17:50:19] "POST /pedidos HTTP/1.1" 201 -
127.0.0.1 - - [18/Nov/2026 17:50:19] "GET /pedidos HTTP/1.1" 200 -
127.0.0.1 - - [18/Nov/2026 17:50:19] "GET /pedidos/1 HTTP/1.1" 200 -

# gateway
2026-11-18 17:50:19,071 [gateway] GET /cardapio -> cardapio
127.0.0.1 - - [18/Nov/2026 17:50:19] "GET /cardapio HTTP/1.1" 200 -
2026-11-18 17:50:19,082 [gateway] resposta: 200
2026-11-18 17:50:19,084 [gateway] POST /pedidos -> pedidos
127.0.0.1 - - [18/Nov/2026 17:50:19] "POST /pedidos HTTP/1.1" 201 -
2026-11-18 17:50:19,097 [gateway] resposta: 201
2026-11-18 17:50:19,098 [gateway] GET /pedidos -> pedidos
127.0.0.1 - - [18/Nov/2026 17:50:19] "GET /pedidos HTTP/1.1" 200 -
2026-11-18 17:50:19,099 [gateway] resposta: 200
2026-11-18 17:50:19,100 [gateway] GET /pedidos/1 -> pedidos
127.0.0.1 - - [18/Nov/2026 17:50:19] "GET /pedidos/1 HTTP/1.1" 200 -
2026-11-18 17:50:19,101 [gateway] resposta: 200
```

## Como coletar os logs com Docker para a entrega

1. Na pasta do projeto, execute `docker compose up --build -d`.
2. Execute a consulta ao cardápio e crie um pedido conforme o README.
3. Capture os logs com `docker compose logs --timestamps gateway pedidos cardapio pagamentos`.
4. Cole os registros abaixo, sem inventar linhas. Os horários e IDs podem variar.

### Evidências de execução com Docker pela equipe

_A preencher após executar no computador da equipe._

## Interpretação do fluxo

O Gateway recebe as chamadas externas. Pedidos busca os preços em Cardápio e solicita autorização simulada a Pagamentos. Se a autorização é aprovada, Pedidos registra a compra e devolve HTTP 201. Os logs permitem identificar em qual etapa ocorreu uma falha.

```
