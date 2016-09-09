

from numpy import *
import matplotlib.pyplot as plt

def main():
    fitness = loadtxt('fitness_evol')
    plt.plot(fitness)
    plt.show()


if __name__ == '__main__':
    main()