from flask import Flask,jsonify

import os
import socket


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the Flask app!",
        "hostname": socket.gethostname(),
        "environment": os.getenv("FLASK_ENV", "development")
    })
@app.route('/health', methods=['GET'])
def health():
    return jsonify({ "status": "healthy", }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)