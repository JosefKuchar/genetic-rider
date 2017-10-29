from pymouse import PyMouse
import win32gui
from population import Population
from image_processing import ImageProcessing

if __name__ == '__main__':
    mouse = PyMouse()
    windowID = win32gui.FindWindow(None, 'NoxPlayer')
    population = Population(windowID, mouse)
    processor = ImageProcessing(windowID)

    processor.get_normal_time()
    #population.run()

    print(population.riders)