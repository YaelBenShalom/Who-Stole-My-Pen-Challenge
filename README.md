# "Who Stole My Pen" Challenge


## Table of Contents

- [Overview](#overview)
- [Installation Instructions](#installation-instructions)
- [Usage and Configuration Instructions](#usage-and-configuration-instructions)



## Overview

In This project, I programmed a robotic arm to "steal" a pen from my hand and throw it on the floor. I used computer vision to detect and locate the pen in the space, and motion planning to control a robotic arm.<br>
This project contains 2 parts:

1. A computer vision algorithm for recognizing the 3D location of a purple pen, using a D435i depth-camera. The software recognize the pen by its color, and locate its coordinate using the 3D camera.
2. Controlling a PincherX 100 robotic arm to accurately seize the pen under varying conditions, and throw it on the floor.

## Installation Instructions
1. Install the RealSense SDK:
  ```
  # Install intel's keys
  sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE

  # Add the apt repository
  sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main"

  # Update the package list
  sudo apt update

  # Install the packages
  sudo apt install librealsense2-dkms librealsense2-utils librealsense2-dev librealsense2-dbg librealsense2-gl-dev ros-noetic-realsense2-camera ros-noetic-realsense2-description

  # Install the python wrapper
  pip3 install pyrealsense2 
  ```

2. Install the PincherX 100 Interbotix library:
  ```
  # Create the workspace
  mkdir -p ~/custom_ws/src
  cd custom_ws/src

  # Clone the repositories
  git clone https://github.com/Interbotix/interbotix_ros_core.git
  git clone https://github.com/Interbotix/interbotix_ros_manipulators.git -b noetic
  git clone https://github.com/Interbotix/interbotix_ros_toolboxes.git

  # Remove some CATKIN_IGNORE files so we build these packages
  find . -name CATKIN_IGNORE | xargs rm

  # Install the udev rules for the arm
  sudo cp interbotix_ros_core/interbotix_ros_xseries/interbotix_xs_sdk/99-interbotix-udev.rules /etc/udev/rules.d
  sudo udevadm control --reload-rules
  sudo udevadm trigger

  # Install remaining depenencies and build the workspace
  cd ~/custom_ws
  rosdep install --from-paths src --ignore-src -r -y
  catkin_make
  ```
3. Clone repository and build the ws:
  ```
  git clone https://github.com/YaelBenShalom/Who-Stole-My-Pen-Challenge.git
  cd ../..
  catkin_make
  source devel/setup.bash 
  ```

## Usage and Configuration Instructions

Make sure that the realsense D435i and the PincherX robotic arm are connected to the computer (The realsense camera also required external power connection).

To run the software, run the code `pen_recognition.py`. The software records the video by default as a bagfile - `camera_video.bag`.

- In order to use pre-recorded bagfile, comment line #45 and uncomment line #46.

Pen recognition:

<p align="center">
  <img align="center" src="https://github.com/YaelBenShalom/Who-Stole-My-Pen-Challenge/blob/master/videos/pen-recognition.gif">
</p>

Pen stealing:

<p align="center">
  <img align="center" src="https://github.com/YaelBenShalom/Who-Stole-My-Pen-Challenge/blob/master/videos/pen-stealing.gif">
</p>
