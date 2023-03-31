from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    {"label":"Comprar Croissants", "done": False},
    {"label":"Ir al doctor", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)



if __name__  == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)