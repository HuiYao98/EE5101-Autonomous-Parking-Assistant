import RPi.GPIO as GPIO
import threading
import pigpio
import time

def motor_Init(pwm):
    motorInputPin1 = 5
    motorInputPin2 = 6
    motorEnablePin = 13
    
    GPIO.setup(motorInputPin1,GPIO.OUT)
    GPIO.setup(motorInputPin2,GPIO.OUT)
    pwm.set_mode(motorEnablePin, pigpio.OUTPUT)
    pwm.set_PWM_frequency(motorEnablePin, 50 )
    return motorEnablePin, motorInputPin1, motorInputPin2

class myMotorThread (threading.Thread):
    def __init__(self, Motor, input1, input2, pwm):
        threading.Thread.__init__(self)
        self.Motor = Motor
        self.input1 = input1
        self.input2 = input2
        self.pwm = pwm
    def runForward(self):
        print("Starting Motor Thread")
        motor(1, 500, self.Motor, self.input1, self.input2, self.pwm)
        print("Exit Motor Thread")
    def runBackward(self):
        print("Starting Motor Thread")
        motor(2, 500, self.Motor, self.input1, self.input2, self.pwm)
        print("Exit Motor Thread")
    def stop(self):
        print("Starting Motor Thread")
        motor(0, 0, self.Motor, self.input1, self.input2, self.pwm)
        print("Exit Motor Thread")

def motor(number,dutyCycle, p, i1, i2, pwm): #duty cycle can be changed during testing if turn too much/too little
    #p.ChangeDutyCycle(dutyCycle)
    if number == 0:
        #Stop
        GPIO.output(i1, False)
        GPIO.output(i2, False)
    elif number == 1:
        #Go forward
        GPIO.output(i1, True)
        GPIO.output(i2, False)
    elif number == 2:
        #Go forward
        GPIO.output(i1, False)
        GPIO.output(i2, True)
    pwm.set_servo_pulsewidth(p, dutyCycle)
    print("Motor dutycycle: " + str(dutyCycle))
    time.sleep(0.5)