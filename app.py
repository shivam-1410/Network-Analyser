from flask import Flask, render_template, jsonify
import json, os

app = Flask(__name__, template_folder='templates', static_folder='static')

DATA_SUMMARY = os.path.join('data','summary.json')
DATA_PACKETS = os.path.join('data','packets.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/summary')
def summary():
    if not os.path.exists(DATA_SUMMARY):
        return jsonify({'error':'summary not found'}), 404
    with open(DATA_SUMMARY) as f:
        return jsonify(json.load(f))

@app.route('/api/packets')
def packets():
    if not os.path.exists(DATA_PACKETS):
        return jsonify([]), 404
    with open(DATA_PACKETS) as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    app.run(debug=True)
