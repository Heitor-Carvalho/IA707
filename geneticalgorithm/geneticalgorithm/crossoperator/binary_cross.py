
from numpy import *

class TwoPointCrossover():
    
    def cross(self, individuals1, individuals2):

        markers = random.permutation(individuals1.shape[1])[0:1]

        marker1 = min(markers)
        marker2 = max(markers)

        sons1 = c_[individuals1[:, :marker1], individuals2[:, marker1:marker2][::-1], individuals1[:, marker2:]]
        sons2 = c_[individuals2[:, :marker1][::-1], individuals1[:, marker1:marker2], individuals2[:, marker2:][::-1]]

        return (sons1, sons2)

class OnePointCrossover():
    
    def cross(self, individuals1, individuals2):

        marker = random.permutation(individuals1.shape[1])[0]

        sons1 = c_[individuals1[:, :marker], individuals2[:, marker:]]
        sons2 = c_[individuals2[:, :marker], individuals1[:, marker:]]

        return (sons1, sons2)

