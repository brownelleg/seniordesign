from ThermalCameraTest import OpticToThermal
from dlibTest import OpticPixels
import time

# set parameters
maxFrames = 211             # total number of seconds * 7
opticTiming = 1             # timing buffer for frames that take ms to process
totalSecondOfData = 30      # the amount of seconds of data taken
# intervalOpticalData = 5     # amount of seconds between each optical image in data taken
buffer = 100                # plus/minus buffer is the amount of variance acceptable between optical images so that
                            # ML algorithm does not have to rerun
thermalPath = "/home/pi/Thermal_Images/vid_frame"
opticalPath = "/home/pi/PycharmProjects/seniordesign/image"


# initialize variables
values = []                 # stores pixel values
values = [0 for i in range(maxFrames)]
frame = []                  # matrix of 1 to the number of frames for plotting data
frame = [i for i in range(maxFrames)]

firstThermal = 0
nextThermal = 1
j = 0

while (nextThermal < maxFrames):
    #while (OpticPixels.getOpticNostrilPixel(opticsFilename) == [0, 0]):
    #    print("No face detected")
    #    exit(0)
    tic = time.time()
    OpticPixels.takeSingleOpticImage(j)
    opticsFilename = opticalPath + str(j) + ".png"
    if j == 0:
        [x_optics, y_optics] = OpticPixels.getOpticNostrilPixel(opticsFilename)
        [x_thermal, y_thermal] = OpticToThermal.optictothermalpixel(x_optics, y_optics)
        previousOpticsFilename = opticsFilename
    else:
        diff1 = OpticPixels.checkImageDifference(opticsFilename)
        diff2 = OpticPixels.checkImageDifference(previousOpticsFilename)
        if abs(diff1 - diff2) > buffer:
            [x_optics, y_optics] = OpticPixels.getOpticNostrilPixel(opticsFilename)
            [x_thermal, y_thermal] = OpticToThermal.optictothermalpixel(x_optics, y_optics)
            previousOpticsFilename = opticsFilename
    OpticToThermal.displaythermalpix(x_thermal, y_thermal, thermalPath + str(nextThermal - 1) + ".png")

    toc = time.time()
    delay = toc - tic
    print('first delay: ' + str(delay))
    if delay < opticTiming:
        time.sleep(opticTiming-delay)
    toc2 = time.time()
    print('total: ' + str(toc2 - tic))

    nextThermal = OpticToThermal.MostRecentFrame() + 1

    for i in range(firstThermal, nextThermal):
        thermalFilename = thermalPath + str(i) + ".png"
        values[i] = OpticToThermal.thermalpixelstovalues(x_thermal, y_thermal, thermalFilename)

    firstThermal = nextThermal


OpticToThermal.showData(values)
