from rider import Rider
import win32gui
import time
import random

class Population:
    def __init__(self, windowID, mouse, image_processing, riders=None):
        self.riders = riders
        self.size = 5
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
        
            self.mouse.release(windowCoordinates[0] + 50, windowCoordinates[1] + windowCoordinates[3] - 50, 1)
            rider.fitness = time.time() - start_time
            time.sleep(1.0)
    
    def evaluate(self):
        weights = [rider.fitness for rider in self.riders]

        print("Scores: {}".format(weights))
        print("Max: {}".format(max(weights)))
        print("Min: {}".format(min(weights)))
        print("Average: {}".format(sum(weights) / len(weights)))
        print("")

        population = []

        for i in range(0, self.size):
            parents = random.choices(self.riders, weights=weights, k=2)
            child = parents[0].crossover(parents[1])
            child.mutation()
            population.append(child)
        
        return Population(self.windowID, self.mouse, self.image_processing, population)