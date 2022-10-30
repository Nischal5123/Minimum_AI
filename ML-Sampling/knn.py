from typing import List

import numpy.random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#https://martin-thoma.com/curse-of-dimensionality/

def  pairDistance(all_points):
    """the distances ||pi - pj|| """
    distance= []
    for i in range(len(all_points)):
        for j in range(len(all_points)):
            dist=numpy.linalg.norm(all_points[i] - all_points[j])
            distance.append(dist)
    return distance


def generatePoints(d,N):
    """.Write a piece of code that will generate N data points uniformly at random in C(d)."""
  # Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

    p = numpy.random.rand(N,d)
    return p

def main(N,d):
    all_points = generatePoints(d, N)
    data=pairDistance(all_points)
    title = "Histogram_" + str(d) + "_" + str(N)

    plt.hist(data, density=True)
    plt.ylabel('Frequency')
    plt.xlabel('Distances')
    plt.title(title)
    plt.savefig('{}.png'.format(title))
    plt.clf()

if __name__=="__main__":
    #Leave N and d as variables that can be set, don't hard-code them. For generating your experiments, set N=100.
    N=100
    for d in [2, 3, 10, 100, 1000, 10000]:
     main(N,d)


