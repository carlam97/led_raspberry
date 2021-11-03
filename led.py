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

# Função para receber mensagem
def on_message(client, userdata, msg):
    MensagemRecebida = str(msg.payload)
    print("[MSG RECEBIDA] Topico: "+ msg.topic+" / Mensagem: "+ MensagemRecebida)
    
# Programa Principal
try: 
  print("[STATUS] Iniciando o MQTT...")

  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message

  # Conexão
  client.connect(Broker, PortaBroker, KeepAliveBroker)
  client.loop_forever()
except KeyboardInterrupt:
  print("Ctrl+C pressionado, encerrando a aplicação")
  sys.exit(0)

# código para acender e apagar led usando raspberry

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(18,GPIO.OUT)
#print "LED on"
#GPIO.output(18,GPIO.HIGH)
#time.sleep(1)
#print "LED off"
#GPIO.output(18,GPIO.LOW)