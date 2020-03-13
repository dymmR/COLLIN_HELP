# coding: utf-8
## @package faboMPU9250
#  This is a library for the FaBo 9AXIS I2C Brick.
#
#  http://fabo.io/202.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBo9Axis_MPU9250
from GPIO_functions import pi_GPIO
import time
from sensor_list import sensor_obj
import sys
class IMU:


#functions to init device, variables for later

    def __init__(self):
        self.gp = pi_GPIO()
        self.gp._push_all_down()
        self.freq=40
        self.delay_value=1/self.freq
        self.sensors=[]

        self.init_mpu()
        self.working_sensors=[]
        self.gp._push_all_down()
        self.sensor_error=0

    def imu_delay(self):
        time.sleep(self.delay_value)

    def init_mpu(self):

        for i in self.gp.list_gpio:
            self.gp._push_target_high(i)
            self.imu_delay()


            try:
                self.mpu9250 = FaBo9Axis_MPU9250.MPU9250()
            except:
                continue
            else:
                print(self.gp.gpio_labels[i])
                print("sensor is working")
                break

#functions that directly read from MPU

    def read_Accel(self):
        self.accel=self.mpu9250.readAccel()
        self.ax=self.accel['x']
        self.ay = self.accel['y']
        self.az = self.accel['z']

    def read_Gyro(self):
        self.gyro=self.mpu9250.readGyro()
        self.gx=self.gyro['x']
        self.gy = self.gyro['y']
        self.gz = self.gyro['z']


    def read_Mag(self):
        self.mag=self.mpu9250.readMag()
        self.mx=self.mag['x']
        self.my=self.mag['y']
        self.mz=self.mag['z']

    #functions for checking which sensors are functional,

    def check_sensor(self,i):
        self.gp._push_target_high(i)
        time.sleep(self.freq/100)
        try:
            self.accel = self.mpu9250.readAccel()

        except:
            print(i)
            print('sensor is not working')


        else:
            self.working_sensors.append(i)

    def check_all_sensors(self):
        for i in range(0,len(self.gp.list_gpio)):
            time.sleep(self.delay_value)
            self.check_sensor(self.gp.list_gpio[i])

        print(self.working_sensors)
        time.sleep(2)



    #functions to create the array of sensor_obj class for later


    def init_sensor_obj_list(self):
        for j in range(0, len(self.working_sensors)):
            self.sensors.append(sensor_obj[j])

        k = 1;
        for obj in self.sensors:
            obj.pin = self.working_sensors[k]
            k = k + 1

    #read all sensors from list of created sensor objects

    def read_all_sensors(self):

        for snsr in self.sensors:
            self.imu_delay()
            self.gp._push_target_high(snsr.pin)
            self.read_Accel()
            self.read_Gyro()
            snsr.ax = self.ax
            snsr.ay = self.ay
            snsr.az = self.az
            snsr.gx= self.gx
            snsr.gy = self.gx
            snsr.gz = self.gx



