from flask import Flask, request, jsonify
from flask_cors import CORS
from pylogix import PLC

app = Flask(__name__)
CORS(app)

@app.route('/discover', methods=['POST'])
def discover():
    print("I AM RUNNING")
    try:
        with PLC() as comm:
            devices = comm.Discover()
            
            if not devices.Value:
                return jsonify({"error": "No devices found"}), 404
            
            # Convert each field to a single string value
            device_list = [
                {
                    "IPAddress": device.IPAddress,
                    "ProductCode": device.ProductCode,
                    "Vendor": device.Vendor,
                    "DeviceID": device.DeviceID,
                    "Revision": device.Revision,
                    "SerialNumber": device.SerialNumber,
                    "ProductName": device.ProductName,
                    "State": device.State,
                }
                for device in devices.Value
            ]
            
            return jsonify(device_list), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/tags', methods=["POST"])
def tags():
    print("TAGS IS RUNNING")
    ip_address = request.json.get("ip_address")
    if not ip_address:
         return jsonify({"error": "IP address has an error"}), 400
    with PLC() as comm:
        comm.IPAddress = ip_address
        tags = comm.GetTagList()
        if not tags.Value:
            return jsonify({"error": "No devices found"}), 404
        tag_list = [
            {
                "TagName": tag.TagName,
                "InstanceID": tag.InstanceID,
                "SymbolType": tag.SymbolType,
                "DataTypeValue": tag.DataTypeValue,
                "DataType": tag.DataType,
                "Array": tag.Array,
                "Struct": tag.Struct,
                "Size": tag.Size,
                "AccessRight": tag.AccessRight,
                "Internal": tag.Internal,
                "Meta": tag.Meta,
                "Scope0": tag.Scope0,
                "Scope1": tag.Scope1,
                "Bytes": tag.Bytes,
            }
            for tag in tags.Value
        ]

        return jsonify(tag_list), 200


@app.route('/readBool', methods=["POST"])
def readBool():
    print("READ BOOL IS RUNNING")
    ip_address = request.json.get("ip_address")
    if not ip_address:
         return jsonify({"error": "IP address has an error"}), 400
    tag_name = request.json.get("tag_name")
    if not tag_name:
         return jsonify({"error": "Tag name has an error"}), 400
    print(ip_address)
    print(tag_name)
    with PLC() as comm:
        comm.IPAddress = ip_address
        readValue = comm.Read(tag_name)
        print(readValue)
    return jsonify(readValue.Value), 200


if __name__ == '__main__':
    app.run(debug=True)



# # Global variable to store the PLC connection and the current IP
# plc = None
# current_ip = None

# @app.route('/connect', methods=['POST'])
# def connect():
#     global plc, current_ip

#     # Get the IP address from the frontend
#     ip_address = request.json.get("ipAddress")
#     if not ip_address:
#         return jsonify({"error": "IP address is required"}), 400

#     try:
#         # Close the existing connection if it exists
#         if plc and plc.is_connected():
#             plc.close_connection()

#         # Create a new PLC connection
#         plc = PLCConnection(ip_address)
#         plc.open_connection()
#         current_ip = ip_address

#         return jsonify({"message": f"Connected to PLC at {ip_address}"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500





