import os
from ThermalCameraTest import OpticToThermal
from dlibTest import OpticPixels
import matplotlib.pyplot as plt
import time
import numpy as np
from moving_average import exponential_moving_avereage, moving_average, weighted_moving_average

xthermalLocations = []
xthermalLocations = [0 for i in range(10)]
ythermalLocations = []
ythermalLocations = [0 for i in range(10)]
values = []
values = [0 for i in range(210)]
frame = []
frame = [i for i in range(210)]

for j in range(10):
    tic = time.time()
    opticsFilename = '/home/pi/libseek-thermal-master/build/examples/image.jpg'
    os.system("sudo fswebcam " + opticsFilename)
    [x_optics, y_optics] = OpticPixels.getOpticNostrilPixel(opticsFilename)
    [x_thermal, y_thermal] = OpticToThermal.optictothermalpixel(x_optics, y_optics)
    xthermalLocations[j] = x_thermal
    ythermalLocations[j] = y_thermal
    toc = time.time()
    for i in range(21):
        thermalFilename = "/home/pi/libseek-thermal-master/build/examples/vid_frame" + str(i+1+21*j) + ".png"
        #print(x_thermal, y_thermal)
        values[i+21*j] = OpticToThermal.thermalpixelstovalues(x_thermal, y_thermal, thermalFilename)
        #time.sleep(0.14)
        #print(OpticToThermal.thermalpixelstovalues(x_thermal, y_thermal, thermalFilename))
        #print(values[i])


    print(toc-tic)

# check the thermal pixel location after finding thermal pixel location
#OpticToThermal.displaythermalpix(x_thermal, y_thermal, '/home/pi/libseek-thermal-master/build/examples/vid_frame1.png')

plt.plot(frame,values)
plt.show()

#t = np.arange(0.0,2.0, 1e-2)
#y = np.sin(t) + np.random.rand(t.shape[0])
#n = 6

#new_data_exp = exponential_moving_avereage(values, n)
#new_data_weight = weighted_moving_average(values, n)
#new_data = moving_average(values, n)

#plt.plot(values, label = 'Original Pixel Values')
#plt.plot(new_data_exp, label = 'Exp Filtered data')
#plt.plot(new_data_weight, label = 'Weight Filtered data')
#plt.plot(new_data, label = 'Smoothed Pixel Values')
#plt.legend()
#plt.show()
