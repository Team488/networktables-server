import time
from networktables import NetworkTablesInstance

if __name__ == '__main__':
    print("Starting NetworkTables Server")
    nt_inst = NetworkTablesInstance.getDefault()
    nt_inst.startServer()
    # loop forever
    while True:
        time.sleep(1)
