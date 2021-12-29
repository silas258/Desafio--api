from flask import Flask
app = Flask(__name__)

@app.route("/")
def cadastro():

  cadastro = {
              "nome": "silas",
              "idade": 23,
              "telefone": "(13) 988755445", 
              "status_code": 200                 
             }         

  return cadastro
