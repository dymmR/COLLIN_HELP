import logging
from IMU_functions import IMU
import time

class IMU_Thread:

    def __init__(self, imu_port):
        self._imu = IMU()

        self._running = True

        self._imu_port = imu_port

    def main(self):
        while self._running:
            if self._imu_port.poll():
                com = self._imu_port.recv()
                self._execute_com(com)

            sensordata = self._imu.read_all_sensors()

            self._imu_port.send(sensordata)

            time.sleep(0.5)

    def _execute_com(self, com):
        if com == "kill":
            self._running = False

        return True