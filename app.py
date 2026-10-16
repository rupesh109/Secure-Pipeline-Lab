from flask import flask, jsonify

app = Flask(__name__)

@app.get("/healthz")
def.healthz():
    return jsonify(status="ok")
if  __name__ == "__main__":
     app.run(host = "o.o.o.o", port=8000) 

