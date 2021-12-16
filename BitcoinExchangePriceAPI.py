from flask import Flask,jsonify,request
from flask_restful import reqparse
from gevent.pywsgi import WSGIServer
import requests
import json

app = Flask(__name__)

@app.route("/api/exchange")
def hello_world():
    parser=reqparse.RequestParser()
    parser.add_argument('from_currency', type=str)
    parser.add_argument('to_currency', type=str)
    parser.add_argument('amount', type=float)
    values=parser.parse_args()
    #return jsonify(values["from_currency"])
    
    x = requests.get('https://blockchain.info/ticker')
    convertion_values = json.loads(x.text)
    if values["from_currency"]=="BTC":
        return jsonify(convertion_values[values["to_currency"]]["last"]*values["amount"])
    else:
        value_for_one=1/convertion_values[values["from_currency"]]["last"]
        return jsonify(value_for_one*values["amount"])

if __name__ == '__main__':
    http_server = WSGIServer(('',5000),app)
    http_server.serve_forever()