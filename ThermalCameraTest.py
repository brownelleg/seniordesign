from PIL import Image

class OpticToThermal:
    @staticmethod
    def optictothermalpixel(x_optics: int, y_optics: int, filename: str):
        img = Image.open(filename).convert(
            'L')  # convert image to 8-bit grayscale
        WIDTH, HEIGHT = img.size
        map = img.load()
        data = list(img.getdata())  # convert image data to a list of integers
        # convert that to 2D list (list of lists of integers)
        data = [data[offset:offset + WIDTH] for offset in range(0, WIDTH * HEIGHT, WIDTH)]
        # At this point the image's pixels are all in memory and can be accessed
        x_thermal = (x_optics - 12) * (154 / 180)
        y_thermal = (y_optics - 64) * (207 / 228)
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


