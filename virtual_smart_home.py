from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# ---------------------------
# Smart Home Device States
# ---------------------------
devices = {
    "light": False,
    "fan": False,
    "door": "Locked",
    "temperature": 25
}

# ---------------------------
# FRONTEND HTML UI
# ---------------------------
html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Virtual Smart Home</title>
    <style>
        body { 
            font-family: Arial; 
            background: #f1f1f1; 
            text-align: center; 
            padding: 30px; 
        }
        .card {
            background: white;
            padding: 20px;
            width: 300px;
            margin: auto;
            margin-top: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px #ccc;
        }
        button {
            padding: 10px 20px;
            margin: 10px;
            border: none;
            background: #4CAF50;
            color: white;
            border-radius: 5px;
        }
        .danger {
            background: red;
        }
    </style>
</head>

<body>

<h1>🏠 Virtual Smart Home</h1>
<h3>Control your devices in real-time</h3>

<div class="card">
    <h2>💡 Light</h2>
    <p id="light-status">Status: OFF</p>
    <button onclick="toggleDevice('light')">Toggle Light</button>
</div>

<div class="card">
    <h2>🌀 Fan</h2>
    <p id="fan-status">Status: OFF</p>
    <button onclick="toggleDevice('fan')">Toggle Fan</button>
</div>

<div class="card">
    <h2>🚪 Door</h2>
    <p id="door-status">Status: Locked</p>
    <button onclick="toggleDevice('door')">Lock/Unlock</button>
</div>

<div class="card">
    <h2>🌡 Temperature Sensor</h2>
    <p id="temp-status">Temperature: 25 °C</p>
    <button onclick="increaseTemp()">Increase</button>
    <button class="danger" onclick="decreaseTemp()">Decrease</button>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.5.4/socket.io.min.js"></script>
<script>
    var socket = io();

    socket.on("update", function(data) {
        document.getElementById("light-status").innerHTML = "Status: " + (data.light ? "ON" : "OFF");
        document.getElementById("fan-status").innerHTML = "Status: " + (data.fan ? "ON" : "OFF");
        document.getElementById("door-status").innerHTML = "Status: " + data.door;
        document.getElementById("temp-status").innerHTML = "Temperature: " + data.temperature + " °C";
    });

    function toggleDevice(device) {
        socket.emit("toggle", device);
    }

    function increaseTemp() {
        socket.emit("temp_change", "increase");
    }

    function decreaseTemp() {
        socket.emit("temp_change", "decrease");
    }
</script>

</body>
</html>
"""

# ---------------------------
# BACKEND API
# ---------------------------
@app.route("/")
def home():
    return render_template_string(html_page)

@socketio.on("toggle")
def toggle_device(device):
    if device in devices:
        if device == "door":
            devices["door"] = "Unlocked" if devices["door"] == "Locked" else "Locked"
        else:
            devices[device] = not devices[device]

    emit("update", devices, broadcast=True)

@socketio.on("temp_change")
def change_temp(action):
    if action == "increase":
        devices["temperature"] += 1
    elif action == "decrease":
        devices["temperature"] -= 1

    emit("update", devices, broadcast=True)

# ---------------------------
# RUN SERVER
# ---------------------------
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)

