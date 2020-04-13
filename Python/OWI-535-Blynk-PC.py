import serial
import time
import os
import threading
import pyttsx3

voice = pyttsx3.init()

from roboarm import Arm
arm = Arm()

import BlynkLib
BLYNK_AUTH = 'fe21DHbGkGWUTaTwSrwwViUyIFGWXSEc'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

def defineButtonControls():

    @blynk.VIRTUAL_WRITE(1)
    def baseRotationHandlerCounter(value):
        if int(value[0]) == 1:
            arm.base.rotate_counter(timeout = None)
        if int(value[0]) == 0:
            arm.base.stop()

    @blynk.VIRTUAL_WRITE(2)
    def baseRotationHandlerClock(value):
        if int(value[0]) == 1:
            arm.base.rotate_clock(timeout = None)
        if int(value[0]) == 0:
            arm.base.stop()

    @blynk.VIRTUAL_WRITE(3)
    def shoulderHandlerUp(value):
        if int(value[0]) == 1:
            arm.shoulder.up(timeout = None)
        if int(value[0]) == 0:
            arm.shoulder.stop()

    @blynk.VIRTUAL_WRITE(4)
    def shoulderHandlerDown(value):
        if int(value[0]) == 1:
            arm.shoulder.down(timeout = None)
        if int(value[0]) == 0:
            arm.shoulder.stop()

    @blynk.VIRTUAL_WRITE(5)
    def elbowHandlerUp(value):
        if int(value[0]) == 1:
            arm.elbow.up(timeout = None)
        if int(value[0]) == 0:
            arm.elbow.stop()

    @blynk.VIRTUAL_WRITE(6)
    def elbowHandlerDown(value):
        if int(value[0]) == 1:
            arm.elbow.down(timeout = None)
        if int(value[0]) == 0:
            arm.elbow.stop()

    @blynk.VIRTUAL_WRITE(7)
    def wristHandlerUp(value):
        if int(value[0]) == 1:
            arm.wrist.up(timeout = None)
        if int(value[0]) == 0:
            arm.wrist.stop()

    @blynk.VIRTUAL_WRITE(8)
    def wristHandlerDown(value):
        if int(value[0]) == 1:
            arm.wrist.down(timeout = None)
        if int(value[0]) == 0:
            arm.wrist.stop()

    @blynk.VIRTUAL_WRITE(9)
    def gripHandlerOpen(value):
        if int(value[0]) == 1:
            arm.grips.open(timeout = None)
        if int(value[0]) == 0:
            arm.grips.stop()

    @blynk.VIRTUAL_WRITE(10)
    def gripHandlerClose(value):
        if int(value[0]) == 1:
            arm.grips.close(timeout = None)
        if int(value[0]) == 0:
            arm.grips.stop()

    @blynk.VIRTUAL_WRITE(11)
    def ledHandler(value):
        if int(value[0]) == 1:
            arm.led.on(timeout = None)
        if int(value[0]) == 0:
            arm.led.off()

    @blynk.VIRTUAL_WRITE(12)
    def speechHandler(value):
        arm.base.stop()
        arm.shoulder.stop()
        arm.elbow.stop()
        voice.say(str(value))
        voice.runAndWait()

def serialComms():

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

    while True:
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

    defineButtonControls()
    while True:
       blynk.run() 

serialLoop = threading.Thread(target = serialComms, args = ())
serialLoop.start()

defineButtonControls()

while True:
    blynk.run()