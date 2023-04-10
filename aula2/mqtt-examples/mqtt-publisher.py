#!/usr/bin/env python3
import paho.mqtt.client as mqtt
from time import sleep
import platform,sys

BROKER_ADDRESS = "test.mosquitto.org"
TOPIC = "Treinamento-Linux"


client = mqtt.Client()

if client.connect(BROKER_ADDRESS, 1883, 60) != 0:
    sys.exit("Falha na conexão com o broker!")

print("CTRL C para sair")

while True:
    client.publish(TOPIC, f"Sistema: {platform.system()}")
    sleep(0.75)
    client.publish(TOPIC, f"Processador: {platform.processor()}")
    sleep(0.75)
    client.publish(TOPIC, f"Arquitetura: {platform.architecture()[0]}")
    sleep(0.75)