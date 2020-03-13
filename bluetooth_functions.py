import sys

import bluetooth
import time

class pi_BT:


    def __init__(self):
        self.port=3
        self.server_MAC='14:10:9F:DD:70:A2'
        self.bt_error = 0


    def start_bluetooth(self):
        self.sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.sock.bind(("", bluetooth.PORT_ANY))
        self.sock.listen(1)

        self.port = self.sock.getsockname()[1]
        uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
        print("Waiting for connection on RFCOMM channel", self.port)
        self.client_sock, self.client_info = self.sock.accept()
        print("Accepted connection from", self.client_info)


    def stop_bluetooth(self):
        self.sock.close()
        self.client_sock.close()

    def send_msg(self,msg):
        self.client_sock.send(msg)

    def send_array(self,big_msg):
        #big msg is string
        self.client_sock.send(big_msg)



