# First import the library
import pyrealsense2 as rs
# Import Numpy for easy array manipulation
import numpy as np
# Import OpenCV for easy image rendering
import cv2
import colorsys
import math
import time
import rospy
import threading
import modern_robotics as mr

from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from interbotix_sdk import angle_manipulation as ang
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from interbotix_sdk.msg import JointCommands
from interbotix_sdk.msg import SingleCommand
from interbotix_sdk.srv import RobotInfo
from interbotix_sdk.srv import OperatingModes
from interbotix_sdk.srv import OperatingModesRequest
from interbotix_sdk.srv import RegisterValues
from interbotix_sdk.srv import RegisterValuesRequest
from interbotix_descriptions import interbotix_mr_descriptions as mrd
from interbotix_sdk.robot_manipulation import InterbotixRobot

def convert_to_cyl(position):
    x = -position[0] - 0.30  # distance of base from camera - x axis
    y = -position[1]
    z = position[2] - 0.25 # distance of base from camera - z axis
    r = math.sqrt(x**2 + z**2)
    theta = math.atan2(x, -z) #- math.pi/2
    return (r, theta, y)


position = [0.041852131485939026, 0.015240330249071121, 0.1990000158548355]
converted_position = convert_to_cyl(position)

arm = InterbotixRobot(robot_name = "px100", mrd = mrd)
arm.go_to_home_pose()
arm_position = (0.0,0.0)
arm.open_gripper(2.0)
arm.set_ee_pose_components(x = converted_position[0],z = converted_position[2]+.2, blocking = True)
arm.set_ee_cartesian_trajectory(x = -0.05)
arm.set_single_joint_position("waist", converted_position[1], blocking = True)
arm.set_ee_cartesian_trajectory(x = +0.05)

arm.close_gripper(2.0)
arm.set_ee_cartesian_trajectory(x = -0.05)
arm.go_to_home_pose()
arm.open_gripper(2.0)
arm.go_to_sleep_pose()


