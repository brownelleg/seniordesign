from PIL import Image
import os
import time

#os.system("sudo /home/pi/libseek-thermal-master/build/examples/seek_snapshot")
#time.sleep(2)

img = Image.open('/home/pi/PycharmProjects/seniordesign/Elizabeth.5MeterThermal.png').convert('L')  # convert image to 8-bit grayscale
WIDTH, HEIGHT = img.size
map = img.load()

data = list(img.getdata()) # convert image data to a list of integers
# convert that to 2D list (list of lists of integers)
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

# At this point the image's pixels are all in memory and can be accessed
# individually using data[row][col].

# For example:
for row in data:
    print(' '.join('{:3}'.format(value) for value in row))

x_optics = 155
y_optics = 199

x_thermal = (-.0291*x_optics*x_optics) + (11.06*x_optics) - 931.3
y_thermal = (-.03125*x_optics*x_optics) + (12.54*x_optics) - 1186
map[x_thermal+1, y_thermal] = 0
map[x_thermal-1, y_thermal] = 0
map[x_thermal-1, y_thermal+1] = 0
map[x_thermal+1, y_thermal+1] = 0
map[x_thermal, y_thermal+1] = 0
map[x_thermal, y_thermal-1] = 0
map[x_thermal+1, y_thermal-1] = 0
map[x_thermal-1, y_thermal-1] = 0
map[x_thermal, y_thermal] = 255
img.show()



# Here's another more compact representation.
print(img.size)
