from PIL import Image
from numpy import mean

class OpticToThermal:
    @staticmethod
    def optictothermalpixel(x_optics: int, y_optics: int, filename: str):
        # conversion factors are determined by initial calibration
        x_thermal = (x_optics - 50) * (154 / 180)
        y_thermal = (y_optics - 40) * (207 / 228)
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
