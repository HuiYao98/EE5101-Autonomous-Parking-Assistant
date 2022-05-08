from tkinter import *
from time import sleep

root = Tk()
root.title("Smart Robot Interface")

#title text
titletext = Label(root, text= 'Smart Robot Interface')
titletext.config(font= ('New Times Roman',25))
titletext.grid( row=0, column=0,columnspan=5)

ultrasonicFrame = Frame(root)
ultrasonicFrame.grid(row=1,column=2,columnspan=3)

motorServoFrame = Frame(root)
motorServoFrame.grid(row=3,column=2,columnspan=3)

buttonFrame = Frame(root)
buttonFrame.grid(row=1, column=0)

#string variables
us1str =StringVar()
us2str =StringVar()
us3str =StringVar()
us4str =StringVar()
us5str =StringVar()
us6str =StringVar()
motorStr = StringVar()
servoStr = StringVar()

#initalisation of all the commands
us1str.set('0')
us2str.set('0')
us3str.set('0')
us4str.set('0')
us5str.set('0')
us6str.set('0')
motorStr.set('0')
servoStr.set('0')


#UI For ultrasonic sensor

ultrasonicTitleHeader= Label ( ultrasonicFrame,text ="UltraSonic sensors")
ultrasonicTitleHeader.grid(row=0,column=1,columnspan=4)
 
us1 = Label(ultrasonicFrame,text='Sensor 1' )
us1.grid(row=1,column=0)
us1Prompt = Entry(ultrasonicFrame, textvariable=us1str, width=5)
us1Prompt.grid(row=1,column=1,columnspan=1 )

us2 = Label(ultrasonicFrame,text='Sensor 2' )
us2.grid(row=2,column=0)
us2Prompt = Entry(ultrasonicFrame, textvariable=us2str, width=5)
us2Prompt.grid(row=2,column=1,columnspan=1,rowspan=1)

us3 = Label(ultrasonicFrame,text='Sensor 3' )
us3.grid(row=3,column=1)
us3Prompt = Entry(ultrasonicFrame, textvariable=us3str, width=5)
us3Prompt.grid(row=3,column=2,columnspan=1,rowspan=1)

us4 = Label(ultrasonicFrame,text='Sensor 4' )
us4.grid(row=3,column=4)
us4Prompt = Entry(ultrasonicFrame, textvariable=us4str, width=5)
us4Prompt.grid(row=3,column=3,columnspan=1,rowspan=1)

us5 = Label(ultrasonicFrame,text='Sensor 5' )
us5.grid(row=2,column=5)
us5Prompt = Entry(ultrasonicFrame, textvariable=us5str, width=5)
us5Prompt.grid(row=2,column=4,columnspan=1,rowspan=1)

us6 = Label(ultrasonicFrame,text='Sensor 6' )
us6.grid(row=1,column=5)
us6Prompt = Entry(ultrasonicFrame, textvariable=us6str, width=5)
us6Prompt.grid(row=1,column=4,columnspan=1,rowspan=1)

#UI FOR MOTOR and Servo

motorLabel = Label(motorServoFrame, text= 'MotorPWM')
motorLabel.grid(row=1,column =0)
motorPrompt = Entry(motorServoFrame, textvariable=motorStr, width=5)
motorPrompt.grid(row=1,column=1 )

servoLabel = Label(motorServoFrame, text = 'ServoPWM' )
servoLabel.grid(row =1,column=4)
servoPrompt = Entry(motorServoFrame, textvariable=servoStr, width=5)
servoPrompt.grid(row=1, column=5)



#on off button
controlLabel = Label ( buttonFrame,text ="Power Controls")
controlLabel.grid(row=1,column=0,columnspan=4)

onButton = Button (buttonFrame, text='Power ON', padx=20, pady=10) #command= lambda: servocontrol("SERVO_ON")
offButton = Button (buttonFrame, text='Power OFF', padx=20, pady=10)
onButton.grid(row=2,column=0)
offButton.grid(row=3,column=0)


#dummylabel for spacing purposes
dummylabel1= Label(buttonFrame, text='   ')
dummylabel1.grid(row=0, column=2,columnspan= 5)

dummylabel2= Label(buttonFrame, text='   ')
dummylabel2.grid(row=0, column=0,columnspan=5)

root.mainloop()