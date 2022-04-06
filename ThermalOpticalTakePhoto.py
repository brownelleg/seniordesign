from ThermalCameraTest import OpticToThermal
from dlibTest import OpticPixels
import time


xthermalLocations = []
xthermalLocations = [0 for i in range(10)]
ythermalLocations = []
ythermalLocations = [0 for i in range(10)]
values = []
values = [0 for i in range(210)]
frame = []
frame = [i for i in range(210)]

previousOpticsFilename = '/home/pi/PycharmProjects/seniordesign/im1.png'

for j in range(6):
    #if (OpticPixels.getOpticNostrilPixel(opticsFilename) == [0, 0]):
    #    print("No face detected")
    #    exit(0)
    opticsFilename = '/home/pi/PycharmProjects/seniordesign/im' + str(j + 1) + '.png'
    tic = time.time()
    if j == 0:
        [x_optics, y_optics] = OpticPixels.getOpticNostrilPixel(opticsFilename)
        [x_thermal, y_thermal] = OpticToThermal.optictothermalpixel(x_optics, y_optics)
    else:
        diff1 = OpticPixels.checkImageDifference(opticsFilename)
        diff2 = OpticPixels.checkImageDifference(previousOpticsFilename)
        if abs(diff1 - diff2) > 50:
            [x_optics, y_optics] = OpticPixels.getOpticNostrilPixel(opticsFilename)
            [x_thermal, y_thermal] = OpticToThermal.optictothermalpixel(x_optics, y_optics)
            previousOpticsFilename = opticsFilename
    OpticToThermal.displaythermalpix(x_thermal, y_thermal, "/home/pi/vid_frame" + str(j * 35 + 1) + ".png")
    toc = time.time()

    for i in range(35):
        thermalFilename = "/home/pi/vid_frame" + str(i+1+35*j) + ".png"
        values[i+35*j] = OpticToThermal.thermalpixelstovalues(x_thermal, y_thermal, thermalFilename)

    print(toc-tic)

OpticToThermal.showData(values)
