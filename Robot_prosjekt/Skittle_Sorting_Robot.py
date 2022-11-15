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

#Kranen
gripper_motor = Motor(Port.A)
elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])
base_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [12, 36])
elbow_motor.control.limits(speed=60, acceleration=120)
base_motor.control.limits(speed=60, acceleration=120)
base_switch = TouchSensor(port=Port.S4)
elbow_sensor = ColorSensor(port=Port.S3)
obstacle_sensor = UltrasonicSensor(port=Port.S1)

#Beltet
belt_sensor = ColorSensor(port=Port.S2)
belt_motor = Motor(port=Port.C)


class Crane:
    def __init__(self, name, base_motor, elbow_motor, gripper_motor, elbow_sensor, obstacle_sensor, base_switch):
        self.name = name
        self.base_motor = base_motor
        self.elbow_motor = elbow_motor
        self.gripper_motor = gripper_motor
        self.elbow_sensor = elbow_sensor
        self.obstacle_sensor = obstacle_sensor
        self.base_switch = base_switch

    elbow_motor.control.limits(speed=60, acceleration=120)
    base_motor.control.limits(speed=60, acceleration=120)

    def robot_pick(self, position):
        # Rotate to the pick-up position.
        base_motor.run_target(60, position)
        # Lower the arm.
        elbow_motor.run_target(60, -55)
        # Close the gripper to grab the wheel stack.
        gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
        # Raise the arm to lift the wheel stack.
        elbow_motor.run(60)
        while elbow_sensor.reflection() < 32:
            wait(10)
        elbow_motor.hold()

    def robot_release(self, position):
        # Rotate to the drop-off position.
        base_motor.run_target(60, position)
        # Open the gripper to release the wheel stack.
        gripper_motor.run_target(200, -90)
        # Raise the arm.
        elbow_motor.run(60)
        while elbow_sensor.reflection() < 32:
            wait(10)
        elbow_motor.hold()

class Belt:
    def __init__(self, name, belt_motor, belt_sensor):
        self.name = name
        self.belt_motor = belt_motor
    
    def sort(self):
        starttime = time.time()
        while(10 >= time.time() - starttime):
            belt_motor.run(60)
            ev3.screen.print(belt_sensor.color())
            if belt_sensor.color() == Color.YELLOW:
                self.reverse()
                break
        belt_motor.run(0)
    
    def reverse(self):
        starttime = time.time()
        while(10 >= time.time() - starttime):
            belt_motor.run(-60)



value = False
belt = False

def start():
        #Løfter kranen start
        elbow_motor.run(15)
        while elbow_sensor.reflection() < 32:
            wait(10)
        elbow_motor.hold()
        #Setter rotasjon til 0 grader 
        base_motor.run(-60)
        while not base_switch.pressed():
            wait(10)
        base_motor.reset_angle(0)
        base_motor.hold()
        #Tester kroken
        gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
        gripper_motor.reset_angle(0)
        gripper_motor.run_target(200, -90)

        pick_position = 105
        release_position = 0
        crane1 = Crane("crane", base_motor, elbow_motor, gripper_motor, elbow_sensor, obstacle_sensor, base_switch)
        belt1 = Belt("Belt", base_motor, belt_sensor)
        while True:
            if obstacle_sensor.distance() < 60:
                crane1.robot_pick(pick_position)
                crane1.robot_release(release_position)
                belt1.sort()

start()








