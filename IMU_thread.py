import logging
from threading import Condition, Thread
from IMU_functions import IMU
from error_functions import errors


class IMU_Thread:

    def __init__(self):
        self.imu_condition=Condition()
        self.imu=IMU()

    def startup_imu(self):
        self.imu.check_all_sensors()

    def init_imu_thread(self):
        self.imu_condition.acquire()

    def notify_imu_thread(self):
        self.imu_condition.notify()

    def release_imu_thread(self):
        self.imu_condition.release()

    def imu_loop(self):
            self.init_imu_thread()
            self.imu.read_all_sensors()
            print('imu read')
            self.notify_imu_thread()
            #self.release_imu_thread()
            self.imu.imu_delay()

    def imu_run(self):
        while self.imu.sensor_error == 0:
            self.imu_loop()









