from rider import Rider
import win32gui
import time

class Population:
    def __init__(self, windowID, mouse, image_processing, riders=None):
        self.riders = riders
        self.size = 20
        self.windowID = windowID
        self.mouse = mouse
        self.image_processing = image_processing

        if not riders:
            self.init()

    def init(self):
        self.riders = []

        for i in range(0, self.size):
            self.riders.append(Rider())

    def run(self):
        windowCoordinates = win32gui.GetWindowRect(self.windowID)
        

        for rider in self.riders:
            start_time = time.time()
        
            for genom in rider.dna:
                if self.image_processing.get_state() == 1:
                    break

                if genom:
                    self.mouse.press(windowCoordinates[0] + 50, windowCoordinates[1] + windowCoordinates[3] - 50, 1)
                else:
                    self.mouse.release(windowCoordinates[0] + 50, windowCoordinates[1] + windowCoordinates[3] - 50, 1)
                time.sleep(0.033333)
        
            print(time.time() - start_time)
            time.sleep(1.0)
            self.mouse.release(windowCoordinates[0] + 50, windowCoordinates[1] + windowCoordinates[3] - 50, 1)