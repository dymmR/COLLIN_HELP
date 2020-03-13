from threading import Thread
from IMU_thread_v2 import IMU_Thread
import time
from multiprocessing import Pipe

####### CONFIG

runtime = 5

########### CODE

print("Initializing IMU Object")
[imu_handler_pipe, imu_pipe] = Pipe(duplex=True)
imu = IMU_Thread(imu_port=imu_pipe)

print("Starting IMU Thread")
imu_thread = Thread(target=imu.main, args=())
imu_thread.daemon = True
imu_thread.start()

print("Listening to IMU Thread")
start_time = time.time()

while time.time() - start_time < runtime:
    if imu_handler_pipe.poll():
        data = imu_handler_pipe.recv()
        print(data)

    time.sleep(0.1)

print("Killing IMU Thread")
imu_handler_pipe.send("kill")

print("Joining IMU Thread")
imu_thread.join(timeout=1)

print("Done")
