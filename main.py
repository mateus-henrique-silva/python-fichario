import paho.mqtt.client as mqtt
import json
import time

# Configuração do Fichar.io
broker_address = "mqtt.fichar.io"
broker_port = 1883
username = "magtash"
password = "Mateushenrique5@"
device_id = "651c401d07cf75e75508c2a3"
topic = f"{username}/{device_id}"

# Configuração do cliente MQTT
client = mqtt.Client()

# Define usuário e senha para autenticação
client.username_pw_set(username, password)

# Conecta ao broker MQTT do Fichar.io
client.connect(broker_address, broker_port)

# Função de callback para conexão bem-sucedida
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker MQTT do Fichar.io")

# Função de callback para publicação bem-sucedida
def on_publish(client, userdata, mid):
    print("Dados enviados para o Fichar.io")

# Configura as funções de callback
client.on_connect = on_connect
client.on_publish = on_publish

# Inicia o loop MQTT
client.loop_start()

# Função para enviar dados para o Fichar.io
def enviar_para_fichar(valor):
    # Cria um dicionário com os dados a serem enviados
    dados = {
        "timestamp": int(time.time()),
        "unique_id": device_id,
        "format": "fichario",
        "dev_info": {},
        "payload": {
            "variavel_1": {
                "val": valor,
                "unt": "graus",
                "min": 0.0,
                "max": 50.0,
                "trg": 0
            }
        }
    }
    # Converte o dicionário para uma string JSON
    json_data = json.dumps(dados)
    # Publica a mensagem no tópico do Fichar.io
    client.publish(topic, json_data)

# Chama a função para enviar dados
enviar_para_fichar(25.5)

# Aguarda um momento para concluir a transmissão
time.sleep(1)

# Interrompe o loop MQTT e desconecta
client.loop_stop()
client.disconnect()
