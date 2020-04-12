import serial
import time
import os
from roboarm import Arm

from blynkKeypad import *

import BlynkLib
BLYNK_AUTH = 'fe21DHbGkGWUTaTwSrwwViUyIFGWXSEc'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

arm = Arm()

ArduinoSerial = serial.Serial('/dev/ttyUSB0',9600)
time.sleep(2)

serialBuffer = ""

baseRot = 0
shoulderRot = 0
elbowRot = 0

baseRotOffset = 0
shoulderRotOffset = 0
elbowRotOffset = 0

outputString = ""
oldOutputString = ""
cycles = 0


# Get input from Arduino serial and save it as current-session offset data
while True:

    blynk.run()

    serialBuffer = str(ArduinoSerial.readline())[2:-5]
    if serialBuffer == "BASE":
        serialBuffer = str(ArduinoSerial.readline())[2:-5]
        baseRotOffset = int(serialBuffer)
    if serialBuffer == "SHOULDER":
        serialBuffer = str(ArduinoSerial.readline())[2:-5]
        shoulderRotOffset = int(serialBuffer)
    if serialBuffer == "ELBOW":
        serialBuffer = str(ArduinoSerial.readline())[2:-5]
        elbowRotOffset = int(serialBuffer)
    serialBuffer = ""

    # Set up matrix for holding position data loaded from file
    positionMemoryMatrix = [baseRot, shoulderRot, elbowRot]

    # On first run, load saved position
    if cycles == 0:

        print("CONTENTS OF MEMORY FILE:")
        positionMemory = open('positionMemory.csv', 'r')
        positionMemoryMatrix = positionMemory.read()
        positionMemory.close()

        # Split CSV
        positionMemoryMatrix = positionMemoryMatrix.split(",")
        print(positionMemoryMatrix)

        baseRot = int(positionMemoryMatrix[0])
        shoulderRot = int(positionMemoryMatrix[1])
        elbowRot = int(positionMemoryMatrix[2])
        print("LOADED: B:" + str(baseRot) + " S:" + str(shoulderRot) + " E:" + str(elbowRot))

    # Save ongoing position data
    positionMemory = open('positionMemory.csv', 'w')
    positionMemoryMatrixFormatted = str(baseRot + baseRotOffset) + "," + str(shoulderRot + shoulderRotOffset) + "," + str(elbowRot + elbowRotOffset)
    positionMemory.write(positionMemoryMatrixFormatted)
    positionMemory.close()

    # Make copy of output string for comparing for differences and deciding if to print
    oldOutputString = outputString

    #Loaded from file
    outputStringBase = "B:" + str(baseRot) + " S:" + str(shoulderRot) + " E:" + str(elbowRot)

    # Movement for this session
    outputStringOffsets = "B:" + str(baseRotOffset) + " S:" + str(shoulderRotOffset) + " E:" + str(elbowRotOffset)

    # Combine offsets and base
    outputString = "B:" + str(baseRot + baseRotOffset) + " S:" + str(shoulderRot + shoulderRotOffset) + " E:" + str(elbowRot + elbowRotOffset)

    # Print UI
    if outputString != oldOutputString:
        os.system('clear')

        print("BASE VALUES:")
        print(outputStringBase)
        print()
        print("OFFSETS:")
        print(outputStringOffsets)
        print()
        print("COMBINED:")
        print(outputString)
        print()
        print("Cycle count: " + str(cycles))

    cycles = cycles + 1
