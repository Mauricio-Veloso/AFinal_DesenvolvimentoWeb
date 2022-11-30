# Aluno: Mauricio Garcia Veloso Junior
# Matricula: 64224115
from flask import Flask

app = Flask(__name__)

#Método GET, implementado para receber informações.
@app.route('/reserva', methods=['GET']) 
def get():
    
    return "Sua reserva está confirmada."

#Método Post, implementado para enviar informações.
@app.route('/reserva', methods=['POST']) 
def post():
    return "Obrigado por nos escolher, sua reserva foi efetuada."

#Método Post, implementado para enviar informações.
@app.route('/reserva', methods=['PUT']) 
def put():
    return "As alterações da sua reserva foram bem-sucedidas."

#Método DELETE, implementado para deletar informações.
@app.route('/reserva', methods=['DELETE']) 
def delete():
    return "O cancelamento da sua reserva foi efetuado, tenha um bom dia."

app.run()

    