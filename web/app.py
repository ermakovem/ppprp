# app.py
from flask import Flask, jsonify
import datetime

app = Flask(__name__)
counter = 0

@app.route('/statistics', methods=['GET'])
def get_statistics():
    return jsonify({'time_requests_count': counter})

@app.route('/time', methods=['GET'])
def get_time():
    global counter
    counter += 1
    return jsonify({'current_time': datetime.datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
