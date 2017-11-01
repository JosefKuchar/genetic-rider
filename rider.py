import random

class Rider:
    def __init__(self, dna=None):
        self.fitness = 0
        self.mutation_rate = 0.01
        self.dna = dna

        if not dna:
            self.init()
    
    def init(self):
        self.dna = []

        for i in range(0, 30*30):
            self.dna.append(bool(random.getrandbits(1)))

    def crossover(self, rider):
        mid_point = random.randint(0, len(self.dna))
        child_dna = []

        for i in range(0, len(self.dna)):
            if i < mid_point:
                child_dna.append(self.dna[i])
            else:
                child_dna.append(rider.dna[i])
        
        return Rider(child_dna)
    
    def mutation(self):
        for genom in self.dna:
            if (random.random() <= self.mutation_rate):
                genom = bool(random.getrandbits(1))