import time
class robot:

    def __init__(self, ultraThreadList, ultraData, motorThread, servoThread):
        self.ultraThreadList = ultraThreadList
        self.ultraData = ultraData
        self.motorThread = motorThread
        self.servoThread = servoThread

        #For checking lot (Step 1)
        self.StartCheckLotTime = 0
        self.leftFlag = 0
        self.checkingLot = 0
        self.rightFlag = 0

        #For turning into parking lot (Step 2)
        self.parking = 0
        
        #For parked car:
        self.parked = 0

    def checkEmptySpace(self):
        if self.ultraData[6] < 20: #Got obstacle
            print("Obstacle detected, continue forward...")
            self.leftFlag = 0
            self.checkingLot = 0
            self.StartCheckLotTime = time.time()
            self.motorThread.runForward()
            self.servoThread.runStraight()

        elif self.leftFlag == 0:
            print("No obstacle detected, checking if empty lot big enough")
            self.leftFlag = 1
            self.checkingLot = 1
            self.StartCheckLotTime = time.time()
            self.motorThread.runForward()
            self.servoThread.runStraight()

        #if self.ultraData[1] == 1: #Got obstacle
            #self.rightFlag = 0
            #self.checkingLot = 0

        #elif self.rightFlag == 0 :
            #self.rightFlag = 1
            #self.checkingLot = 1
            #self.StartCheckLotTime = time.time()
            #self.motorThread.runForward()
            #self.servoThread.runStraight()

    def confirmEmptySpace(self):
        if time.time() - self.StartCheckLotTime > 1.6 and self.checkingLot == 1: #Means lot is empty
            #Lot is empty
            print("Lot is empty, reversing in...")
            if self.leftFlag == 1:
                self.parking = 1
                self.motorThread.runBackward()
                self.servoThread.runLeft()
            else: #rightFlag == 1:
                self.parking = 1
                self.motorThread.runBackward()
                self.servoThread.runRight()
        else:
            self.parking = 0
    def checkParkingObstacles(self):
        #Check how to determine car is straight in the lot
        if (self.ultraData[6] > self.ultraData[5] - 2) and (self.ultraData[6] < self.ultraData[5] + 2):
            #Car straight in the lot
            self.servoThread.runStraight()
        if self.ultraData[3] < 10:
            #Car reached end of lot
            self.parked = 1
            self.motorThread.stop()
