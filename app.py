from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/sensor-data')
def sensor_data():
   # Replace these random values with actual sensor readings
    data = {
        'temperature': round(random.uniform(10, 40), 2),  # Random temperature between 10°C and 40°C
        'humidity': round(random.uniform(0, 100), 2),      # Random humidity between 0% and 100%
        'water_level': round(random.uniform(0, 100), 2),   # Random water level between 0 and 100
        'ph_level': round(random.uniform(0, 14), 2),       # Random pH level between 0 and 14
        'light': round(random.uniform(0, 1000), 2),        # Random light level between 0 and 1000
        'nutrients_level': round(random.uniform(0, 100), 2) # Random nutrients level between 0 and 100
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
