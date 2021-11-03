# no terminal dar o comando pip install paho-mqtt

# importar bibliotecas 
import paho.mqtt.client as mqtt
import sys
import RPi.GPIO as GPIO
import time

# configurações do MQTT
Broker = "test.mosquitto.org"
PortaBroker = 1883
KeepAliveBroker = 60
TopicoSubscribe = "cm031121"

# Função para conexão com o broker
def on_connect(client, userdata, flags, rc):
    print('[STATUS] Conectando ao Broker, Resultado: ', + str(rc))
    # Increver no tópico configurado
    cliente.subscribe(TopicoSubscribe)
    
    


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print "LED on"
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(18,GPIO.LOW)