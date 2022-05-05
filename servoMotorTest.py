import RPi.GPIO as GPIO
import threading
import pigpio
import time

#Initialize the Servo motor
def servo_Init(pwm):
    servoPIN = 12 
    pwm.set_mode(servoPIN, pigpio.OUTPUT)
    pwm.set_PWM_frequency(servoPIN, 50 )
    return servoPIN

#Servo Thread defn
class myServoThread (threading.Thread):
    def __init__(self, Servo, pwm):
        threading.Thread.__init__(self)
        self.Servo = Servo
        self.pwm = pwm
    #Can adjust the dutycycle values(1st parameter) in the 3 methods below
    # according to what we need for straight/left/right
    def runStraight(self):
        print("Starting Servo Thread")
        servo(1500, self.Servo, self.pwm)
        print("Exit Servo Thread")
    def runLeft(self):
        print("Starting Servo Thread")
        servo(1150, self.Servo, self.pwm)
        print("Exit Servo Thread")
    def runRight(self):
        print("Starting Servo Thread")
        servo(1850, self.Servo, self.pwm)
        print("Exit Servo Thread")

def servo(dutyCycle, p, pwm): #duty cycle can be changed during testing if turn too much/too little
    pwm.set_servo_pulsewidth(p, dutyCycle)
    print("Servo Dutycycle: " + str(dutyCycle))
    time.sleep(0.5) #Set this thread to sleep for other threads to run
    

