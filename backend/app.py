"""Flask app for the Moments frontend."""
from flask import Flask, jsonify, request
import photo_reader

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from the Flask API!"})

if __name__ == '__main__':
    photo_reader.initialize()
    app.run(debug=True)
