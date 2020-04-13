import serial
import time
import os
from roboarm import Arm

import BlynkLib
BLYNK_AUTH = 'fe21DHbGkGWUTaTwSrwwViUyIFGWXSEc'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

arm = Arm()

ArduinoSerial = serial.Serial('/dev/ttyUSB0',9600)
time.sleep(2)

serialBuffer = ""

global baseRot
global shoulderRot
global elbowRot

baseRot = 0
shoulderRot = 0
elbowRot = 0

baseRotOffset = 0
shoulderRotOffset = 0
elbowRotOffset = 0

outputString = ""
oldOutputString = ""
cycles = 0

def defineButtonControls():
    @blynk.VIRTUAL_WRITE(0)
    def emergencyStopHandler(value):
        if int(value[0]) == 1:
            arm.base.stop()

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

def defineJoystickControls():
    @blynk.VIRTUAL_WRITE(12)
    def joystickBaseHandler(value):

        baseLeftTurnCutoff = 640
        baseRightTurnCutoff = 384

        if int(value[0]) > baseLeftTurnCutoff:
            arm.base.rotate_clock(timeout = None)
        if int(value[0]) < baseRightTurnCutoff:
            arm.base.rotate_counter(timeout = None)
        if int(value[0]) < baseLeftTurnCutoff and int(value[0]) > baseRightTurnCutoff:
            arm.base.stop()

    #@blynk.VIRTUAL_WRITE(13)
    #def joystickVerticalHandler(value):

defineButtonControls()
defineJoystickControls()

while True:
    blynk.run()
