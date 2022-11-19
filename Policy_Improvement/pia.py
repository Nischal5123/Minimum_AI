import numpy as np

def pia(gamma,R,P):
    """.
    gamma: the discount factor, which is a float strictly between 0 and 1.
    the reward array R: that's a n-by-n-by-m array, where n is the number of states in the MDP and m is the number of unique actions.
    The transition probability array P: this is also n-by-n-by-m, where P(s,s',a) =  probability of transitioning to s' given that agent took action a in state s.

    """
    print(np.shape(R))
    N_STATES, N_ACTIONS, _ = np.shape(R)
    # initialize policy and value arbitrarily
    policy = [0 for s in range(N_STATES)]
    V = np.zeros(N_STATES)

    print("Initial policy", policy)
    # print V
    # print P
    # print R

    is_value_changed = True
    iterations = 0
    while is_value_changed:
        is_value_changed = False
        iterations += 1
        # run value iteration for each state
        for s in range(N_STATES):
            V[s] = sum([P[s, policy[s], s1] * (R[s, policy[s], s1] + gamma * V[s1]) for s1 in range(N_STATES)])
            # print "Run for state", s

        for s in range(N_STATES):
            q_best = V[s]
            # print "State", s, "q_best", q_best
            for a in range(N_ACTIONS):
                q_sa = sum([P[s, a, s1] * (R[s, a, s1] + gamma * V[s1]) for s1 in range(N_STATES)])
                if q_sa > q_best:
                    print("State", s, ": q_sa", q_sa, "q_best", q_best)
                    policy[s] = a
                    q_best = q_sa
                    is_value_changed = True

        print("Iterations:", iterations)
        # print "Policy now", policy

    print("Final policy")
    print(policy)
    print(V)