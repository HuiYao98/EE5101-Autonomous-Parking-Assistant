from ultrasonicTest import myUltraThread, ultraSonic_Init
from servoMotorTest import myServoThread, servo_Init
from motorTest import myMotorThread, motor_Init
from robotMain import robot
import RPi.GPIO as GPIO
import pigpio

#Set board to use GPIO board pin numbering
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#Initialize the sensors/motors
ultraD = ultraSonic_Init()
pwm = pigpio.pi()
servo = servo_Init(pwm)
motor = motor_Init()

if __name__ == '__main__':
    try:
        #To store the threads and ultrasonic sensor values
        threads = []
        ultraSensorValues = {} #Dictionary for storing ultrasonic distance values
        
        #Create New Ultrasonic Threads:
        thread1 = myUltraThread(1,ultraD["GPIO_TRIGGER1"], ultraD["GPIO_ECHO1"])
        thread2 = myUltraThread(2,ultraD["GPIO_TRIGGER2"], ultraD["GPIO_ECHO2"])
        thread3 = myUltraThread(3,ultraD["GPIO_TRIGGER3"], ultraD["GPIO_ECHO3"])
        #thread4 = myUltraThread(4,ultraD["GPIO_TRIGGER4"], ultraD["GPIO_ECHO4"])
        thread5 = myUltraThread(5,ultraD["GPIO_TRIGGER5"], ultraD["GPIO_ECHO5"])
        thread6 = myUltraThread(6,ultraD["GPIO_TRIGGER6"], ultraD["GPIO_ECHO6"])
        
        #Create thread for Servo
        thread7 = myServoThread(servo,pwm)
        
        #Create thread for motor
        threadM = myMotorThread(motor[0], motor[1], motor[2], motor[3])
        
        #Adding ultrasonic threads to list of threads to execute
        threads.append(thread1)
        threads.append(thread2)
        threads.append(thread3)
        #threads.append(thread4)
        threads.append(thread5)
        threads.append(thread6)
        smartRobot = robot(threads, ultraSensorValues, threadM, thread7)
        #Executing the threads
        for t in smartRobot.ultraThreadList:
            t.start()
        smartRobot.motorThread.start()
        smartRobot.servoThread.start()
        smartRobot.servoThread.runStraight()
        while True:
            for t in smartRobot.ultraThreadList:
                t.join()
            for t in smartRobot.ultraThreadList:
                smartRobot.ultraData[t.sensorNo] = t.run()
            #Can use this dict to trigger servo thread movement 
            print(smartRobot.ultraData)
            if smartRobot.parking == 0: #Not parking
                smartRobot.checkEmptySpace()
                if smartRobot.leftFlag == 1:
                    smartRobot.confirmEmptySpace()

                

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        pwm.set_PWM_dutycycle(servo,0)
        pwm.set_PWM_frequency(servo,0)
        GPIO.cleanup()