from flask import Flask, request, json
from flask import jsonify
import json 

app = Flask(__name__)

@app.route('/AVFinal', methods=['GET'])
def home():
    return "Hello, Flask!"

@app.route('/', methods=['POST'])
def info_nome():
    return ""

@app.route('/', methods=['PUT'])
def info_nome():
    return ""

@app.route('/', methods=['DELETE'])
def info_nome():
    return ""

    app.run()

    