


from numpy import *

import real_mutation as realmut
import real_cross as realcross

import fitness as fit


def objective_fun(x):
    return x**2 + 25*x + 12

def main():
    set_printoptions(precision=4)

    # Creating individuals in ther original representation 
    init_solutions = array([linspace(-30, 20, 5)])
    
	init_population = concatenate([init_solutions, zeros(init_solutions.shape)], axis = 0)
    population_size = init_population.shape[1]

    # Instantiating real mutation class
    real_mut = realmut.GaussianMutation(1)
    real_mut = realmut.UniformMutation(0,1)

    # Instatiating real crossover 
    real_cross = realcross.ArithmeticCrossover(0.5)
    

#    print real_mut.mutate(init_population[0:1, :])
#    print real_cross.cross(init_population[0:1, random.permutation(population_size)], init_population[0:1, random.permutation(population_size)])
    max_escal = fit.MaxInvEscal(objective_fun)
    adjust = fit.AdustFitness()
    normal = fit.NoramlFitness()
#    print max_escal.escalonate(init_population[0:1, :])    
    fitness = max_escal.escalonate(init_population[0:1, :])    
    adjusted_fitness = adjust.adjust(fitness)
    normalized_fitness = normal.normalize(adjusted_fitness)
    print fitness, adjusted_fitness, normalized_fitness
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    main()