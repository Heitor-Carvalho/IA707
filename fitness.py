from numpy import *

class OptKnowEscal(object):
    
    def __init__(self, func, max_fit):
        self.object_fun = func
        self.max_fit = max_fit

    def escalonate(self, individuals):

        return self.max_fit - self.func(individuals) 
        
class MaxUntilEscal(object):
    
    def __init__(self, func):
        self.object_fun = func
        self.max_fit = None
    
    def escalonate(self, individuals):
        
        if(self.max_fit is None):
            fitness = self.object_fun(individuals)
        else:
            fitness = self.max_fit - self.object_fun(individuals) 
        import pdb; pdb.set_trace()
        self.max_fit = fitness.max()

        return fitness

class MinInvEscal(object):
    
    def __init__(self, func):
        self.object_fun = func
        self.min_fit = None
    
    def escalonate(self, individuals):

        if(self.max_fit is None):
            fitness = 1/(1 + self.object_fun(individuals))
        else:
            fitness = 1/(1 + self.object_fun(individuals) - self.min_fit)

        self.min_fit = max(fitness)

        return fitness

class MaxInvEscal(object):
    
    def __init__(self, func):
        self.object_fun = func
        self.max_fit = None
    
    def escalonate(self, individuals):

        if(self.max_fit is None):
            fitness = 1/(1 + self.object_fun(individuals))
        else:
            fitness = 1/(1 + self.max_fit - self.object_fun(individuals))

        self.min_fit = max(fitness)

        return fitness

class  AdustFitness(object):
    
    def adjust(self, fitness):
        
        return 1/(1 + fitness)

class NoramlFitness(object):

    def normalize(self, fitness):

        return fitness/sum(fitness)


class FitnessFactory(object):

    def __init__(self, escalonate_tp, func):
        
        if(escalonate_tp == "OptKnow"):
            self.escal = OptKnow(func, self.fitness_par["extra"])
        elif(escalonate_tp == "MaxUntilEscal"):
            self.escal = MaxUntilEscal(func)
        elif(escalonate_tp == "MinInvEscal"):
            self.escal = MinInvEscal(func)
        elif(escalonate_tp == "MaxInvEscal"):
            self.escal = MaxInvEscal(func)
        else:
            error("Not valid escalonate function")

        self.normal = NoramlFitness()

        self.adjust = AdustFitness()

    def calculate(self, individuals):
        fitness = self.escal.escalonate(individuals) 
        adt_fitness = self.adjust.adjust(fitness)
        return self.normal.normalize(fitness)

