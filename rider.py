from pymouse import PyMouse
from PIL import ImageGrab
import win32gui
import random
import time

class Rider:
    def __init__(self, dna=None):
        self.fitness = 0
        self.dna = dna

        if not dna:
            self.init()
    
    def init(self):
        self.dna = []

        for i in range(0, 30*30):
            self.dna.append(bool(random.getrandbits(1)))

class Population:
    def __init__(self, windowID, mouse, riders=None):
        self.riders = riders
        self.size = 20
        self.windowID = windowID
        self.mouse = mouse

        if not riders:
            self.init()

    def init(self):
        self.riders = []

        for i in range(0, self.size):
            self.riders.append(Rider())

    def run(self):
        windowCoordinates = win32gui.GetWindowRect(self.windowID)

        for genom in self.riders[0].dna:
            if genom:
                self.mouse.press(windowCoordinates[0] + 50, windowCoordinates[1] + windowCoordinates[3] - 50, 1)
            else:
                self.mouse.release(windowCoordinates[0] + 50, windowCoordinates[1] + windowCoordinates[3] - 50, 1)
            time.sleep(0.0333)
        self.mouse.release(windowCoordinates[0] + 50, windowCoordinates[1] + windowCoordinates[3] - 50, 1)




if __name__ == '__main__':
    mouse = PyMouse()
    windowID = win32gui.FindWindow(None, 'NoxPlayer')
    windowCoordinates = win32gui.GetWindowRect(windowID)
    img = ImageGrab.grab(windowCoordinates)
    img.save("score.png")
    population = Population(windowID, mouse)
    #population.run()

    print(population.riders)