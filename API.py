from flask import Flask, request, jsonify

app = Flask(_name_)

users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]), 200
    return jsonify({"message": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"message": "Invalid data"}), 400
    user_id = len(users) + 1
    users[user_id] = {
        "id": user_id,
        "name": data['name'],
        "email": data['email']
    }
    return jsonify({"message": "User created successfully", "user": users[user_id]}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
 return jsonify({"message": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted successfully"}), 200

if _name_ == '_main_':
    app.run(debug=True)