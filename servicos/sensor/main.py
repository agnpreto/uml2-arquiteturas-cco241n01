"""Serviço SENSOR: simula estações de monitoramento (fumaça + PM2.5) em Manaus
e PUBLICA eventos de leitura.

Canal publicado: "leituras"
Campos: sensor_id, local, fumaca_ppm, pm25 (ug/m3), timestamp
"""
import json, os, random, time
from datetime import datetime
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
INTERVALO = float(os.getenv("INTERVALO", "1"))      # segundos entre leituras
random.seed(int(os.getenv("SEED", "42")))           # simulação reproduzível

SENSORES = [
    ("S1", "Distrito Industrial"),
    ("S2", "Centro"),           # episódio de névoa/poluição (PM2.5 alto, sem fogo local)
    ("S3", "Reserva Ducke"),    # foco de incêndio (fumaça e PM2.5 sobem juntos)
]
FOGO = (6, 14)    # ciclos do incêndio em S3
NEVOA = (2, 8)    # ciclos de névoa em S2


def conectar():
    while True:
        try:
            r = redis.Redis(host=REDIS_HOST, decode_responses=True)
            r.ping()
            return r
        except redis.ConnectionError:
            print("aguardando broker...", flush=True)
            time.sleep(1)


def leitura(sensor_id, ciclo):
    """Retorna (fumaca_ppm, pm25) simulados."""
    fumaca = random.uniform(15, 60)
    pm25 = random.uniform(8, 28)
    if sensor_id == "S3" and FOGO[0] <= ciclo < FOGO[1]:
        k = ciclo - FOGO[0]
        fumaca = 120 + k * 75 + random.uniform(-10, 10)
        pm25 = 40 + k * 20 + random.uniform(-3, 3)
    if sensor_id == "S2" and NEVOA[0] <= ciclo < NEVOA[1]:
        pm25 = random.uniform(42, 62)
    return round(fumaca, 1), round(pm25, 1)


def main():
    r = conectar()
    print(f"[sensor] conectado ao broker em {REDIS_HOST}", flush=True)
    ciclo = 0
    while True:
        for sensor_id, local in SENSORES:
            fumaca, pm25 = leitura(sensor_id, ciclo)
            evento = {
                "sensor_id": sensor_id, "local": local,
                "fumaca_ppm": fumaca, "pm25": pm25,
                "timestamp": datetime.now().isoformat(timespec="seconds"),
            }
            r.publish("leituras", json.dumps(evento))
            print(f"[sensor] leitura publicada: {sensor_id} ({local}) fumaca={fumaca} ppm | PM2.5={pm25} ug/m3", flush=True)
        ciclo += 1
        time.sleep(INTERVALO)


if __name__ == "__main__":
    main()
