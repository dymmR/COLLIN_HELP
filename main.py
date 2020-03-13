#!/usr/bin/python3
from threading import Thread, enumerate
from IMU_thread_v2 import IMU_Thread
from algo_process import Algo
from Bluetooth_thread import BT_Thread
import time
from GPIO_functions import pi_GPIO
from multiprocessing import Pipe


[imu_handler_pipe, imu_pipe] = Pipe(duplex=True)


bt=BT_Thread()
imu=IMU_Thread(imu_pipe)
gp=pi_GPIO()
algo=Algo()


#test for speeed
# time.sleep(5)
#
# print("checking sensors")
#
# imu.check_all_sensors()
# print('these are the working sensors')
# print(imu.working_sensors)
# time.sleep(2)
# start=int(round(time.time()*1000))
# log=[]
# for i in range(0,1000):
#     imu.read_all_sensors()
#     log.append(imu.accel['x'])
#
# end=int(round(time.time()*1000))
# print("done")
# print('total time')
# print(end-start)

#test for threading
time.sleep(5)

print("checking sensors")
imu.startup_imu()
print('these are the working sensors')
print(imu.imu.working_sensors)
time.sleep(2)
bt.startup_bt()
time.sleep(2)


print('starting thread')
imu_thread=Thread(target=imu.imu_run())
bt_thread=Thread(target=bt.bt_run())
algo_thread=Thread(target=algo.run())

imu_thread.setDaemon(True)
bt_thread.setDaemon(True)
algo_thread.setDaemon(True)

print(enumerate())
bt_thread.start()
algo_thread.start()
imu_thread.start()

while True:
    time.sleep(0.1)
    pass







