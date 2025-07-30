from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

static_dir = os.environ.get('FLASK_STATIC_FOLDER', 'static')

app = Flask(__name__, static_folder=static_dir, static_url_path='/')
CORS(app)

# Serve frontend
@app.route('/')
@app.route('/<path:path>')
def serve_react(path=''):
    file_path = os.path.join(app.static_folder, path)
    if path != "" and os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# Example API route
@app.route('/api/hello')
def hello():
    return jsonify(message="Hello from Flask backend!")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
