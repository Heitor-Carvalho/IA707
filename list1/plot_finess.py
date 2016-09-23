

from numpy import *
import matplotlib.pyplot as plt

import glob 

def main():
    files = glob.glob('/home/heitor/Repo/IA707/list1/ex3/list1_ex3_fitness/fitness_evol*')
    i = 1
    for file in files:
    	print 'Saving figure from file: ', file
        fitness = loadtxt(file)

        fit_plot1 = plt.plot(fitness[:, 0], label='Best fitness')
        fit_plot2 = plt.plot(fitness[:, 1], label='Worst fitness')
        fit_plot3 = plt.plot(fitness[:, 2], label='Average fitness')
        plt.setp(fit_plot1, linewidth=2)
        plt.setp(fit_plot2, linewidth=2)
        plt.setp(fit_plot3, linewidth=2)
        plt.legend(loc=2)
        plt.axis([0, fitness.shape[0], 0, 4.5])
        plt.savefig('fitness_eval' + str(i))
        plt.clf()
        i += 1


if __name__ == '__main__':
    main()