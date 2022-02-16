import os
from ThermalCameraTest import OpticToThermal
from dlibTest import OpticPixels

#os.system("sudo /home/pi/libseek-thermal-master/build/examples/seek_snapshot")
opticsFilename = 'KarisCropTestOptics.jpg'
[x_optics, y_optics] = OpticPixels.getOpticNostrilPixel(opticsFilename)


filename = '/home/pi/PycharmProjects/seniordesign/KarisCropTestThermal.png'
OpticToThermal.optictothermalpixel(x_optics, y_optics, filename)


#print('nonsense')
