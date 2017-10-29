import random

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