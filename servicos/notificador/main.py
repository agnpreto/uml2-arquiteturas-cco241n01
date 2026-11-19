"""Serviço NOTIFICADOR: CONSOME "alertas" e envia a notificação (simulada)."""
import json, os, time
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")


def conectar():
    while True:
        try:
            r = redis.Redis(host=REDIS_HOST, decode_responses=True)
            r.ping()
            return r
        except redis.ConnectionError:
            print("aguardando broker...", flush=True)
            time.sleep(1)


def main():
    r = conectar()
    p = r.pubsub()
    p.subscribe("alertas")
    print("[notificador] inscrito no canal 'alertas'", flush=True)
    for msg in p.listen():
        if msg["type"] != "message":
            continue
        a = json.loads(msg["data"])
        local = a["local"]
        if a["tipo"] == "NORMALIZADO":
            print(f"[notificador] Situacao normalizada em {local}", flush=True)
        elif a["tipo"] == "QUALIDADE_AR":
            print(f"[notificador] Aviso de qualidade do ar ({a['nivel']}) em {local}: PM2.5 = {a['pm25']} ug/m3 -> Defesa Civil / Vigilancia em Saude", flush=True)
        elif a["nivel"] == "PERIGO":
            print(f"[notificador] SMS + ligacao aos Bombeiros (CBMAM): fumaca intensa em {local} ({a['fumaca_ppm']} ppm)", flush=True)
        else:
            print(f"[notificador] Aviso a Defesa Civil: fumaca elevada em {local} ({a['fumaca_ppm']} ppm)", flush=True)


if __name__ == "__main__":
    main()
