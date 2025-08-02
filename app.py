from flask import Flask
from datetime import datetime
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/hello", methods=["GET"])
def hello():
    timestamp = datetime.now().isoformat()
    message = f"Hello world {timestamp}"
    app.logger.info(message)
    return message, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
