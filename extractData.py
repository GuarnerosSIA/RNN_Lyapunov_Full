import pandas as pd
import RNN_Ale as RNN
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# First 2 files to analyzed
path_Input = 'platform_tests_first_part\matrix_0\matrix_0_input.csv'
path_Output = 'platform_tests_first_part\matrix_0\matrix_0_output_LHR-92216C00.csv'

Input = pd.read_csv(path_Input,sep=';')
Output = pd.read_csv(path_Output,sep=';')

roll = Input['Roll'].to_numpy()
pitch = Input['Pitch'].to_numpy()
heave = Input['Heave'].to_numpy()
timeInput = Input['Timestamp'].to_numpy()
timeStampInput = []
# Convert time to integer
for date in timeInput:
    var = dt.datetime.strptime(date,'%Y-%m-%dT%H:%M:%S.%f')
    timeStampInput.append(var)

angularV = Output['AngularVelocity'].tolist()
xAngVel = []
yAngVel = []
zAngVel = []
for item in angularV:
    my_tuple = eval(item)
    xAngVel.append(my_tuple[0])
    yAngVel.append(my_tuple[1])
    zAngVel.append(my_tuple[2])

Position = Output['Position'].tolist()

xPosition = []
yPosition = []
zPosition = []

for item in Position:
    my_tuple = eval(item)
    xPosition.append(my_tuple[0])
    yPosition.append(my_tuple[1])
    zPosition.append(my_tuple[2])

rotation = Output['Rotation'].tolist()
aRotation = []
bRotation = []
cRotation = []
dRotation = []
for item in rotation:
    my_tuple = eval(item)
    aRotation.append(my_tuple[0])
    bRotation.append(my_tuple[1])
    cRotation.append(my_tuple[2])
    dRotation.append(my_tuple[3])

velocity = Output['Velocity'].tolist()
xVel = []
yVel = []
zVel = []
for item in velocity:
    my_tuple = eval(item)
    xVel.append(my_tuple[0])
    yVel.append(my_tuple[1])
    zVel.append(my_tuple[2])


timeOutput = Output['Timestamp'].tolist()
timeStampOutput = []
# Convert time to integer
for date in timeOutput:
    var = dt.datetime.strptime(date,'%Y-%m-%dT%H:%M:%S.%f')
    timeStampOutput.append(var)


# I need to compare the inputs adquistion against the output adquisition
cont2 = 0 

inputIX = []
newRoll = []
newPitch = []
newHeave = []

outputIX = []
newXAngVel = []
newYAngVel = []
newZAngVel = []
newXPosition = []
newYPosition = []
newZPosition = []
newARotation = []
newBRotation = []
newCRotation = []
newDRotation = []
newXVel = []
newYVel = []
newZVel = []

for item in timeStampInput:
    cont = 0
    flag = 0
    for otherItem in timeStampOutput:
        if(item == otherItem):
            inputIX.append(timeStampInput[cont2])
            newRoll.append(roll[cont2])
            newPitch.append(pitch[cont2])
            newHeave.append(heave[cont2])
            outputIX.append(timeStampOutput[cont])
            newXAngVel.append(xAngVel[cont])
            newYAngVel.append(yAngVel[cont])
            newZAngVel.append(zAngVel[cont])
            newXPosition.append(xPosition[cont])
            newYPosition.append(yPosition[cont])
            newZPosition.append(zPosition[cont])
            newARotation.append(aRotation[cont])
            newBRotation.append(bRotation[cont])
            newCRotation.append(cRotation[cont])
            newDRotation.append(dRotation[cont])
            newXVel.append(xVel[cont])
            newYVel.append(yVel[cont])
            newZVel.append(zVel[cont])
            cont += 1
            cont2 += 1
            flag = 1
        else:
            cont += 1
    if (flag == 0):
        cont2 += 1
