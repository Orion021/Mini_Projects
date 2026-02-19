import time 
from flask import Flask, jsonify, send_from_directory 
import board 
import adafruit_dht 
 
# Initialize DHT11 on GPIO4 (physical pin 7) 
sensor = adafruit_dht.DHT11(board.D4) 
 
# Create Flask app 
app = Flask(__name__, static_folder="static") 
 
# Route for getting the sensor data 
@app.route("/api/data") 
def get_data(): 
    try: 
        temperature = sensor.temperature 
        humidity = sensor.humidity 
    except Exception: 
        # If reading fails, just return None 
        temperature = None 
        humidity = None 
 
    return jsonify({ 
        "temperature": temperature, 
        "humidity": humidity, 
        "time": time.strftime("%I:%M:%S %p") 
    }) 
 
# Route for the main webpage 
@app.route("/") 
def home(): 
    return send_from_directory("static", "index.html") 
 
# Run the Flask server 
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000) 
