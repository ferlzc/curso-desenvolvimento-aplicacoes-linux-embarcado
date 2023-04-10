#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import sys

BROKER_ADDRESS = "test.mosquitto.org"
TOPIC = "Treinamento-Linux"


def on_connect(client, userdata, flags, rc):
    print("Resultado da conexão: " + str(rc))
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    print(msg.topic + " - " + msg.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

if client.connect(BROKER_ADDRESS, 1883, 60) != 0:
    sys.exit("Falha na conexão com o broker!")

print("CTRL C para sair")

try:
    client.loop_forever()
except:
    client.disconnect()