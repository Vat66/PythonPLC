from Routines.ReadTag import read_tag
from Routines.WriteTag import write_tag

def Test(plc_connection):
    print("Running Task 1...")
    read_tag(plc_connection, "PyFlash")
