# Trabalho de Análise e Projeto de Sistemas: Arquiteturas de Software

**Disciplina:** Análise e Projeto de Sistemas (Ciência da Computação)
**Prazo:** 18/11/2026

## Equipe

**Nome do time:** Monitoramento de sensores
**Modelo escolhido:** 2 - Monitoramento de sensores (arquitetura orientada a eventos)

| Nome | Usuário do GitHub |
|------|-------------------|
| Rafaela Martins | RafaelaMrtns |
| Yasmim Medeiros | Yazzymds |
| Felipe Velarde | Felipeclave |
| Rian Rosenberg | rianamarorosenberg-dotcom |
| Maria Vitoria | mvitoriaaa |

## Sobre o sistema

Sistema de monitoramento ambiental para Manaus: estações de sensores medem **fumaça (ppm)** e **material particulado PM2.5 (µg/m³)** e o sistema detecta possíveis **focos de incêndio** e **piora da qualidade do ar**, avisando os responsáveis. O tema foi escolhido por causa do impacto das queimadas e da fumaça na cidade.

### Como funciona (arquitetura orientada a eventos)

Os serviços não se chamam diretamente: cada um publica e consome **eventos** num broker (Redis Pub/Sub), e por isso podem ser trocados ou cair de forma independente.

| Serviço | Papel | Consome | Publica |
|---------|-------|---------|---------|
| `servicos/sensor` | Simula as estações S1 (Distrito Industrial), S2 (Centro) e S3 (Reserva Ducke) | - | `leituras` |
| `servicos/detector` | Classifica as leituras (NORMAL / ATENÇÃO / PERIGO) e gera alertas | `leituras` | `alertas` |
| `servicos/notificador` | Avisa Defesa Civil, Bombeiros ou Vigilância em Saúde (simulado) | `alertas` | - |
| `servicos/historico` | Grava leituras e alertas em SQLite | `leituras`, `alertas` | - |

Tipos de alerta: `INCENDIO_SUSPEITO` (fumaça alta), `QUALIDADE_AR` (só PM2.5 alto) e `NORMALIZADO`.

Documentação: [`docs/requisitos.md`](docs/requisitos.md), [`docs/arquitetura.png`](docs/arquitetura.png), [`docs/sequencia.png`](docs/sequencia.png) e [`LOGS.md`](LOGS.md).

## Como rodar

Pré-requisito: Docker com Docker Compose.

**Um comando:**

```bash
docker compose up --build
```

### Fluxo principal (o que acontece ao rodar)
O próprio sistema executa a simulação, sem precisar fazer mais nada. Em cerca de 20 segundos aparecem no terminal:

1. **S2 (Centro):** a névoa faz o PM2.5 subir -> alerta `QUALIDADE_AR` (ATENÇÃO) -> depois normaliza.
2. **S3 (Reserva Ducke):** fumaça e PM2.5 sobem juntos -> `INCENDIO_SUSPEITO` em ATENÇÃO -> PERIGO (aviso aos Bombeiros) -> normaliza.
3. **S1 (Distrito Industrial):** fica sempre normal.

O que cada serviço mostra: `[sensor]` leituras publicadas, `[detector]` alertas gerados, `[notificador]` avisos enviados, `[historico]` alertas gravados no banco.

Para ver só os alertas: `docker compose logs -f detector notificador`
Para parar: `Ctrl+C` e depois `docker compose down`.

### Configuração (opcional, variáveis de ambiente)
- detector: `FUMACA_ATENCAO` (150), `FUMACA_PERIGO` (300), `PM25_ATENCAO` (35), `PM25_PERIGO` (75), `CONFIRMACOES` (2)
- sensor: `INTERVALO` (1 s entre leituras)

Os limiares são valores didáticos para a simulação.

## Estrutura do repositório

```
README.md
LOGS.md
docker-compose.yml
docs/        requisitos.md, arquitetura.png, sequencia.png
servicos/
  sensor/  detector/  notificador/  historico/    (cada um com main.py, Dockerfile e requirements.txt)
```

## Entrega
Pull Request do fork da equipe para o repositório do professor (Contribute -> Open pull request).
