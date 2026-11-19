# Requisitos

## Requisitos funcionais

| ID | Requisito |
| --- | --- |
| RF01 | O sistema deve simular a coleta de dados das três estações (S1, S2 e S3), registrando os níveis de fumaça (ppm) e PM2.5 (µg/m³). |
| RF02 | O sistema deve receber e processar as informações dos sensores por meio do broker Redis. |
| RF03 | O sistema deve analisar as medições e identificar os níveis de qualidade do ar: NORMAL, ATENÇÃO e PERIGO. |
| RF04 | O sistema deve enviar notificações simuladas aos órgãos responsáveis, de acordo com o tipo e a gravidade do alerta. |
| RF05 | O sistema deve armazenar o histórico das leituras dos sensores e dos alertas gerados. |

## Requisitos não funcionais

| ID | Requisito |
| --- | --- |
| RNF01 | O sistema deve utilizar arquitetura orientada a eventos, permitindo a comunicação entre os serviços por meio de mensagens. |
| RNF02 | O sistema deve permitir a execução integrada dos serviços utilizando Docker Compose, por meio de um único comando. |
| RNF03 | Os componentes devem funcionar como serviços independentes, facilitando a manutenção e futuras atualizações. |
