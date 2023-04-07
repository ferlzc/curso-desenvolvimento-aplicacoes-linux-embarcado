#!/usr/bin/env python3
from flask import Flask

#TODO - incluir biblioteca para manipular GPIO, ex: https://pythonhosted.org/python-periphery/

app = Flask(__name__)

#TODO - configuar qual eh o GPIO para LED1 ?


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/led1on')
def led1On():
    #TODO - fazer GPIO ON
    return 'LED1 - ON'

@app.route('/led1off')
def led1Off():
    #TODO - fazer GPIO OFF
    return 'LED1 - OFF'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
