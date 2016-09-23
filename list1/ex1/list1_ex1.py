
from numpy import *
import copy
    
import geneticalgorithm.crossoperator.binary_cross as bincross
import geneticalgorithm.mutatoroperator.binary_mutation as binmut
import geneticalgorithm.selectionoperator.selection as selec

def objective_fun(objects, population):
    
    for i in arange(population.shape[0]):
        idx = population[i, :-1] > 0.5
        population[i, -1] = -abs(sum(objects[idx]) - sum(objects[~idx]))
    
    return population[:, -1]


def main():
        
    objects = loadtxt('sum_diff_order.txt')
    max_iteration = 400

    bin_mutation_par = {}
    bin_mutation_par['steps'] = array([0.1, 0.2, 0.3, 0.4, 0.8])*max_iteration
    bin_mutation_par['steps'] = bin_mutation_par['steps'].astype('int')
    bin_mutation_par['probs'] = [0.3, 0.2, 0.08, 0.025, 0.015, 0.01]

    # Instantiating genetic operators
    binmut_op = binmut.PunctualStepBinaryMutation(bin_mutation_par)
    cross_op = bincross.OnePointCrossover()    
    selection_op = selec.ElitistTournamentSelection(0.6)

    # Population size
    N = 200
    
    # Population option
    op = 1

    # Generating population
    if op == 1:
        init_sol = random.rand(N, objects.shape[0]) > 0.5
    else:
        init_sol = zeros((N, objects.shape[0]))
        i = 0
        while i < N:
            init_sol[i] = random.rand(1, objects.shape[0]) > 0.5
            if(sum(init_sol[i])/objects.shape[0] > 0.6 or sum(init_sol[i])/objects.shape[0] < 0.4):
                continue
            else:
                i += 1
    population = concatenate([init_sol, zeros((init_sol.shape[0], 1))], axis = 1)
    new_population = zeros((population.shape[0]*2, population.shape[1]))

    # Creating fitness tracking
    fitness_tracking = zeros((max_iteration, 3))

    for i in arange(max_iteration):
        
        # Population fitness evaluation
        population[:, -1] = objective_fun(objects, population)

        # Population mutation
        population = binmut_op.mutate(population, i)

        # Population crossover
        new_population, idx_sons = cross_op.cross(population)

        # Fitness evaluation
        new_population[:, -1] = objective_fun(objects, new_population)
        
        # Selecting individuals                
        population = selection_op.select(new_population)   
        
        fitness_tracking[i, 0] = max(population[:, -1])
        fitness_tracking[i, 1] = min(population[:, -1])
        fitness_tracking[i, 2] = mean(population[:, -1])
        
        print 'Max %s, Min %s, Mean %s, It %s' % (max(population[:, -1]), min(population[:, -1]), mean(population[:, -1]), i)

    savetxt('fitness_evol', fitness_tracking, fmt='%1.4f')
    savetxt('best_sol', population[argmax(population[:, -1])], fmt='%1.4f')

if __name__ == '__main__':
    main()