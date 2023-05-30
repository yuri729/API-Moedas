from flask import Flask, jsonify, request

app = Flask(__name__)

moeda = [
{
    'id': 1,
    'Titulo': 'Imperador',
    'autor': 'Yuri'
},
{  
    'id': 2,
    'Titulo': 'Rei',
    'autor': 'Andre'
},
]

#Consultar moedas (todos)
@app.route('/moeda',methods=['GET'])
def obter_moeda():
    return jsonify(moeda)

#Consultar moeda por (id)
@app.route('/moeda/<string:autor>',methods=['GET'])
def obter_moeda_id(autor):
    for moedas_id in moeda:
        if moedas_id.get('autor') == autor:
            return jsonify(moedas_id)
     
app.run(port=5000, host='localhost', debug=True)
