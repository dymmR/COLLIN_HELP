import logging
from threading import Condition, Thread
from bluetooth_functions import pi_BT

from error_functions import errors




class BT_Thread:

    def __init__(self):
        self.bt_condition=Condition()
        self.bt=pi_BT()





    def init_bt_thread(self):
        self.bt_condition.acquire()

    def wait_bt_thread(self):
        self.bt_condition.wait()

    def release_bt_thread(self):
        self.bt_condition.release()

    def startup_bt(self):
        self.bt.start_bluetooth()


    def bt_send_loop(self,data):
        self.init_bt_thread()
        #self.wait_bt_thread()
        self.bt.send_msg(data)
        self.release_bt_thread()


    def bt_run(self):
        while self.bt.bt_error==0:


            print('bt loop')

            self.bt_send_loop()
