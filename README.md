# MRS Hackathon
GitHub repository - https://github.com/YaelBenShalom/Who-Stole-My-Pen-Challenge

## Overview
In This project I used computer vision and motion planning to control a robotic arm to "steal" a pen for my hand and throw it on the floor.
This project contains 2 parts:
1. A computer vision algorithm for recognizing the 3D location of a purple pen, using a D435i depth-camera. The software recognize the pen by its color, and locate its coordinate using the 3D camera.
2. Controlling a PincherX robotic arm to accurately seize the pen under varying conditions, and throw it on the floor.

## Usage and Configuration Instructions
Make sure that the sealsense D435i and the PincherX robotic arm are connected to the computer (The realsense camera also required external power connection).

To run the software, run the code `Hackathon_Challenge.py`. The software records the video by defalt as a bagfile - `camera_video.bag`.
- In order to use pre-recorded bagfile, comment line #45 and uncomment line #46.

Pen recognition:
![Pen recognition](https://github.com/YaelBenShalom/Who-Stole-My-Pen-Challenge/blob/master/videos/pen-recognition.gif)

Pen stealing:
![Pen stealing](https://github.com/YaelBenShalom/Who-Stole-My-Pen-Challenge/blob/master/videos/pen-stealing.gif)