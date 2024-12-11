from flask import Flask, request, jsonify
from Connection.Connection import PLCConnection
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Global variable to store the PLC connection and the current IP
plc = None
current_ip = None

@app.route('/connect', methods=['POST'])
def connect():
    global plc, current_ip

    # Get the IP address from the frontend
    ip_address = request.json.get("ipAddress")
    if not ip_address:
        return jsonify({"error": "IP address is required"}), 400

    try:
        # Close the existing connection if it exists
        if plc and plc.is_connected():
            plc.close_connection()

        # Create a new PLC connection
        plc = PLCConnection(ip_address)
        plc.open_connection()
        current_ip = ip_address

        return jsonify({"message": f"Connected to PLC at {ip_address}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/disconnect', methods=['POST'])
def disconnect():
    global plc, current_ip

    if plc and plc.is_connected():
        plc.close_connection()
        plc = None
        current_ip = None
        return jsonify({"message": "PLC connection closed"}), 200
    else:
        return jsonify({"message": "No active connection to close"}), 200

@app.route('/read', methods=['POST'])
def read_tag():
    global plc

    if not plc or not plc.is_connected():
        return jsonify({"error": "No active PLC connection"}), 400

    tag_name = request.json.get("tagName")
    if not tag_name:
        return jsonify({"error": "Tag name is required"}), 400

    try:
        tag_name, value, status = plc.read_tag(tag_name)
        return jsonify({"tag": tag_name, "value": value, "status": status}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
