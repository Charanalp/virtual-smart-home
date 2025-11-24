# 🏠 Virtual Smart Home Automation System  
A complete **real-time smart home simulation system** built using **Python, Flask, Flask-SocketIO, and Eventlet**, featuring live device control, sensor simulation, automation rules, and cloud deployment.

🔗 **Live Demo:**  
**https://virtual-smart-home.onrender.com**

🔗 **GitHub Repository:**  
**https://github.com/Charanalp/virtual-smart-home**

---

## 🚀 Project Overview
This project simulates a fully functional smart home with devices and sensors.  
It uses **WebSockets** for real-time communication between the server and frontend.

The system allows users to:
- Control **Lights**, **Fan**, **Door Lock**
- View real-time **Temperature**, **Humidity**, **Light Level**, **Motion**
- Create **Automation Rules**
- Monitor **Live Logs**
- Run entirely on the **cloud (Render.com)**

---

## 🧰 Tech Stack

### **Backend**
- Python 3  
- Flask  
- Flask-SocketIO  
- Eventlet  

### **Frontend**
- HTML5  
- CSS3  
- JavaScript (Real-time WebSocket updates)

### **Deployment**
- Render.com — Web Service  
- Gunicorn / Eventlet Worker  

---

## 📂 Folder Structure
```
virtual-smart-home/
│
├── virtual_smart_home.py      # Main backend application
├── requirements.txt           # Dependencies
├── Procfile                   # Deployment command for Render
├── static/
│   ├── style.css              # UI styling
│   └── script.js              # Frontend logic / WebSocket events
└── templates/
    └── index.html             # Main UI
```

---

## 🎯 Features

### **1. Smart Devices**
- Toggle Lights (On/Off)
- Fan Control
- Smart Door Lock (Lock/Unlock)

### **2. Real-Time Sensors**
- Temperature Sensor  
- Light Intensity Sensor  
- Motion Sensor  
- Humidity Sensor

### **3. Automation Rules Engine**
Example rules:
- Auto-turn on fan if temperature > 30°C  
- Lights on when motion detected  
- Auto-lock door after inactivity  

### **4. Live Logging**
- Sensor activity  
- Device events  
- Automation triggers  

---

## 🖥️ How to Run Locally

```bash
# Clone
git clone https://github.com/Charanalp/virtual-smart-home.git
cd virtual-smart-home

# Create & activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Or Linux/Mac
# source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Run application
python virtual_smart_home.py
```

Now open:  
➡️ http://127.0.0.1:5000/

---

## 🌐 Deployment (Render.com)

The project is deployed using Render’s **Web Service** with:

**Procfile**
```
web: python virtual_smart_home.py
```

**Render Build Command**
```
pip install -r requirements.txt
```

The app auto-runs on port:
```
PORT = os.environ.get("PORT", 10000)
``` 
---

## 🧑‍💻 Author
**Charan ALP**  
Smart Systems Developer  
GitHub: https://github.com/Charanalp  

---

## 📄 License
This project is open-source and free to use.

---

If you use this project, please give it a ⭐ on GitHub!
