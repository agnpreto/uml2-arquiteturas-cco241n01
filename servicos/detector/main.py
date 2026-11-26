"""Serviço DETECTOR: CONSOME "leituras", aplica as regras e PUBLICA "alertas".

Regras (limiares configuráveis, valores didáticos):
  - Fumaça: ATENCAO >= 150 ppm | PERIGO >= 300 ppm
  - PM2.5:  ATENCAO >= 35 ug/m3 | PERIGO >= 75 ug/m3
  - Nível da leitura = o pior entre fumaça e PM2.5
  - Só dispara alerta após 2 leituras consecutivas no mesmo nível (evita falso positivo)
  - Só publica quando o nível MUDA (evita alerta repetido)
  - Tipo do alerta: INCENDIO_SUSPEITO (fumaça alta) | QUALIDADE_AR (só PM2.5 alto) | NORMALIZADO
"""
import json, os, time
from datetime import datetime
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
FUMACA_ATENCAO = float(os.getenv("FUMACA_ATENCAO", "150"))
FUMACA_PERIGO = float(os.getenv("FUMACA_PERIGO", "300"))
PM25_ATENCAO = float(os.getenv("PM25_ATENCAO", "35"))
PM25_PERIGO = float(os.getenv("PM25_PERIGO", "75"))
CONFIRMACOES = int(os.getenv("CONFIRMACOES", "2"))
ORDEM = {"NORMAL": 0, "ATENCAO": 1, "PERIGO": 2}


def conectar():
    while True:
        try:
            r = redis.Redis(host=REDIS_HOST, decode_responses=True)
            r.ping()
            return r
        except redis.ConnectionError:
            print("aguardando broker...", flush=True)
            time.sleep(1)


def classificar(valor, atencao, perigo):
    if valor >= perigo:
        return "PERIGO"
    if valor >= atencao:
        return "ATENCAO"
    return "NORMAL"


def main():
    r = conectar()
    p = r.pubsub()
    p.subscribe("leituras")
    print("[detector] inscrito no canal 'leituras'", flush=True)

    nivel_atual = {}      # sensor_id -> último nível confirmado
    candidato = {}        # sensor_id -> (nível, contagem)

    for msg in p.listen():
        if msg["type"] != "message":
            continue
        ev = json.loads(msg["data"])
        sid = ev["sensor_id"]
        n_fumaca = classificar(ev["fumaca_ppm"], FUMACA_ATENCAO, FUMACA_PERIGO)
        n_pm = classificar(ev["pm25"], PM25_ATENCAO, PM25_PERIGO)
        nivel = max(n_fumaca, n_pm, key=ORDEM.get)

        nivel_c, cont = candidato.get(sid, (nivel, 0))
        cont = cont + 1 if nivel == nivel_c else 1
        candidato[sid] = (nivel, cont)

        if cont >= CONFIRMACOES and nivel != nivel_atual.get(sid, "NORMAL"):
            anterior = nivel_atual.get(sid, "NORMAL")
            nivel_atual[sid] = nivel
            if nivel == "NORMAL":
                tipo = "NORMALIZADO"
            elif n_fumaca != "NORMAL":
                tipo = "INCENDIO_SUSPEITO"
            else:
                tipo = "QUALIDADE_AR"
            alerta = {
                "tipo": tipo, "nivel": nivel, "nivel_anterior": anterior,
                "sensor_id": sid, "local": ev["local"],
                "fumaca_ppm": ev["fumaca_ppm"], "pm25": ev["pm25"],
                "timestamp": datetime.now().isoformat(timespec="seconds"),
            }
            r.publish("alertas", json.dumps(alerta))
            print(f"[detector] ALERTA publicado: {sid} {tipo} {anterior} -> {nivel} "
                  f"(fumaca={ev['fumaca_ppm']} ppm, PM2.5={ev['pm25']} ug/m3)", flush=True)


if __name__ == "__main__":
    main()
