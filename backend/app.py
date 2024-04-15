from flask import Flask, jsonify, request

app = Flask(__name__)

# Example of a simple route that returns a static message
@app.route('/')
def home():
    return jsonify({"message": "Hello from the Flask API!"})

# Example of a route that could return data (e.g., list of items)
@app.route('/items', methods=['GET'])
def get_items():
    items = [{"id": 1, "name": "Item One"}, {"id": 2, "name": "Item Two"}]
    return jsonify(items)

# Example of a route to get a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    items = [{"id": 1, "name": "Item One"}, {"id": 2, "name": "Item Two"}]
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Example of a route to create a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    new_item = {"id": len(data) + 1, "name": data['name']}
    # Normally, you would insert the new item into a database.
    return jsonify(new_item), 201

# Example of a route to update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    # Here, you would normally update the item in a database.
    updated_item = {"id": item_id, "name": data['name']}
    return jsonify(updated_item)

# Example of a route to delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    # Normally, you would delete the item from a database here.
    return jsonify({"success": True}), 204

if __name__ == '__main__':
    app.run(debug=True)
