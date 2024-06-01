# from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import json

import random

from paho.mqtt import client as mqtt_client

client_id = f'python-mqtt-{random.randint(0, 1000)}'
# MQTT broker configuration
broker = "broker.emqx.io"  # Public MQTT broker for testing, you can replace it with your broker address
port = 1883
topic = "projek_AI"  # The topic you want to subscribe to

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# def publish(client: mqtt_client, message: str, topic: str):
#     result = client.publish(topic, message)
#     status = result[0]
#     if status == 0:
#         print(f"Sent `{message}` to topic `{topic}`")
#     else:
#         print(f"Failed to send message to topic {topic}")

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        dicti = json.loads(msg.payload.decode())
        temp = (dicti['temperature'])
        humid = (dicti['humidity'])
        current_hour = (dicti['current_hour'])
        desired_temp= (dicti['desired_temp'])
        current_ac_temp = (dicti['current_ac_temp'])
        ac = predict_ac(temp, humid, current_hour, desired_temp, current_ac_temp)
        waktu = predict_waktu(temp, humid, current_hour, desired_temp, current_ac_temp)
        client.publish('projekAI/AC', str(ac) )
        client.publish('projekAI/waktu', str(waktu) )
    
    client.subscribe(topic)
    client.on_message = on_message

def calculate_time_to_reach(data):
    time_to_reach = []
    for i in range(len(data)):
        current_time = data['timestamp'][i]
        current_temp = data['temperature'][i]
        desired_temp = data['desired_temperature'][i]
        
        future_data = data[i:]
        target_time = future_data[future_data['temperature'] <= desired_temp]['timestamp']
        
        if not target_time.empty:
            time_diff = (target_time.iloc[0] - current_time).total_seconds() / 60
            time_to_reach.append(time_diff)
        else:
            time_to_reach.append(np.nan)

    return time_to_reach

# Load and preprocess the data
data = pd.read_csv('data_ai_2.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'])
data = data.sort_values(by='timestamp').reset_index(drop=True)
data['desired_temperature'] = 25


data['time_to_reach'] = calculate_time_to_reach(data)
data = data.dropna(subset=['time_to_reach'])
data['hour'] = data['timestamp'].dt.hour

features_time = ['temperature', 'humidity', 'suhu_ac', 'desired_temperature', 'hour']
X_time = data[features_time]
y_time = data['time_to_reach']

features_ac = ['temperature', 'humidity', 'suhu_ac', 'desired_temperature', 'hour']
X_ac = data[features_ac]
y_ac = data['suhu_ac']

X_time_train, X_time_test, y_time_train, y_time_test = train_test_split(X_time, y_time, test_size=0.2, random_state=42)
X_ac_train, X_ac_test, y_ac_train, y_ac_test = train_test_split(X_ac, y_ac, test_size=0.2, random_state=42)

model_time = LinearRegression()
model_time.fit(X_time_train, y_time_train)

model_ac = LinearRegression()
model_ac.fit(X_ac_train, y_ac_train)


def predict_ac(temp, humid, hour, desired, current):
    current_temp = float(temp)
    current_humidity = float(humid)
    current_ac_temp = float(hour)
    desired_temp = float(desired)
    current_hour = int(current)

    sample_data = pd.DataFrame([[current_temp, current_humidity, current_ac_temp, desired_temp, current_hour]], columns=features_time)

    predict_ac = model_ac.predict(sample_data)
    predict_ac = np.maximum(predict_ac, 0)

    predict_ac=predict_ac[0]

    return predict_ac

def predict_waktu(temp, humid, hour, desired, current):
    current_temp = float(temp)
    current_humidity = float(humid)
    current_ac_temp = float(hour)
    desired_temp = float(desired)
    current_hour = int(current)

    sample_data = pd.DataFrame([[current_temp, current_humidity, current_ac_temp, desired_temp, current_hour]], columns=features_time)

    predict_waktu = model_time.predict(sample_data)
    predict_waktu = np.maximum(predict_waktu, 0)

    predict_waktu=predict_waktu[0]

    return predict_waktu


def run():
    client = connect_mqtt()
    subscribe(client)
    # publish(client)
    client.loop_forever()
    
if __name__ == '__main__':
    run()