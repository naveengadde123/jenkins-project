import os

from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "taskflow")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "development")
PORT = int(os.getenv("PORT", "5000"))


@app.get("/")
def home():
    return jsonify({
        "app": APP_NAME,
        "status": "running",
        "version": APP_VERSION,
        "environment": APP_ENV,
        "message": "Welcome to Taskflow!"
    })


@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False)
