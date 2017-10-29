from rider import Rider
import win32gui
import time

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