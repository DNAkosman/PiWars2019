from pololu_drv8835_rpi import motors
import math



class MotorControl:

    def __init__(self):
        self.rightSpeed = 0
        self.leftSpeed = 0

    def setSpeeds(self, rightSpeed, leftSpeed):

        self.rightSpeed = rightSpeed
        self.leftSpeed = leftSpeed

        480 if rightSpeed>480 else rightSpeed
        -480 if rightSpeed < -480 else rightSpeed

        480 if leftSpeed > 480 else leftSpeed
        -480 if leftSpeed < -480 else leftSpeed



        motors.setSpeeds(rightSpeed, leftSpeed)

    def controllerDataToMotorSpeed(self, x, y, t):
        
        r = math.hypot(x, y)
        t = math.atan2(y, x)

        t += math.pi / 4

        left = r * math.cos(t)
        right = r * math.sin(t)

        left = left * math.sqrt(2)
        right = right * math.sqrt(2)
 
        left = max(-1, min(left, 1))
        right = max(-1, min(right, 1))

        return int(left * 480), -int(right * 480)
