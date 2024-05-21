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
    response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
    data = response.json()
    return jsonify({'datetime': data['datetime']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
