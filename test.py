
import numpy.random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x=[2, 3, 10, 100, 1000, 10000]
y=[0.564820029243673,
0.672834236901434,
1.257940747227836,
4.051881338676664,
12.75636183544085,
40.38160148772381

]
plt.plot(x,y,"ro-")
plt.ylabel(' Average ||pi - pj||')
plt.xlabel('d')
plt.show()
