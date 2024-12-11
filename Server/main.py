from Connection.Connection import PLCConnection
from Tasks.Test import Test

def main():
    # Initialize PLC connection
    ip_address = "192.168.100.103"
    plc = PLCConnection(ip_address)

    try:
        # Open connection
        plc.open_connection()

        # Run tasks
        Test(plc)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Ensure the connection is closed
        plc.close_connection()

if __name__ == "__main__":
    main()
