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

# Synthetic test credential for Gitleaks validation only
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
