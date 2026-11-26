# LOGS - Fluxo principal

Saída do terminal ao executar o fluxo principal do sistema (broker Redis + os 4 serviços: sensor, detector, notificador e histórico).

O que aparece, em ordem:
1. **S2 (Centro):** PM2.5 sobe por causa da névoa -> alerta `QUALIDADE_AR` em ATENÇÃO -> normaliza.
2. **S3 (Reserva Ducke):** incêndio -> `INCENDIO_SUSPEITO` em ATENÇÃO -> PERIGO (aviso aos Bombeiros) -> normaliza.
3. **S1 (Distrito Industrial):** sempre normal, sem alertas.

As linhas `[historico]` mostram cada alerta sendo gravado no banco. Como os serviços rodam em paralelo, algumas linhas de serviços diferentes aparecem entrelaçadas.

```text
[detector] inscrito no canal 'leituras'
[notificador] inscrito no canal 'alertas'
[historico] gravando em /data/historico.db
[sensor] conectado ao broker em localhost
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=43.8 ppm | PM2.5=8.5 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=27.4 ppm | PM2.5=12.5 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=48.1 ppm | PM2.5=21.5 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=55.1 ppm | PM2.5=9.7 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=34.0 ppm | PM2.5=8.6 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=24.8 ppm | PM2.5=18.1 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=16.2 ppm | PM2.5=12.0 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=44.2 ppm | PM2.5=46.4 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=41.5 ppm | PM2.5=24.2 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=15.3 ppm | PM2.5=24.1 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=46.4 ppm | PM2.5=45.1 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=58.1 ppm | PM2.5=14.7 ug/m3
[detector] ALERTA publicado: S2 QUALIDADE_AR NORMAL -> ATENCAO (fumaca=46.4 ppm, PM2.5=45.1 ug/m3)
[notificador] Aviso de qualidade do ar (ATENCAO) em Centro: PM2.5 = 45.1 ug/m3 -> Defesa Civil / Vigilancia em Saude
[historico] alerta registrado (total de alertas no banco: 1)
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=19.2 ppm | PM2.5=9.9 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=53.1 ppm | PM2.5=58.1 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=47.8 ppm | PM2.5=18.7 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=58.8 ppm | PM2.5=15.6 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=39.8 ppm | PM2.5=54.4 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=53.8 ppm | PM2.5=19.5 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=46.7 ppm | PM2.5=8.9 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=25.3 ppm | PM2.5=43.6 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=115.6 ppm | PM2.5=40.8 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=31.4 ppm | PM2.5=15.4 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=24.4 ppm | PM2.5=60.7 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=188.4 ppm | PM2.5=61.4 ug/m3
[notificador] Aviso a Defesa Civil: fumaca elevada em Reserva Ducke (188.4 ppm)
[detector] ALERTA publicado: S3 INCENDIO_SUSPEITO NORMAL -> ATENCAO (fumaca=188.4 ppm, PM2.5=61.4 ug/m3)
[historico] alerta registrado (total de alertas no banco: 2)
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=22.4 ppm | PM2.5=15.6 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=59.5 ppm | PM2.5=20.8 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=276.9 ppm | PM2.5=81.7 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=25.3 ppm | PM2.5=8.6 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=29.2 ppm | PM2.5=13.4 ug/m3
[detector] ALERTA publicado: S2 NORMALIZADO ATENCAO -> NORMAL (fumaca=29.2 ppm, PM2.5=13.4 ug/m3)
[notificador] Situacao normalizada em Centro
[notificador] SMS + ligacao aos Bombeiros (CBMAM): fumaca intensa em Reserva Ducke (352.5 ppm)
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=352.5 ppm | PM2.5=98.9 ug/m3
[detector] ALERTA publicado: S3 INCENDIO_SUSPEITO ATENCAO -> PERIGO (fumaca=352.5 ppm, PM2.5=98.9 ug/m3)
[historico] alerta registrado (total de alertas no banco: 3)
[historico] alerta registrado (total de alertas no banco: 4)
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=44.5 ppm | PM2.5=15.9 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=56.2 ppm | PM2.5=17.2 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=421.2 ppm | PM2.5=118.6 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=41.3 ppm | PM2.5=26.0 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=33.0 ppm | PM2.5=12.4 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=486.8 ppm | PM2.5=137.3 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=19.9 ppm | PM2.5=20.5 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=50.6 ppm | PM2.5=16.4 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=579.9 ppm | PM2.5=160.2 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=58.7 ppm | PM2.5=25.2 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=15.5 ppm | PM2.5=22.4 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=640.3 ppm | PM2.5=180.8 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=20.0 ppm | PM2.5=16.7 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=35.4 ppm | PM2.5=27.1 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=54.4 ppm | PM2.5=13.3 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=37.5 ppm | PM2.5=11.6 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=56.1 ppm | PM2.5=25.4 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=28.4 ppm | PM2.5=20.8 ug/m3
[detector] ALERTA publicado: S3 NORMALIZADO PERIGO -> NORMAL (fumaca=28.4 ppm, PM2.5=20.8 ug/m3)
[notificador] Situacao normalizada em Reserva Ducke
[historico] alerta registrado (total de alertas no banco: 5)
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=42.4 ppm | PM2.5=11.1 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=49.3 ppm | PM2.5=18.8 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=50.0 ppm | PM2.5=18.6 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=15.0 ppm | PM2.5=14.5 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=15.9 ppm | PM2.5=26.6 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=54.5 ppm | PM2.5=24.6 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=28.8 ppm | PM2.5=9.2 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=54.5 ppm | PM2.5=26.9 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=18.9 ppm | PM2.5=17.7 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=18.1 ppm | PM2.5=23.2 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=49.5 ppm | PM2.5=10.6 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=36.4 ppm | PM2.5=19.0 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=26.9 ppm | PM2.5=25.4 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=34.0 ppm | PM2.5=12.2 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=39.3 ppm | PM2.5=22.6 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=24.1 ppm | PM2.5=14.2 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=59.8 ppm | PM2.5=21.0 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=34.7 ppm | PM2.5=18.4 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=20.4 ppm | PM2.5=12.5 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=30.2 ppm | PM2.5=19.8 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=25.4 ppm | PM2.5=12.4 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=18.2 ppm | PM2.5=20.6 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=25.3 ppm | PM2.5=26.1 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=53.7 ppm | PM2.5=9.4 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=25.7 ppm | PM2.5=21.4 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=24.6 ppm | PM2.5=10.6 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=57.1 ppm | PM2.5=19.4 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=36.3 ppm | PM2.5=23.7 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=51.3 ppm | PM2.5=11.8 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=19.4 ppm | PM2.5=16.6 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=34.1 ppm | PM2.5=17.3 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=47.8 ppm | PM2.5=21.5 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=59.3 ppm | PM2.5=10.0 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=33.1 ppm | PM2.5=14.8 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=53.8 ppm | PM2.5=13.0 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=23.6 ppm | PM2.5=17.0 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=34.0 ppm | PM2.5=13.6 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=26.2 ppm | PM2.5=26.5 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=34.9 ppm | PM2.5=25.2 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=39.8 ppm | PM2.5=9.0 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=60.0 ppm | PM2.5=24.7 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=58.6 ppm | PM2.5=26.5 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=53.2 ppm | PM2.5=11.3 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=36.9 ppm | PM2.5=12.3 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=33.0 ppm | PM2.5=9.2 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=32.1 ppm | PM2.5=27.7 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=26.9 ppm | PM2.5=23.7 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=35.5 ppm | PM2.5=16.5 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=58.1 ppm | PM2.5=27.9 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=40.0 ppm | PM2.5=22.4 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=22.0 ppm | PM2.5=13.9 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=58.6 ppm | PM2.5=19.6 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=39.4 ppm | PM2.5=23.0 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=17.6 ppm | PM2.5=19.7 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=37.6 ppm | PM2.5=25.1 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=22.1 ppm | PM2.5=27.2 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=18.6 ppm | PM2.5=11.7 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=41.8 ppm | PM2.5=21.5 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=25.6 ppm | PM2.5=10.4 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=55.1 ppm | PM2.5=12.9 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=41.8 ppm | PM2.5=20.4 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=33.9 ppm | PM2.5=19.7 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=38.5 ppm | PM2.5=26.7 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=24.2 ppm | PM2.5=22.3 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=25.7 ppm | PM2.5=15.9 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=45.2 ppm | PM2.5=14.0 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=29.2 ppm | PM2.5=23.0 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=18.3 ppm | PM2.5=17.2 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=59.9 ppm | PM2.5=27.9 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=18.3 ppm | PM2.5=12.3 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=26.9 ppm | PM2.5=26.7 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=54.6 ppm | PM2.5=25.6 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=31.6 ppm | PM2.5=11.2 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=52.5 ppm | PM2.5=22.1 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=42.5 ppm | PM2.5=27.7 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=44.4 ppm | PM2.5=8.2 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=51.8 ppm | PM2.5=14.0 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=44.9 ppm | PM2.5=26.8 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=21.0 ppm | PM2.5=10.3 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=19.8 ppm | PM2.5=19.1 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=27.3 ppm | PM2.5=20.1 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=47.3 ppm | PM2.5=12.1 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=43.5 ppm | PM2.5=13.3 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=37.0 ppm | PM2.5=26.1 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=53.1 ppm | PM2.5=9.8 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=34.1 ppm | PM2.5=13.5 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=15.2 ppm | PM2.5=23.4 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=43.7 ppm | PM2.5=13.2 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=48.4 ppm | PM2.5=19.0 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=34.2 ppm | PM2.5=8.2 ug/m3
[sensor] leitura publicada: S1 (Distrito Industrial) fumaca=18.4 ppm | PM2.5=25.7 ug/m3
[sensor] leitura publicada: S2 (Centro) fumaca=55.7 ppm | PM2.5=18.9 ug/m3
[sensor] leitura publicada: S3 (Reserva Ducke) fumaca=52.6 ppm | PM2.5=19.7 ug/m3
```
