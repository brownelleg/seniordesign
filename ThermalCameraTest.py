from PIL import Image
from numpy import mean
import matplotlib.pyplot as plt
from moving_average import exponential_moving_avereage, moving_average

class OpticToThermal:
    @staticmethod
    def optictothermalpixel(x_optics: int, y_optics: int):
        # conversion factors are determined by initial calibration
        x_thermal = (x_optics - 115) * (154 / 295)
        y_thermal = (y_optics - 66) * (207 / 383)
        thermalpix = [x_thermal, y_thermal]
        return thermalpix

    @staticmethod
    def thermalpixelstovalues(x_thermal: int, y_thermal: int, filename: str):
        img2 = Image.open(filename)
        pix = img2.load()
        total = pix[x_thermal, y_thermal]
        total += pix[x_thermal + 1, y_thermal]
        total += pix[x_thermal - 1, y_thermal]
        total += pix[x_thermal - 1, y_thermal + 1]
        total += pix[x_thermal + 1, y_thermal + 1]
        total += pix[x_thermal, y_thermal + 1]
        total += pix[x_thermal, y_thermal - 1]
        total += pix[x_thermal + 1, y_thermal - 1]
        total += pix[x_thermal - 1, y_thermal - 1]
        total += pix[x_thermal + 2, y_thermal]
        total += pix[x_thermal - 2, y_thermal]
        total += pix[x_thermal - 2, y_thermal + 2]
        total += pix[x_thermal + 2, y_thermal + 2]
        total += pix[x_thermal - 2, y_thermal + 1]
        total += pix[x_thermal + 2, y_thermal + 1]
        total += pix[x_thermal, y_thermal + 2]
        total += pix[x_thermal, y_thermal - 2]
        total += pix[x_thermal + 2, y_thermal - 2]
        total += pix[x_thermal - 2, y_thermal - 2]
        total += pix[x_thermal + 2, y_thermal - 1]
        total += pix[x_thermal - 2, y_thermal - 1]
        value = mean(total)
        return value

    @staticmethod
    def displaythermalpix(x_thermal: int, y_thermal: int, filename: str):
        img = Image.open(filename).convert(
            'L')  # convert image to 8-bit grayscale
        WIDTH, HEIGHT = img.size
        map = img.load()
        data = list(img.getdata())  # convert image data to a list of integers
        # convert that to 2D list (list of lists of integers)
        data = [data[offset:offset + WIDTH] for offset in range(0, WIDTH * HEIGHT, WIDTH)]
        # place a white circle around the pixels located by the thermal camera in the nostril
        map[x_thermal + 1, y_thermal] = 0
        map[x_thermal - 1, y_thermal] = 0
        map[x_thermal - 1, y_thermal + 1] = 0
        map[x_thermal + 1, y_thermal + 1] = 0
        map[x_thermal, y_thermal + 1] = 0
        map[x_thermal, y_thermal - 1] = 0
        map[x_thermal + 1, y_thermal - 1] = 0
        map[x_thermal - 1, y_thermal - 1] = 0
        map[x_thermal, y_thermal] = 255
        img.show()

    @staticmethod
    def calculateBreathRate(input_data, median_line):
        u = 0
        RR = 0
        p = 0

        for u in range(210):
            if p == 0:
                if input_data[u] > median_line[u]:
                    p = 1
                    RR = RR + 1
            if p == 1:
                if median_line[u] > input_data[u]:
                    p = 0
                    RR = RR + 1

        return RR

    @staticmethod
    def showData(data):
        n = 8
        a = 80

        new_data_weight = moving_average(data, a)
        new_data = exponential_moving_avereage(data, n)

        OpticToThermal.calculateBreathRate(new_data, new_data_weight)
        print("Breath Rate: " + str(OpticToThermal.calculateBreathRate(new_data, new_data_weight)))

        plt.plot(data, label='Original Pixel Values')
        plt.plot(new_data_weight, label='Weight Filtered data')
        plt.plot(new_data, label='Smoothed Pixel Values')
        plt.legend()
        plt.show()
