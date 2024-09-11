from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/posts"

@app.route('/items', methods=['GET'])
def get():
    response = requests.get(JSONPLACEHOLDER_URL)
    return jsonify(response.json())

@app.route('/items/<int:id>', methods=['GET'])
def get_id(id):
     response = requests.get(f"{JSONPLACEHOLDER_URL}/{id}")
     return jsonify(response.json())

@app.route('/items', methods=['POST'])
def create():
    new_post = request.json
    response = requests.post(JSONPLACEHOLDER_URL, json=new_post)
    return jsonify(response.json()), response.status_code

@app.route('/items/<post_id>', methods=['PUT'])
def update(post_id):
     update_post = request.json
     response = requests.put(f"{JSONPLACEHOLDER_URL}/{post_id}", json=update_post)
     return jsonify(response.json()), response.status_code

@app.route('/items/<post_id>', methods=['DELETE'])
def delete_post(post_id):
     response = requests.delete(f"{JSONPLACEHOLDER_URL}/{post_id}")
     return jsonify({"message": "Post deletado"}), 204

if __name__ == '__main__':
    app.run(debug=True)
