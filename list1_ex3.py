
from numpy import *

import real_mutation as realmut
import real_cross as realcross
import selection as selec


def objective_fun(value):
    x = value[:, 0]
    y = value[:, 1]
    return x*sin(4*pi*x) - y*sin(4*pi*y + pi) + 1

def main():
    # Population size
    N = 80
    max_mut_it = 150
    max_iteration = 190

    # Instantiating mutator operator
    mutation_op = realmut.NonUniformMutation(-1, 2, 2.5, max_mut_it)
    cross_op =  realcross.ArithmeticCrossover()
    selection_op = selec.TournamentSelection(0.2)

    # Random population in the interval [-1, 2] 
    init_solutions = 2*random.rand(N, 2) - 1;
    population = concatenate([init_solutions, zeros((init_solutions.shape[0], 1))], axis = 1)

    # Initializing sons
    sons1 = zeros((population.shape[0]/2, population.shape[1]))
    sons2 = zeros((population.shape[0]/2, population.shape[1]))
    
    fitness_tracking = zeros((max_iteration, 3))

    for i in arange(max_iteration):
    
        # Generate mutation
        population[:, 0:-1] = mutation_op.mutate(population[:, 0:-1], i)

        # Selec random individuals to cross
        individuals = random.permutation(population.shape[0])
   
        # Crossing random individuals (double the population)
        sons1[:, 0:-1], sons2[:, 0:-1] = cross_op.cross(population[individuals[0:N/2], 0:-1], population[individuals[N/2:], 0:-1])
       
        # New population with double size
        new_population = concatenate([population, sons1, sons2], axis = 0)

        # Calculating population fitness
        new_population[:, -1] = objective_fun(new_population[:, 0:-1])

        fitness_tracking[i, 0] = max(new_population[:, -1])
        fitness_tracking[i, 1] = min(new_population[:, -1])
        fitness_tracking[i, 2] = mean(new_population[:, -1])

        # Selecting individuals
        population = selection_op.select(new_population)   
        
    savetxt('fitness_evol', fitness_tracking)
if __name__ == '__main__':
    main()