#this section will have simple function for dealing with all of the GPIO funcitonality
import RPi.GPIO as GPIO
import time






class pi_GPIO:


    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        self.list_gpio=[
            8,
            10,
            12,
            13,
            15,
            16,
            18,
            19,
            21,
            22,
            23,
            24,
            26,
            29,
            31
        ]


        self.gpio_labels=[
            'left_wrist',
            'left_forearm',
            'left bicep',
            'left_shoulder',
            'left_foot',
            'left_calf',
            'left_ham',
            'lower_back',
            'right_ham',
            'right_calf',
            'right_foot',
            'right_shoulder',
            'right_bicep',
            'right_forearm',
            'right wrist'

        ]


        for i in self.list_gpio:
            GPIO.setup(i,GPIO.OUT)

    def _push_all_down(self):

        for i in self.list_gpio:
            GPIO.output(i, False)


    def _push_all_high(self):
        for i in self.list_gpio:
            GPIO.output(i, True)


    def _push_target_high(self, target):
        print("pushing target")
        print(target)
        for i in self.list_gpio:


            time.sleep(0.0001)

            if i==target:
                GPIO.output(i, True)

            else:
                GPIO.output(i, False)




