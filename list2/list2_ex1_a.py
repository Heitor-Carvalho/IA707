
from numpy import *
import copy
    
import geneticalgorithm.crossoperator.perm_cross as permcross
import geneticalgorithm.mutatoroperator.perm_mutation as permut
import geneticalgorithm.selectionoperator.selection as selec

def objective_fun(dist_matrix, population):

    for i in arange(population.shape[0]):
        path = population[i, :-1]
        path_segments = c_[roll(path, -1), path]
        population[i, -1] = -sum(dist_matrix[path_segments[:, 0].astype('int'), path_segments[:, 1].astype('int')])
    
    return population[:, -1]


def main():
        
    dist_matrix = loadtxt('dist.txt')
    max_iteration = 350


    # Instantiating genetic operators
    binmut_op = permut.ElitistPercentReverseMutation(1)
    cross_op = permcross.ElitistPMXCrossover()    
    selection_op = selec.ElitistTournamentSelection(0.75)

    # Population size
    N = 100
    
    # Generating population
    init_sol = zeros((N, dist_matrix.shape[1]))
    for i in arange(0, N):
        init_sol[i, :] = random.permutation(dist_matrix.shape[1])
       
    population = concatenate([init_sol, zeros((init_sol.shape[0], 1))], axis = 1)
    new_population = zeros((population.shape[0]*2, population.shape[1]))

    # Creating fitness tracking
    fitness_tracking = zeros((max_iteration, 3))

    import pdb; pdb.set_trace()

    for i in arange(max_iteration):
        
        # Population fitness evaluation
        population[:, -1] = objective_fun(dist_matrix, population)

        # Population mutation
        population = binmut_op.mutate(population, i)

        # Population crossover
        new_population, idx_sons = cross_op.cross(population)

        # Fitness evaluation
        new_population[:, -1] = objective_fun(dist_matrix, new_population)
        
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