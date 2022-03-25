import RPi.GPIO as GPIO
import threading
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER1 = 23
GPIO_ECHO1 = 24
GPIO_TRIGGER2 = 25
GPIO_ECHO2 = 16
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

class myUltraThread (threading.Thread):
    def __init__(self,sensorNo, triggerPin, echoPin):
        threading.Thread.__init__(self)
        self.sensorNo = sensorNo
        self.triggerPin = triggerPin
        self.echoPin = echoPin
    def run(self):
        print("Starting Thread " + str(self.sensorNo))
        distance(self.sensorNo, self.triggerPin, self.echoPin)
        print("Exit Thread " + str(self.sensorNo))
        
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
if __name__ == '__main__':
    try:
        while True:
            threads = []
            #Create New Threads:
            thread1 = myUltraThread(1,GPIO_TRIGGER1, GPIO_ECHO1)
            thread2 = myUltraThread(2,GPIO_TRIGGER2, GPIO_ECHO2)
            threads.append(thread1)
            threads.append(thread2)
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            print("Next Cycle")
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
