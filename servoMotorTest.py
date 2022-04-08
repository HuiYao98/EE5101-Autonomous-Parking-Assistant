import RPi.GPIO as GPIO
import threading
import pigpio

#Initialize the Servo motor
def servo_Init(pwm):
    servoPIN = 12 
    pwm.set_mode(servoPIN, pigpio.OUTPUT)
    pwm.set_PWM_frequency(servoPIN, 50 )
    #GPIO.setup(servoPIN, GPIO.OUT)
    #p = GPIO.PWM(servoPIN, 50) # GPIO 12 for PWM with 50Hz
    #p.start(0) # Start the servo motor 
    return servoPIN

#Servo Thread defn
class myServoThread (threading.Thread):
    def __init__(self, Servo, pwm):
        threading.Thread.__init__(self)
        self.Servo = Servo
        self.pwm = pwm
    def runStraight(self):
        print("Starting Servo Thread")
        servo(1500, self.Servo, self.pwm)
        print("Exit Servo Thread")
    def runLeft(self):
        print("Starting Servo Thread")
        servo(500, self.Servo, self.pwm)
        print("Exit Servo Thread")
    def runRight(self):
        print("Starting Servo Thread")
        servo(2500, self.Servo, self.pwm)
        print("Exit Servo Thread")

def servo(dutyCycle, p, pwm): #duty cycle can be changed during testing if turn too much/too little
    #p.ChangeDutyCycle(dutyCycle)
    pwm.set_servo_pulsewidth(p, dutyCycle)
    print(dutyCycle)
    

