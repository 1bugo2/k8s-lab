import os
import redis
from flask import Flask, request

app = Flask(__name__)

# Redis connection (Docker service name)
r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.route("/")
def home():
    return {"message": "API is running"}

@app.route("/set")
def set_value():
    r.set("hello", "world")
    return {"status": "stored"}

@app.route("/get")
def get_value():
    value = r.get("hello")
    return {"value": value}

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True)
    return {
        "you_sent": data,
        "status": "ok"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)