import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello from Koyeb", 200


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
