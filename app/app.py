import json, requests
from datetime import datetime
from flask import Flask, request


app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello_world():
    message = "Hello World"
    timestamp = datetime.now().timestamp()

    payload = json.dumps({
        "message": f"{message}",
        "timestamp": f"{timestamp}"
    })
    return payload, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
