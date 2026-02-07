# Placeholder for main.py
import os
import time
import psycopg2
from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="Cloud Reliability Platform API")

REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["path", "method", "status"])
LATENCY = Histogram("http_request_duration_seconds", "Request latency", ["path"])

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppass")


def db_ok() -> bool:
    try:
        conn = psycopg2.connect(
            host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, connect_timeout=2
        )
        conn.close()
        return True
    except Exception:
        return False


@app.get("/")
def root():
    return {"service": "Cloud Reliability Platform API", "docs": "/docs", "health": "/healthz", "ready": "/readyz"}


@app.get("/healthz")
def healthz():
    REQUESTS.labels(path="/healthz", method="GET", status="200").inc()
    return {"status": "ok"}


@app.get("/readyz")
def readyz(response: Response):
    ok = db_ok()
    status = "ok" if ok else "db_not_ready"
    code = 200 if ok else 503
    REQUESTS.labels(path="/readyz", method="GET", status=str(code)).inc()
    response.status_code = code
    return {"status": status}


@app.get("/api/tasks")
def tasks():
    start = time.time()
    try:
        # simple DB query
        conn = psycopg2.connect(
            host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, connect_timeout=2
        )
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, title TEXT NOT NULL);")
        cur.execute("SELECT id, title FROM tasks ORDER BY id DESC LIMIT 20;")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        LATENCY.labels(path="/api/tasks").observe(time.time() - start)
        REQUESTS.labels(path="/api/tasks", method="GET", status="200").inc()
        return {"tasks": [{"id": r[0], "title": r[1]} for r in rows]}
    except Exception as e:
        LATENCY.labels(path="/api/tasks").observe(time.time() - start)
        REQUESTS.labels(path="/api/tasks", method="GET", status="500").inc()
        return {"error": str(e)}


@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)
