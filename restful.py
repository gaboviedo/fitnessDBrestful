from flask import Flask, jsonify, request

app = Flask(_name_)

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<string:name>', methods=['GET'])
def get_item(name):
    item = next((item for item in items if item['name'] == name), None)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item = {'name': data['name'], 'price': data['price']}
    items.append(item)
    return jsonify(item), 201

@app.route('/items/<string:name>', methods=['PUT'])
def update_item(name):
    data = request.get_json()
    item = next((item for item in items if item['name'] == name), None)
    if item:
        item.update(data)
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

@app.route('/items/<string:name>', methods=['DELETE'])
def delete_item(name):
    global items
    items = [item for item in items if item['name'] != name]
    return jsonify({'message': 'Item deleted'})

if _name_ == '_main_':
    app.run(debug=True)