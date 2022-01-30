from flask import Flask, jsonify, request
app = Flask(__name__)
import json

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    { "label": "My third task", "done": True }
]


@app.route('/', methods=['GET'])
def hello():
    return '<h1>Hello!</h1>'

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    new_todo_list = todos + [request_body]
    return jsonify(new_todo_list)
    
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete(position):
    del todos[position]
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)