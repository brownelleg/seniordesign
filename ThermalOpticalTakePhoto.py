import os
from ThermalCameraTest import OpticToThermal
from dlibTest import OpticPixels
import matplotlib.pyplot as plt
import numpy as np

#os.system("sudo /home/pi/libseek-thermal-master/build/examples/seek_snapshot")
opticsFilename = '/home/pi/libseek-thermal-master/build/examples/image.jpg'
[x_optics, y_optics] = OpticPixels.getOpticNostrilPixel(opticsFilename)
#print(x_optics, y_optics)

values = []
values = [0 for i in range(71)]
time = []
time = [i for i in range(71)]

for i in range(70):
    thermalFilename = "/home/pi/libseek-thermal-master/build/examples/vid_frame" + str(i+1) + ".png"
    [x_thermal, y_thermal] = OpticToThermal.optictothermalpixel(x_optics, y_optics, thermalFilename)
    #print(x_thermal, y_thermal)
    values[i] = OpticToThermal.thermalpixelstovalues(x_thermal, y_thermal, thermalFilename)
    #print(OpticToThermal.thermalpixelstovalues(x_thermal, y_thermal, thermalFilename))
    #print(values[i])

# check the thermal pixel location after finding thermal pixel location
OpticToThermal.displaythermalpix(x_thermal, y_thermal, '/home/pi/libseek-thermal-master/build/examples/vid_frame1.png')

plt.plot(time,values)
plt.show()

