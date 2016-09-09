
from numpy import *

class OxCrossover():

    def cross(self, individuals1, individuals2):

        permutation = random.permutation(individuals1.shape[1])[0:2]
        marker1 = min(permutation)
        marker2 = max(permutation)

        sons1 = c_[individuals1[:, :marker1], individuals2[:, marker1:marker2], individuals1[:, marker2:][::-1]]
        sons2 = c_[individuals2[:, :marker1][::-1], individuals1[:, marker1:marker2][::-1], individuals2[:, marker2:]]

        return (sons1, sons2)

