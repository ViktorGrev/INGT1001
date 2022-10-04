#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=120)

ev3.speaker.beep()
ev3.screen.print("Hello World!")
time.sleep(3)
for x in range(4):
    robot.straight(250)
    ev3.speaker.beep()
    robot.turn(90)
    ev3.speaker.beep()
 
ev3.screen.print("Have a nice day!")
time.sleep(3)
ev3.speaker.beep()