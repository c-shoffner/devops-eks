import json, requests
from datetime import datetime
from flask import Flask, request


app = Flask(__name__)
@app.route('/liatrio', methods=['GET'])
def liatrio():
    message = "Automate all the things!"
    timestamp = datetime.now()

    payload = json.dumps({
        "message": f"{message}",
        "timestamp": f"{timestamp}"
    })
    return payload, 200


@app.route('/', methods=['GET'])
def main():
    return "Please call /liatrio for the exercise"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
