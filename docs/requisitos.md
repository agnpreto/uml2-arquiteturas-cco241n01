# Requisitos

Sistema: **Marketplace com pagamento**, arquitetura orientada a serviços (SOA).

## Requisitos funcionais

| ID | Requisito |
| --- | --- |
| RF01 | O sistema deve listar os produtos disponíveis no catálogo, com nome, preço e vendedor. |
| RF02 | O cliente deve poder criar um pedido informando produto, quantidade e dados de pagamento. |
| RF03 | O sistema deve reservar no estoque as unidades do pedido e recusar o pedido quando não houver unidades suficientes. |
| RF04 | O sistema deve processar o pagamento do pedido e, se for recusado, cancelar o pedido e devolver o estoque reservado. |
| RF05 | O sistema deve notificar o cliente sobre a confirmação ou o cancelamento do pedido. |

## Requisitos não funcionais

| ID | Requisito |
| --- | --- |
| RNF01 | Cada serviço deve ser independente (processo e contêiner próprios) e se comunicar apenas por APIs HTTP/JSON. |
| RNF02 | O sistema inteiro deve subir com um único comando (`docker compose up --build`). |
| RNF03 | Cada serviço deve registrar em log as operações relevantes, com horário e nome do serviço, para rastrear o fluxo de um pedido. |
