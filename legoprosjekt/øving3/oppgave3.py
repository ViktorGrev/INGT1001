
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
color_sensor= ColorSensor(port=Port.S4)
obstacle_sensor = UltrasonicSensor(port=Port.S3)
touch_sensor = TouchSensor(port=Port.S2)
left_motor = Motor(port=Port.B)
right_motor = Motor(port=Port.C)
my_motor = Motor(port=Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)


#Underholdning
def function():
    valg = random.randrange(1,5)
    if(valg == 1):
        robot.drive(0,0)
        ev3.screen.print("function 1")
        my_motor.run(-1000)
        wait(1000)
        my_motor.run(0)
    elif(valg == 2):
        ev3.screen.print("function 2")
        robot.drive(0,0)
        robot.turn(355)
        robot.turn(-355)
        wait(10)
    elif(valg == 3):
        ev3.screen.print("function 3")
        robot.drive(0,0)
        ev3.speaker.play_file(SoundFile.T_REX_ROAR)
        ev3.speaker.play_file(SoundFile.T_REX_ROAR)
        ev3.speaker.play_file(SoundFile.T_REX_ROAR)
        
    else:
        ev3.screen.print("function 4") 
        robot.drive(0,0)
        ev3.screen.print("Are you not entertained?")
        ev3.speaker.say("Are you not entertained?")
        ev3.speaker.say("Are you not entertained?")
        ev3.speaker.say("Is this not why you're here?")
        wait(10)
        
startTime = time.time()
endTime = time.time()
#Start-knapp
value = False
while not value:
    if touch_sensor.pressed():
        value = True
ev3.speaker.beep()
ev3.speaker.say("Exercise three")
#Kjøreprosess
while value:
    if color_sensor.reflection() <= 15:
        robot.drive(80, 25)
    else:
        robot.drive(60, -40)
             
#Timer
    endTime = time.time()
    ev3.screen.print(endTime - startTime)
    if endTime - startTime > 10:
        function()
        startTime = time.time()
    
#Sensor avstand
    if obstacle_sensor.distance() < 150:
        robot.drive(0,0)
        ev3.speaker.play_file(SoundFile.FANFARE)
        ev3.stop()
#Off-knapp
    if touch_sensor.pressed():
        robot.drive(0,0)
        ev3.speaker.say("Exercise done")
        #wait for 50 milliseconds
        #value 1
        value = False
        ev3.stop()
