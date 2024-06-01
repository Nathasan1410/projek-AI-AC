from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error




app = Flask(__name__)

# Load and preprocess the data
data = pd.read_csv('data_ai_2.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'])
data = data.sort_values(by='timestamp').reset_index(drop=True)
data['desired_temperature'] = 25

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    current_temp = float(request.form['current_temp'])
    current_humidity = float(request.form['current_humidity'])
    current_ac_temp = float(request.form['current_ac_temp'])
    desired_temp = float(request.form['desired_temp'])
    current_hour = int(request.form['current_hour'])

    sample_data = pd.DataFrame([[current_temp, current_humidity, current_ac_temp, desired_temp, current_hour]], columns=features_time)

    predict_waktu = model_time.predict(sample_data)
    predict_waktu = np.maximum(predict_waktu, 0)

    predict_ac = model_ac.predict(sample_data)
    predict_ac = np.maximum(predict_ac, 0)

    return render_template('result.html', predict_waktu=predict_waktu[0], predict_ac=predict_ac[0])

if __name__ == '__main__':
    app.run(debug=True)






