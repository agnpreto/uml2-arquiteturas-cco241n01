"""Serviço HISTÓRICO: CONSOME "leituras" e "alertas" e grava tudo em SQLite."""
import json, os, sqlite3, time
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
DB_PATH = os.getenv("DB_PATH", "/data/historico.db")


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
    os.makedirs(os.path.dirname(DB_PATH) or ".", exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.execute("CREATE TABLE IF NOT EXISTS leituras (sensor_id TEXT, local TEXT, ppm REAL, pm25 REAL, ts TEXT)")
    db.execute("CREATE TABLE IF NOT EXISTS alertas (sensor_id TEXT, local TEXT, tipo TEXT, nivel TEXT, ppm REAL, pm25 REAL, ts TEXT)")
    r = conectar()
    p = r.pubsub()
    p.subscribe("leituras", "alertas")
    print(f"[historico] gravando em {DB_PATH}", flush=True)
    for msg in p.listen():
        if msg["type"] != "message":
            continue
        ev = json.loads(msg["data"])
        if msg["channel"] == "leituras":
            db.execute("INSERT INTO leituras VALUES (?,?,?,?,?)",
                       (ev["sensor_id"], ev["local"], ev["fumaca_ppm"], ev["pm25"], ev["timestamp"]))
        else:
            db.execute("INSERT INTO alertas VALUES (?,?,?,?,?,?,?)",
                       (ev["sensor_id"], ev["local"], ev["tipo"], ev["nivel"], ev["fumaca_ppm"], ev["pm25"], ev["timestamp"]))
            n = db.execute("SELECT COUNT(*) FROM alertas").fetchone()[0]
            print(f"[historico] alerta registrado (total de alertas no banco: {n})", flush=True)
        db.commit()


if __name__ == "__main__":
    main()
