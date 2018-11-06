#A program that measures pitch and acceleration as a function of time

import time

timeStep = 0 
#Open text file
timestr = time.strftime("%H-%M-%S")
print(timestr)
F = open("data"+timestr+".txt","w")

#Initial waiting time 60s
time.sleep(60)
print("Starting Recording")

#Record for 10 mins at 10hz 
while timeStep < 600:
	time.sleep(0.1)
	#Record Pitch
	pitch = 12
	#Record acceleration
	acceleration = 5
    #Print into 3 coloumns
	F.write(str(round(timeStep,1))+"    ")
	F.write(str(pitch)+"    ")
	F.write(str(acceleration)+"\n")
	#Incriment time
	timeStep += 0.1
#Closing the file
F.close()
