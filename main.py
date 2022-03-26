from ultrasonicTest import myUltraThread, ultraSonic_Init
from servoMotorTest import myServoThread, servo_Init
import RPi.GPIO as GPIO

#Set board to use GPIO board pin numbering
GPIO.setmode(GPIO.BCM)

#Initialize the sensors/motors
ultraD = ultraSonic_Init()
servo = servo_Init()

if __name__ == '__main__':
    try:
        #To store the threads and ultrasonic sensor values
        threads = []
        ultraSensorValues = {}
        
        #Create New Threads:
        thread1 = myUltraThread(1,ultraD["GPIO_TRIGGER1"], ultraD["GPIO_ECHO1"])
        thread2 = myUltraThread(2,ultraD["GPIO_TRIGGER2"], ultraD["GPIO_ECHO2"])
        thread3 = myServoThread(25, servo)
        
        #Adding threads to list of threads to execute
        threads.append(thread1)
        threads.append(thread2)
        #threads.append(thread3)
        
        #Executing the threads
        for t in threads:
            t.start()
        while True:
            for t in threads:
                t.join()
            for t in threads:
                ultraSensorValues[t.sensorNo] = t.run()
            #Can use this dict to trigger servo thread movement 
            print(ultraSensorValues)

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        servo.stop()
        GPIO.cleanup()