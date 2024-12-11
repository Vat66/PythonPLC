from flask import Flask, request, jsonify
from Connection.Connection import PLCConnection

app = Flask(__name__)

# Allow requests from your front-end
from flask_cors import CORS
CORS(app)

# Initialize PLC connection
plc = PLCConnection("192.168.100.103")

@app.route('/connect', methods=['POST'])
def connect():
    try:
        plc.open_connection()
        return jsonify({"message": "PLC connection opened"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/disconnect', methods=['POST'])
def disconnect():
    try:
        plc.close_connection()
        return jsonify({"message": "PLC connection closed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/read', methods=['POST'])
def read_tag():
    try:
        tag_name = request.json.get("tagName")
        tag_name, value, status = plc.read_tag(tag_name)
        return jsonify({"tag": tag_name, "value": value, "status": status}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/write', methods=['POST'])
def write_tag():
    try:
        tag_name = request.json.get("tagName")
        value = request.json.get("value")
        status = plc.write_tag(tag_name, value)
        return jsonify({"tag": tag_name, "status": status}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
