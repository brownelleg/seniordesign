# seniordesign

# README

# This project is for a senior capstone class at John Brown University working alongside Montana State University.
This project uses an optical (normal) camera and a thermal (heat sensing) camera in conjuction with a raspberry pi (microcontroller/computer). This readme doument will detail how to run this project beginning with hardward setup and intitial library installments. The IDE used was PyCharm. For other IDEs, parts of the process may be different. The 3D printed part is a mount for the thermal and optical cameras, taken from Dr. Bryce Hill at Montana Technological University.

# Credits
* https://github.com/OpenThermal/libseek-thermal
* moving average code was taken from another github that I can't find

# STEP 1: INSTALL OPENCV ON RASPBERRY PI
After going through the normal installation process for the reaspberry pi os (https://www.raspberrypi.com/documentation/computers/getting-started.html), you will need to install opencv on the pi.
To do that, start with https://singleboardbytes.com/647/install-opencv-raspberry-pi-4.htm Method 1 (install with pip). 
[pycharm download: https://raspberrytips.com/install-pycharm-raspberry-pi/] 
After PyCharm is installed, make sure to download the interpreter, link to git repository by signing into pycharm.  
Since you've already downlaoded OpenCV, it is located in home/pi.
There are two folders: opencv-4.0.0 and opencv_contrib-4.0.0, that need to be copied into "external libraries," or "bin" folder, where Python 3.9 is.
On our pi, Pycharm was located in /home/pi/Downloads/pycharm-community-2021.3.1/bin

# STEP 2: DOWNLOAD LIBSEEK-THERMAL LIBRARY
The libseek_thermal library is a C++ library that can take photos and stream video from the seek thermal compact camera.
It is located at: https://github.com/OpenThermal/libseek-thermal
Follow the instructions in the "Build" section of their readme
Replace their seek_viewer function with the seek_viewer function in this repository (the difference is that theirs doesn't save any files and ours does)

# STEP 3: DOWNLOAD FUNCTIONS FROM THIS REPOSITORY
Download the following files from this repo:
* dlibTest.py
* ThermalOpticalTakePhoto.py
* ThermalCameraTest.py
* moving_average.py

These should be all of the functions you need to gather data from both the thermal and optical cameras and display it in a graph format

Optionally:
* ThermalOpticalTakePhotoLivePlotting.py

This code is not fully developed but ideally it can plot the data in live time on a graph that updates as the subject breaths

# STEP 4: CHECK IMPORTS
Make sure that all libaries called in each script have been imported. We found that the easiest way to do this was in PyCharm directly.

# CONTACT INFORMATION
contact trippekaris@gmail.com with questions
