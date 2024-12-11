from pylogix import PLC

class PLCConnection:
    def __init__(self, ip_address, processor_slot=0, is_micro800=False):
        self.ip_address = ip_address
        self.processor_slot = processor_slot
        self.is_micro800 = is_micro800
        self.comm = None

    def open_connection(self):
        if self.comm is None:
            self.comm = PLC()
            self.comm.IPAddress = self.ip_address
            self.comm.ProcessorSlot = self.processor_slot
            self.comm.Micro800 = self.is_micro800

            # try:
            #     # Perform a test read to confirm the connection
            #     response = self.comm.Read("DummyTag")
            #     if response.Status == "Success":
            #         print(f"Connection to PLC at {self.ip_address} opened successfully.")
            #     else:
            #         raise ConnectionError(f"Failed to connect to PLC at {self.ip_address}: {response.Status}")
            # except Exception as e:
            #     self.comm = None  # Reset comm on failure
            #     raise ConnectionError(f"Connection error: {e}")
        else:
            print("Connection already established.")

    def close_connection(self):
        if self.comm:
            self.comm.Close()
            self.comm = None
            print("Connection closed.")
        else:
            print("No active connection to close.")

    def read_tag(self, tag_name):
        if not self.comm:
            raise ConnectionError("No active connection. Open the connection first.")
        ret = self.comm.Read(tag_name)
        return ret.TagName, ret.Value, ret.Status

    def write_tag(self, tag_name, value):
        if not self.comm:
            raise ConnectionError("No active connection. Open the connection first.")
        ret = self.comm.Write(tag_name, value)
        return ret.Status

    def is_connected(self):
        return self.comm is not None
