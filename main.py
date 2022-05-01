from ultrasonicTest import myUltraThread, ultraSonic_Init
from servoMotorTest import myServoThread, servo_Init
from motorTest import myMotorThread, motor_Init
import RPi.GPIO as GPIO
import pigpio

#Set board to use GPIO board pin numbering
GPIO.setmode(GPIO.BCM)

#Initialize the sensors/motors
ultraD = ultraSonic_Init()
pwm = pigpio.pi()
servo = servo_Init(pwm)
motor = motor_Init()

if __name__ == '__main__':
    try:
        #To store the threads and ultrasonic sensor values
        threads = []
        ultraSensorValues = {}
        
        #Create New Ultrasonic Threads:
        thread1 = myUltraThread(1,ultraD["GPIO_TRIGGER1"], ultraD["GPIO_ECHO1"])
        thread2 = myUltraThread(2,ultraD["GPIO_TRIGGER2"], ultraD["GPIO_ECHO2"])
        thread3 = myUltraThread(3,ultraD["GPIO_TRIGGER3"], ultraD["GPIO_ECHO3"])
        thread4 = myUltraThread(4,ultraD["GPIO_TRIGGER4"], ultraD["GPIO_ECHO4"])
        thread5 = myUltraThread(5,ultraD["GPIO_TRIGGER5"], ultraD["GPIO_ECHO5"])
        thread6 = myUltraThread(6,ultraD["GPIO_TRIGGER6"], ultraD["GPIO_ECHO6"])
        
        #Create thread for Servo
        thread7 = myServoThread(servo,pwm)
        
        #Create thread for motor
        threadM = myMotorThread(motor[0], motor[1], motor[2], motor[3])
        
        #Adding ultrasonic threads to list of threads to execute
        threads.append(thread1)
        threads.append(thread2)
        #threads.append(thread3) #--> dk why this one & thread 6
        #got issue, maybe its bec of the connection?
        threads.append(thread4)
        threads.append(thread5)
        #threads.append(thread6)
        
        #Executing the threads
        for t in threads:
            t.start()
        thread7.start()
        threadM.start()
        while True:
            for t in threads:
                t.join()
            for t in threads:
                ultraSensorValues[t.sensorNo] = t.run()
            #Can use this dict to trigger servo thread movement 
            print(ultraSensorValues)
            
            if ultraSensorValues[1] == 1 or ultraSensorValues[2] == 1:
                #If my left ultrasonic sensor is too near
                #, front wheels turn right to reverse right
                #Turn right:
                thread7.runRight() #func to turn front wheel right
                threadM.runBackward()
            elif ultraSensorValues[4] == 1 or ultraSensorValues[5] == 1 or ultraSensorValues[6] == 1:
                #If my right ultrasonic sensor is too near
                #Turn left:
                thread7.runLeft() #func to turn front wheel left
                threadM.runBackward()
            else: #All clear, continue straight path
                #Go straight:
                thread7.runStraight()
                threadM.runForward()
                

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        pwm.set_PWM_dutycycle(servo,0)
        pwm.set_PWM_frequency(servo,0)
        GPIO.cleanup()