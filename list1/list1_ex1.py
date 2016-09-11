
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
        
    objects = loadtxt('sum_diff.txt')
    max_iteration = 200

    bin_mutation_par = {}
    bin_mutation_par['steps'] = array([0.1, 0.2, 0.3, 0.4, 0.8])*max_iteration
    bin_mutation_par['steps'] = bin_mutation_par['steps'].astype('int')
    bin_mutation_par['probs'] = [0.3, 0.3, 0.1, 0.05, 0.02, 0.01]

    binmut_op = binmut.PunctualStepBinaryMutation(bin_mutation_par)

    cross_op = bincross.TwoPointCrossover()    
    selection_op = selec.ElitistTournamentSelection(0.6)

    N = 200

    init_sol = random.rand(N, objects.shape[0]) > 0.5

#    init_sol = zeros((N, objects.shape[0]))
#    i = 0
#    while i < N:
#        init_sol[i] = random.rand(1, objects.shape[0]) > 0.5
#        if(sum(init_sol[i])/objects.shape[0] > 0.6 or sum(init_sol[i])/objects.shape[0] < 0.4):
#            continue
#        else:
#            i += 1

    population = concatenate([init_sol, zeros((init_sol.shape[0], 1))], axis = 1)

    sons1 = zeros((population.shape[0]/2, population.shape[1]))
    sons2 = zeros((population.shape[0]/2, population.shape[1]))

    fitness_tracking = zeros((max_iteration, 3))

    for i in arange(max_iteration):

        population[:, -1] = objective_fun(objects, population)
        best = copy.copy(population[argmax(population[:, -1]), :])
        population[:, :-1] = binmut_op.mutate(population[:, :-1].astype('bool'), i)
        population[0] = best

        individuals = random.permutation(population.shape[0])

        sons1[:, 0:-1], sons2[:, 0:-1] = cross_op.cross(population[individuals[0:N/2], :-1], population[individuals[N/2:], :-1])

        new_population = concatenate([population, sons1, sons2], axis = 0)
        new_population[:, -1] = objective_fun(objects, new_population)
        
        new_population[0] = best
        
        best = copy.copy(new_population[argmax(new_population[:, -1]), :])
        population = selection_op.select(new_population)   
        population[0] = best
        
        fitness_tracking[i, 0] = max(population[:, -1])
        fitness_tracking[i, 1] = min(population[:, -1])
        fitness_tracking[i, 2] = mean(population[:, -1])
        
        print 'Max %s, Min %s, Mean %s' % (max(population[:, -1]), min(population[:, -1]), mean(population[:, -1]))

    savetxt('fitness_evol', fitness_tracking)





if __name__ == '__main__':
    main()