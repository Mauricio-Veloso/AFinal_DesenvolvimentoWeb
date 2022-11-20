from flask import Flask, request, json
from flask import jsonify
import json 

app = Flask(__name__)

@app.route('/AVFinal', methods=['GET'])
def home():
    return "Hello, Flask!"

@app.route('/get', methods=['GET'])
def get():
    return "Implementação do metodo GET"

@app.route('/post', methods=['POST'])
def post():
    return "Implementação do metodo POST"

@app.route('/put', methods=['PUT'])
def put():
    return "Implementação do metodo PUT"

@app.route('/delete', methods=['DELETE'])
def delete():
    return "Implementação do metodo DELETE"

    app.run()

    