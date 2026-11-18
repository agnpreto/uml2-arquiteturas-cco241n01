# Logs do fluxo principal

O sistema foi executado utilizando Docker Compose. Durante a simulação, as três estações enviaram leituras ao broker Redis. O detector analisou os dados, publicou alertas quando necessário, o notificador simulou o envio às instituições responsáveis e o histórico armazenou os eventos no banco SQLite.

**Fluxo:** 

```
## Resultados observados

- **S1 — Distrito Industrial:** permaneceu sem gerar alertas durante o trecho registrado.
- **S2 — Centro:** apresentou aumento de PM2.5, gerando alerta de qualidade do ar em nível ATENÇÃO e posteriormente normalizando.
- **S3 — Reserva Ducke:** apresentou aumento de fumaça, gerando alerta em ATENÇÃO, evoluindo para PERIGO e posteriormente normalizando.
- **Histórico:** registrou 5 eventos de alerta no banco de dados.

## Saída do terminal

```text
broker-1 | Redis version=7.4.12
broker-1 | Ready to accept connections tcp

detector-1 | [detector] inscrito no canal 'leituras'
sensor-1 | [sensor] conectado ao broker em broker
notificador-1 | [notificador] inscrito no canal 'alertas'
historico-1 | [historico] gravando em /data/historico.db

sensor-1 | leitura publicada: S2 (Centro) fumaca=44.2 ppm | PM2.5=46.4 ug/m3

detector-1 | ALERTA publicado: S2 QUALIDADE_AR NORMAL -> ATENCAO (fumaca=46.4 ppm, PM2.5=45.1 ug/m3)

notificador-1 | Aviso de qualidade do ar (ATENCAO) em Centro: PM2.5 = 45.1 ug/m3 -> Defesa Civil / Vigilancia em Saude

historico-1 | alerta registrado (total de alertas no banco: 1)

detector-1 | ALERTA publicado: S3 INCENDIO_SUSPEITO NORMAL -> ATENCAO (fumaca=188.4 ppm, PM2.5=61.4 ug/m3)

notificador-1 | Aviso a Defesa Civil: fumaca elevada em Reserva Ducke (188.4 ppm)

detector-1 | ALERTA publicado: S3 INCENDIO_SUSPEITO ATENCAO -> PERIGO (fumaca=352.5 ppm, PM2.5=98.9 ug/m3)

notificador-1 | SMS + ligacao aos Bombeiros (CBMAM): fumaca intensa em Reserva Ducke (352.5 ppm)

detector-1 | ALERTA publicado: S3 NORMALIZADO PERIGO -> NORMAL (fumaca=28.4 ppm, PM2.5=20.8 ug/m3)

notificador-1 | Situacao normalizada em Reserva Ducke

historico-1 | alerta registrado (total de alertas no banco: 5)

```
```
