from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify({
        "application": "Secure Pipeline Lab",
        "status": "running"
    })


@app.get("/healthz")
def healthz():
    return jsonify({"status": "healthy"}), 200
