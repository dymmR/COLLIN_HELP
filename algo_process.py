
from IMU_thread import IMU_Thread
from threading import Condition, Thread
from error_functions import errors

from Bluetooth_thread import BT_Thread



class Algo:

    def __init__(self):
        self.results=0
        self.algo_condition=Condition()
        self.algo_error=0


    def process(self):

        self.results=IMU_Thread.imu.accel['x']


    def algo_run(self):
        while self.algo_error==0:

            print('algo running')
            IMU_Thread.init_imu_thread()
            self.process()
            IMU_Thread.release_imu_thread()
            BT_Thread.init_bt_thread()
            BT_Thread.bt_condition.notify()
            BT_Thread.release_bt_thread()




