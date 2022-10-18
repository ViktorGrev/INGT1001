#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random
import time

ev3 = EV3Brick()
right_sensor= ColorSensor(port=Port.S4)
left_sensor= ColorSensor(port=Port.S1)
touch_sensor1 = TouchSensor(port=Port.S2)
touch_sensor2 = TouchSensor(port=Port.S3)
left_motor = Motor(port=Port.B)
right_motor = Motor(port=Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

#Kjøreprosess
value = False
counter = 0
while not value:
    if touch_sensor1.pressed():
        value = True
        road = "left"
    if touch_sensor2.pressed():
        value = True
        road = "right"

def r2lTransition():
    starttime = time.time()
    while(7 >= time.time() - starttime):
        if left_sensor.reflection() <= 15:
            robot.drive(60, -70)
        else:
            robot.drive(190, 10)

def l2rTransition():
    starttime = time.time()
    while(4 >= time.time() - starttime):
        if right_sensor.reflection() <= 15:
            robot.drive(60, 30)
        else:
            robot.drive(250,-10)
    

while value:
    if road == "right":
        if right_sensor.reflection() <= 15:
            robot.drive(150, 25)
        else:
            robot.drive(175,-30)

        if left_sensor.reflection() <= 15:
            r2lTransition()
            road = "left"

    elif road == "left":
        if left_sensor.reflection() <= 15:
            robot.drive(50, -70)
        else:
            robot.drive(190, 10)

        if right_sensor.reflection() <= 15:
            l2rTransition()
            road = "right"







