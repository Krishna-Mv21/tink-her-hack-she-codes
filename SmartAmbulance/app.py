import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# In-memory storage for active emergencies (mock database)
active_emergencies = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def user_view():
    return render_template('user.html')

@app.route('/driver')
def driver_view():
    tomtom_api_key = os.environ.get('TOMTOM_API_KEY', '')
    return render_template('driver.html', tomtom_api_key=tomtom_api_key)

@app.route('/api/sos', methods=['POST'])
def trigger_sos():
    data = request.json
    phone = data.get('phone', 'Unknown')
    lat = data.get('lat')
    lng = data.get('lng')
    
    if lat and lng:
        emergency_id = len(active_emergencies) + 1
        active_emergencies[emergency_id] = {
            'phone': phone,
            'lat': lat,
            'lng': lng,
            'status': 'pending'
        }
        return jsonify({"success": True, "message": "SOS received", "emergency_id": emergency_id})
    return jsonify({"success": False, "message": "Location missing"}), 400

@app.route('/api/location', methods=['GET'])
def get_locations():
    return jsonify({"emergencies": active_emergencies})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
