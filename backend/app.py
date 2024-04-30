from flask import Flask, jsonify, request
import photo_reader

app = Flask(__name__)

# Example of a simple route that returns a static message
@app.route('/')
def home():
    return jsonify({"message": "Hello from the Flask API!"})

if __name__ == '__main__':
    photo_reader.initialize()
    app.run(debug=True)
