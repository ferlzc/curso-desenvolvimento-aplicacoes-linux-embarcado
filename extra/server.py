#!/usr/bin/env python3
from flask import Flask
# para manipular LED vamos utilizar a biblioteca - https://github.com/vsergeev/python-periphery
from periphery import LED

app = Flask(__name__)

#Configura LED_ACT como LED de saída - led0
ledACT = LED("led0", False)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/led1on')
def led1On():
    ledACT.write(1)
    return 'LED1 - ON'

@app.route('/led1off')
def led1Off():
    ledACT.write(0)
    return 'LED1 - OFF'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    ledACT.close()
