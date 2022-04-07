from ThermalCameraTest import OpticToThermal
from dlibTest import OpticPixels
import time

# set parameters
opticTiming = 3             # timing buffer for frames that take ms to process
totalSecondOfData = 30      # the amount of seconds of data taken
buffer = 100                # plus/minus buffer is the amount of variance acceptable between optical images so that
                            # ML algorithm does not have to rerun
intervalOpticalData = 5     # amount of seconds between each optical image in data taken

# initialize variables
values = []                 # stores pixel values
values = [0 for i in range(totalSecondOfData*7)]
frame = []                  # matrix of 1 to the number of frames for plotting data
frame = [i for i in range(totalSecondOfData*7)]
previousOpticsFilename = '/home/pi/PycharmProjects/seniordesign/im1.png'    # set to the first optics image



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
        if abs(diff1 - diff2) > buffer:
            [x_optics, y_optics] = OpticPixels.getOpticNostrilPixel(opticsFilename)
            [x_thermal, y_thermal] = OpticToThermal.optictothermalpixel(x_optics, y_optics)
            previousOpticsFilename = opticsFilename
    #OpticToThermal.displaythermalpix(x_thermal, y_thermal, "/home/pi/vid_frame" + str(j * 35 + 1) + ".png")


    for i in range(intervalOpticalData*7):
        thermalFilename = "/home/pi/vid_frame" + str(i+1+intervalOpticalData*7*j) + ".png"
        values[i+intervalOpticalData*7*j] = OpticToThermal.thermalpixelstovalues(x_thermal, y_thermal, thermalFilename)

    toc = time.time()
    delay = toc - tic
    print('first delay: ' + str(delay))
    if delay < opticTiming:
        time.sleep(opticTiming-delay)
    toc2 = time.time()
    print('total: ' + str(toc2 - tic))

OpticToThermal.showData(values)
