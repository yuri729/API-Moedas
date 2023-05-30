from flask import Flask, jsonify, request

app = Flask(__name__)

moeda = [
{
    "USDBRL": {
        "code": "USD",
        "codein": "BRL",
        "name": "Dólar Americano/Real Brasileiro",
        "high": "5.734",
        "low": "5.7279",
        "varBid": "-0.0054",
        "pctChange": "-0.09",
        "bid": "5.7276",
        "ask": "5.7282",
        "timestamp": "1618315045",
        "create_date": "2021-04-13 08:57:27"
    },
    "EURBRL": {
        "code": "EUR",
        "codein": "BRL",
        "name": "Euro/Real Brasileiro",
        "high": "6.8327",
        "low": "6.8129",
        "varBid": "-0.0069",
        "pctChange": "-0.1",
        "bid": "6.8195",
        "ask": "6.822",
        "timestamp": "1618315093",
        "create_date": "2021-04-13 08:58:15"
    },
    "BTCBRL": {
        "code": "BTC",
        "codein": "BRL",
        "name": "Bitcoin/Real Brasileiro",
        "high": "360000",
        "low": "340500",
        "varBid": "17072.9",
        "pctChange": "4.98",
        "bid": "359973.9",
        "ask": "359974",
        "timestamp": "1618315092",
        "create_date": "2021-04-13 08:58:12"
    }
}
]

#Consultar moedas (todos)
@app.route('/moeda',methods=['GET'])
def obter_moeda():
    return jsonify(moeda)

#Consultar moeda por (id)
@app.route('/moeda/<string:code>',methods=['GET'])
def obter_moeda_id(code):
    for moedas_id in moeda:
        if moedas_id.get('code') == code:
            return jsonify(moedas_id)
     
app.run(port=5000, host='localhost', debug=True)