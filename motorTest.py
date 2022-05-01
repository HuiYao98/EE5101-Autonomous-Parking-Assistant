import RPi.GPIO as GPIO
import threading
import pigpio
import time

#Initializing the motor:
def motor_Init():
    motorInputPin1 = 5
    motorInputPin2 = 6
    motorEnablePin = 13
    
    #Set both pins to enable the motor direction as outputs
    GPIO.setup(motorInputPin1,GPIO.OUT)
    GPIO.setup(motorInputPin2,GPIO.OUT)
    
    #Set pwm pin to motor as output
    GPIO.setup(motorEnablePin, GPIO.OUT)
    pwm=GPIO.PWM(motorEnablePin, 100)
    pwm.start(0)
    return motorEnablePin, motorInputPin1, motorInputPin2, pwm

class myMotorThread (threading.Thread):
    def __init__(self, Motor, input1, input2, pwm):
        threading.Thread.__init__(self)
        self.Motor = Motor
        self.input1 = input1
        self.input2 = input2
        self.pwm = pwm
    def runForward(self):
        print("Starting Motor Forward Thread")
        motor(1, 100, self.Motor, self.input1, self.input2, self.pwm)
        print("Exit Motor Forward Thread")
    def runBackward(self):
        print("Starting Motor Backward Thread")
        motor(2, 100, self.Motor, self.input1, self.input2, self.pwm)
        print("Exit Motor Backward Thread")
    def stop(self):
        print("Starting Motor Stop Thread")
        motor(0, 0, self.Motor, self.input1, self.input2, self.pwm)
        print("Exit Motor Stop Thread")

def motor(number,dutyCycle, p, i1, i2, pwm): #duty cycle can be changed during testing if turn too much/too little
    #p.ChangeDutyCycle(dutyCycle)
    if number == 0:
        #Stop:
        GPIO.output(i1, False)
        GPIO.output(i2, False)
    elif number == 1:
        #Go forward:
        GPIO.output(i1, True)
        GPIO.output(i2, False)
    elif number == 2:
        #Go backward:
        GPIO.output(i1, False)
        GPIO.output(i2, True)
    #Dutycycle set to 100% for now
    pwm.ChangeDutyCycle(dutyCycle)
    GPIO.output(p, True)
    print("Motor dutycycle: " + str(dutyCycle))
    #Put thread to sleep for other threads to run
    time.sleep(1)