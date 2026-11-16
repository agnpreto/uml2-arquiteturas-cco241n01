# Trabalho de Análise e Projeto de Sistemas: Arquiteturas de Software

**Disciplina:** Análise e Projeto de Sistemas (Ciência da Computação)  
**Prazo:** 18/11/2026

## Equipe

**Nome do time:** Marketplace SOA  
**Modelo escolhido:** 4 (Marketplace com pagamento, arquitetura orientada a serviços)

| Nome | Usuário do GitHub |
| --- | --- |
| Pedro Henrique | pedroallencar |
| Eduardo Victor | EduardoVitorr |

## Sobre o sistema

Marketplace em que o cliente compra um produto e o sistema reserva o estoque, cobra o pagamento e avisa o cliente. Cada responsabilidade é um serviço independente, e o serviço de **Pedidos** orquestra a chamada aos demais (orquestração SOA). Se o pagamento falha, o estoque reservado é devolvido.

| Serviço | Porta | Função |
| --- | --- | --- |
| `pedidos` | 5000 | Orquestrador do fluxo de compra (único exposto ao cliente) |
| `catalogo` | 5001 | Lista e consulta produtos e preços |
| `estoque` | 5002 | Consulta, reserva e libera unidades |
| `pagamento` | 5003 | Simula o gateway de pagamento (cartão terminado em `0000` é recusado) |
| `notificacao` | 5004 | Simula o envio de e-mail ao cliente |

Documentação em `docs/`: [requisitos](docs/requisitos.md), [arquitetura](docs/arquitetura.png) e [diagrama de sequência](docs/sequencia.png).

## Como rodar

Subir o sistema (requer Docker):

```
docker compose up --build
```

Em outro terminal, executar o fluxo principal (três cenários: compra aprovada, pagamento recusado e estoque insuficiente):

```
python fluxo.py
```

Os logs de cada serviço aparecem no terminal do `docker compose`. Um exemplo de execução está em [LOGS.md](LOGS.md).

## Entrega

Pull Request único do fork para o repositório do professor.
