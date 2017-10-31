import win32gui
import cv2
import numpy
import imutils
from PIL import ImageGrab

class ImageProcessing:
    def __init__(self, windowID):
        self.windowID = windowID
        self.barHeight = 30
        self.borderWidth = 2

    def detect_points(self, width, height, data):
        off_x = int(width / 10) + 1
        off_y = int(height / 15) + 1

        return(data[off_y][off_x], data[off_y][int(width / 2)], data[off_y][width - off_x - 1],
            data[int(height / 4)][off_x], data[int(height / 4)][width - off_x - 1],
            data[int(height / 2)][off_x],  data[int(height / 2)][int(width / 2)], data[int(height / 2)][width - off_x - 1],
            data[height - off_y - 1][off_x], data[height - off_y - 1][width - off_x - 1])

    def calculate_sizes(self):
        windowCoordinates = win32gui.GetWindowRect(self.windowID)

        width = windowCoordinates[2] - windowCoordinates[0] - self.borderWidth * 2
        height = windowCoordinates[3] - windowCoordinates[1] - self.barHeight - self.borderWidth

        return (windowCoordinates[0] + self.borderWidth, 
                windowCoordinates[2] - self.borderWidth, 
                windowCoordinates[1] + self.barHeight, 
                windowCoordinates[3] - self.borderWidth, 
                width, 
                height)

    def recognize_images(self, images):

        for image in images:
            (x, y, width, height, data) = image

            if width / height < 0.3:
                print("1")
            elif width / height >= 0.78:
                print(".")
            else:
                points = self.detect_points(width, height, data)
                if (points == (255, 255, 255, 255, 255, 255, 0, 255, 255, 255)):
                    print("0")
                elif (points == (255, 255, 255, 0, 255, 255, 255, 255, 255, 255)):
                    print("2")
                elif (points == (255, 255, 255, 0, 255, 0, 255, 255, 255, 255)):
                    print("3")
                elif (points == (255, 0, 255, 255, 255, 255, 255, 255, 0, 255)):
                    print("4")
                elif (points == (255, 255, 255, 255, 0, 255, 255, 255, 255, 255)):
                    print("5")
                elif (points == (255, 0, 0, 255, 0, 255, 255, 255, 255, 255)):
                    print("6")
                elif (points == (255, 255, 255, 255, 255, 255, 255, 255, 255, 255)):
                    print("8")
                elif (points == (255, 255, 255, 255, 255, 255, 255, 255, 0, 255)):
                    print("9")
                else:
                    print("7")

                

    def prepare_numbers(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        (_, image) = cv2.threshold(image, 45, 255, cv2.THRESH_BINARY)
        cv2.imwrite("test_image.png", image)
        contours = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if imutils.is_cv2() else contours[1]
        images = []

        for contour in contours:
            (x, y, width, height) = cv2.boundingRect(contour)

            images.append((x, y, width, height, image[y:(y + height), x:(x + width)].copy()))
        
        images.sort(key=lambda x: x[0])

        self.recognize_images(images)

    def get_state(self):
        (x0, x1, y0, y1, width, height) = self.calculate_sizes()

        (r, g, b) = ImageGrab.grab((x0, y0, x0 + 1, y0 + 1)).getpixel((0, 0))

        if r < 10 and g < 10 and b < 10:
            return 1
        else:
            return 0

    def get_ending_time(self):
        (x0, x1, y0, y1, width, height) = self.calculate_sizes()

        x0 += int(width / 7)
        x1 = x0 + int(width / 3.5)
        y0 += int(height / 3.3)
        y1 = y0 + int(height / 22)

        image = numpy.array(ImageGrab.grab((x0, y0, x1, y1)))
        self.prepare_numbers(image)

    def get_normal_time(self):
        (x0, x1, y0, y1, width, height) = self.calculate_sizes()

        x0 += int(width / 1.4)
        y0 += int(height / 20)
        y1 = y0 + int(height / 30)

        image = numpy.array(ImageGrab.grab((x0, y0, x1, y1)))
        self.prepare_numbers(image)
    