# Recall there are three variables, x1, x2 and x3.
#
# The objective is f(x) = x1*(S1-C1) + x2*(S2-C2)+x3*(S3-C3).
#
# The constraints are x1 >= 0, x2 >= 0, x3 >= 0, x1*C1 + x2*C2 + x3*C3 <= 3,000,000.
#
# Use the following values: S1 = 100, S2 = 200, S3 = 300, C1 = 50, C2 = 55, C3 = 75.
#
# Solve the problem a second time, but with parameter values S1 = 50, S2 = 201, S3 = 200, C1 = 52.4, C2 = 55, C3 = 75.
# Import packages.
import cvxpy as cp
import numpy as np


def factory_assignment(S,C):
    n = 3 #number of decision variable : x1,x2,x3
    A = np.array(C)
    b = 3000000 #Max cost constraint
    c=[]  # get Sk-Ck
    for Sk,Ck in zip(S,C):
        c.append(Sk-Ck)

    c=np.array(c)  #need nd array to run transpose

    # Define and solve the CVXPY problem.
    x = cp.Variable(n,nonneg=True)  #constarint: x1 , x2 , x3 => 0
    prob = cp.Problem(cp.Maximize(c.T@x),
                      [A @ x <= b]) #constraint: x1*C1 + x2*C2 + x3*C3 <= 3,000,000.
    prob.solve()

    # Print result.
    print("\nThe optimal objective function value is:", prob.value)
    print("\nA solution x , the optimizer x*")
    print(x.value)
    print("##########################################################")

def main():
    factory_assignment([100,200,300],[50,55,75])  #parameters 1  [S1,S2,S3],[C1,C2,C3]
    factory_assignment([50,201,200],[52.4,55,75]) #parameters 2  [S1,S2,S3],[C1,C2,C3]


if __name__=="__main__":
    main()