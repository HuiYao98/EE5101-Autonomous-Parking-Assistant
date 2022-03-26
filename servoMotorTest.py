import RPi.GPIO as GPIO
import threading

#Initialize the Servo motor
def servo_Init():
    servoPIN = 12
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 500) # GPIO 12 for PWM with 500Hz
    p.start(2.5) # Start the servo motor 
    return p

#Servo Thread defn
class myServoThread (threading.Thread):
    def __init__(self,dutyCycle, Servo):
        threading.Thread.__init__(self)
        self.dutyCycle = dutyCycle
        self.Servo = Servo
    def run(self):
        print("Starting Servo Thread")
        servo(self.dutyCycle, self.Servo)
        print("Exit Servo Thread")

def servo(dutyCycle, p):
    p.ChangeDutyCycle(dutyCycle)
    print(dutyCycle)

