import RPi.GPIO as GPIO
import threading
import time

servoPIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

class myServoThread (threading.Thread):
    def __init__(self,dutyCycle):
        threading.Thread.__init__(self)
        self.dutyCycle = dutyCycle
        
    def run(self):
        print("Starting Servo Thread")
        servo(self.dutyCycle)
        print("Exit Servo Thread")

def servo(dutyCycle):
    p.ChangeDutyCycle(dutyCycle)
    time.sleep(0.5)
    
p = GPIO.PWM(servoPIN, 500) # GPIO 12 for PWM with 500Hz
p.start(2.5) # Initialization
try:
      threads = []
      thread1 = myServoThread(25)
      threads.append(thread1)
      for t in threads:
          t.start()
      for t in threads:
          t.join()
      print("Next Cycle")
      time.sleep(0.5)
      p.stop()
      GPIO.cleanup()
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
