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
