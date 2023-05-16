
from fastapi import FastAPI
import paho.mqtt.client as mqtt
import random
import time

pub = FastAPI()

brokerAddress = "broker.hivemq.com"
userName = "vasavi"
passWord = "Chinnu@123"
topic = "Sensor/Temperature/TMP36"
min_temp = 20
max_temp = 30

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set(userName, passWord)
client.connect(brokerAddress, 8883)

# Publish Temperature Data
wait = 20
while True:
    data = random.randint(min_temp, max_temp)
    print(data)

    
@pub.get("/")
def read_root():
    return {"Hello": "MQTT FastAPI"}

@pub.get("/get_variable")
def read_variable():
    return {"value": data.get_value()}

@pub.post("/publish")
def publish_temperature():
    client.publish(topic, data)
    return {"message": "Temperature data published"}

# Run the MQTT client loop in a background thread
client.loop_start()

# Sleep to allow the client to establish a connection
time.sleep(0.1)


***********

from fastapi import FastAPI
import paho.mqtt.client as mqtt
import random
import time

app = FastAPI()

brokerAddress = "broker.hivemq.com"
userName = "vasavi"
passWord = "Chinnu@123"
topic = "Sensor/Temperature/TMP36"
min_temp = 20
max_temp = 30
data = None

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set(userName, passWord)
client.connect(brokerAddress, 8883)

# Publish Temperature Data
wait = 20
def publish_data():
    global data
    while True:
        data = random.randint(min_temp, max_temp)
        client.publish(topic, data)
        print(data)
        time.sleep(wait)

# Run the MQTT client loop in a background thread
client.loop_start()

# Sleep to allow the client to establish a connection
time.sleep(0.1)

@app.get("/")
def read_root():
    return {"Hello": "MQTT FastAPI"}

@app.get("/get_variable")
def read_variable():
    global data
    return {"value": data}

@app.post("/publish")
def publish_temperature():
    global data
    client.publish(topic, str(data))
    return {"message": "Temperature data published"}

# Start publishing data in a separate thread
publish_thread = threading.Thread(target=publish_data)
publish_thread.start()


