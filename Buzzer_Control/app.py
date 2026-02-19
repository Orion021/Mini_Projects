from flask import Flask, jsonify, send_from_directory 
from gpiozero import OutputDevice 
 
# GPIO17 (Pin 11), active_low=True means .on() pulls pin low (buzzer ON) 
buzzer = OutputDevice(17, active_high=False, initial_value=False) 
 
app = Flask(__name__, static_folder="static") 
 
@app.route("/api/on") 
def api_on(): 
    buzzer.on()   # drives pin LOW → buzzer ON 
    return jsonify({"status": "ON"}) 
 
@app.route("/api/off") 
def api_off(): 
    buzzer.off()  # drives pin HIGH → buzzer OFF 
    return jsonify({"status": "OFF"}) 
 
@app.route("/") 
def index(): 
    return send_from_directory("static", "index.html") 
 
if __name__ == "__main__": 
    # accessible from other devices on the LAN 
    app.run(host="0.0.0.0", port=5000) 