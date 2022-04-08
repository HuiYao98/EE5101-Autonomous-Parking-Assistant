from ultrasonicTest import myUltraThread, ultraSonic_Init
from servoMotorTest import myServoThread, servo_Init
import RPi.GPIO as GPIO
import pigpio

#Set board to use GPIO board pin numbering
GPIO.setmode(GPIO.BCM)

#Initialize the sensors/motors
ultraD = ultraSonic_Init()
pwm = pigpio.pi()
servo = servo_Init(pwm)

if __name__ == '__main__':
    try:
        #To store the threads and ultrasonic sensor values
        threads = []
        ultraSensorValues = {}
        
        #Create New Ultrasonic Threads:
        thread1 = myUltraThread(1,ultraD["GPIO_TRIGGER1"], ultraD["GPIO_ECHO1"])
        thread2 = myUltraThread(2,ultraD["GPIO_TRIGGER2"], ultraD["GPIO_ECHO2"])
        
        #Create thread for Servo
        thread3 = myServoThread(servo,pwm)
        
        #Adding ultrasonic threads to list of threads to execute
        threads.append(thread1)
        threads.append(thread2)
        
        #Executing the threads
        for t in threads:
            t.start()
        thread3.start()
        while True:
            for t in threads:
                t.join()
            for t in threads:
                ultraSensorValues[t.sensorNo] = t.run()
            #Can use this dict to trigger servo thread movement 
            print(ultraSensorValues)
            
            if ultraSensorValues[1] == 1: #If my left ultrasonic sensor is too near
                #, front wheels turn right to reverse right
                #Turn right:
                thread3.runRight() #func to turn front wheel right
            elif ultraSensorValues[2] == 1: #If my right ultrasonic sensor is too near
                #Turn left:
                thread3.runLeft() #func to turn front wheel left
            else: #All clear, continue straight path
                #Go straight:
                thread3.runStraight()
                

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        pwm.set_PWM_dutycycle(servo,0)
        pwm.set_PWM_frequency(servo,0)
        GPIO.cleanup()