# small helpers
import json, os

def ensure_data():
    os.makedirs('data', exist_ok=True)

def load_json(path):
    with open(path) as f:
        return json.load(f)
