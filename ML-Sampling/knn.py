import numpy.random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def  pairDistance(all_points):
    """given a nd array of n-dimensional points return a list of the distances ||pi - pj|| """
    distance= []
    for i in range(len(all_points)):
        for j in range(len(all_points)):
            dist=numpy.linalg.norm(all_points[i] - all_points[j])
            distance.append(dist)
    return distance


def generatePoints(d,N):
    """.Write a piece of code that will generate N data points uniformly at random in C(d)."""
  # Create an array of the given shape and populate it with random samples from a uniform distribution .

    p = numpy.random.rand(N,d)
    return p



def main(N,d):
    """ Generate N d-dimensional points , Calculate pair-wise distance , Plot Histograms"""
    all_points = generatePoints(d, N)
    data=pairDistance(all_points)
    title = "Histogram_d_{}_N_{}".format(d,N)
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



