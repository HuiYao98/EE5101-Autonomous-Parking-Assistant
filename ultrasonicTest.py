import RPi.GPIO as GPIO
import threading
import time

#Initialize the ultrasonic sensors
def ultraSonic_Init():
    #Dictionary to store GPIO pin values
    ultraD = {}
    #set GPIO Pins for Ultrasonic Sensors
    ultraD["GPIO_TRIGGER1"] = 23
    ultraD["GPIO_ECHO1"] = 24
    ultraD["GPIO_TRIGGER2"] = 25
    ultraD["GPIO_ECHO2"] = 16
     
    #set GPIO direction (echo as input / trigger as output)
    GPIO.setup(ultraD["GPIO_TRIGGER1"], GPIO.OUT)
    GPIO.setup(ultraD["GPIO_ECHO1"], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(ultraD["GPIO_TRIGGER2"], GPIO.OUT)
    GPIO.setup(ultraD["GPIO_ECHO2"], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    
    return ultraD

#Ultrasonic Thread Defn
class myUltraThread (threading.Thread):
    def __init__(self,sensorNo, triggerPin, echoPin):
        threading.Thread.__init__(self)
        self.sensorNo = sensorNo
        self.triggerPin = triggerPin
        self.echoPin = echoPin
    def run(self):
        print("Starting Thread " + str(self.sensorNo))
        d = distance(self.sensorNo, self.triggerPin, self.echoPin)
        #If distance measured is under __cm, means servo should turn __
        if d < 15:
            print("Exit Thread, Sensor " + str(self.sensorNo) + " Too near.")
            return 1
        else:
            print("Exit Thread cond 2, Sensor " + str(self.sensorNo) + " Ok.")
            return 0

#Function to calculate and return the distance read by an ultrasonic sensor (cm)
def distance(sensorNo, TriggerPin, EchoPin):
    # set Trigger to HIGH
    GPIO.output(TriggerPin, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(TriggerPin, False)
 
    StartTime = time.time()
    StopTime = time.time()
    # save StartTime
    while GPIO.input(EchoPin) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(EchoPin) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    print("Measured distance from sensor " + str(sensorNo) + " = " + str(distance) +"cm \n")
    time.sleep(0.5)
    return distance
