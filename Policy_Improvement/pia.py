import numpy as np


def initilize_pi(P):
    """To initialize pi: for every state s, look up the actions that can be taken there, and assign pi[s,a] = 1/(number of actions available at s)"""
    nS, _, nA = np.shape(P)
    pi = np.zeros((nS, nA))  # start with all states have transitions for all actions
    for s in range(nS):
        for a in range(nA):
            for s_prime in range(nS):
                if (
                    P[s][s_prime][a]
                ) != 0:  # if  transition doesn't exist policy set to 0
                    pi[s][a] = 1

    for i in range(nS):
        available_actions_s = pi[i].sum(axis=0)
        for j in range(nA):
            if pi[i][j] != 0:
                # assign pi[s,a] = 1/(number of actions available at s)
                pi[i][j] = 1 / available_actions_s

    return pi


def policy_evaluation(P, R, policy, gamma):
    """Policy Evaluation (prediction): Compute the state Value Function for some or all states given a fixed policy.

    gamma: the discount factor, which is a float strictly between 0 and 1.
    R:the reward array: that's a n-by-n-by-m array, where n is the number of states in the MDP and m is the number of unique actions.
    P:The transition probability array: this is also n-by-n-by-m, where P(s,s',a) =  probability of transitioning to s' given that agent took action a in state s.
    policy: p[i,j]

    return V: Value function for policy V[pi]
    """
    theta = 0.000001  # to measure significane of the improvement
    max_iterations = 99999999999
    nS, _, nA = np.shape(R)  # nS: number of States, nA:number of Actions
    V = np.zeros(nS)

    # FAIL SAFE: to stop iteration even if the change of value function is never less than theta
    for i in range(int(max_iterations)):
        # Initialize a change of value function as zero
        delta = 0
        for s in range(nS):
            # initialize state-action-value
            v_sa = 0
            for a in range(nA):
                for s_prime in range(nS):
                    v_sa += (
                        (policy[s][a])
                        * P[s, s_prime, a]
                        * (R[s, s_prime, a] + gamma * V[s_prime])
                    )

            # delta:change in value of state
            delta = max(delta, np.abs(V[s] - v_sa))
            V[s] = v_sa

        # Repeat until change in value is below the threshold
        if delta < theta:
            return V


def pia(gamma, P, R):
    """
    gamma: the discount factor, which is a float strictly between 0 and 1.

    The MDP description: consists in two matrices.
    R:the reward array: that's a n-by-n-by-m array, where n is the number of states in the MDP and m is the number of unique actions.
    P:The transition probability array: this is also n-by-n-by-m, where P(s,s',a) =  probability of transitioning to s' given that agent took action a in state s.

    print Policy and Value
    """
    max_iterations = 99999999999
    nS, _, nA = np.shape(R)
    # initialize policy and value arbitrarily
    pi = initilize_pi(P)
    print(f"INITIAL POLICY \n{pi}\n")
    # FAIL SAFE: to stop iteration even if we never get a stable policy, this can be useful if the updates keep switching between 2 equally good policy
    for i in range(int(max_iterations)):
        # Evaluate current policy by computing the valur function
        V = policy_evaluation(P, R, pi, gamma)
        stable_policy = True
        # Go through each state and try to improve actions that were taken (policy Improvement)
        for s in range(nS):
            # policy action: best action for current state determined by the policy
            policy_action = np.argmax(pi[s])

            q_sa = np.zeros(nA)
            for a in range(nA):
                for s_prime in range(nS):
                    q_sa[a] += [
                        P[s, s_prime, a] * (R[s, s_prime, a] + gamma * V[s_prime])
                    ]

            # action/s that provided the best value; not based on the policy
            all_best_value_actions = (
                (np.argwhere(q_sa == np.max(q_sa))).flatten().tolist()
            )

            # if 2 or more actions are equally good in terms of action value then policy can choose any
            updated_action_probability = 1 / len(
                all_best_value_actions
            )  # if only one best value action: pick that action with probability 1/1
            pi[s] = np.zeros(nA)
            for act in all_best_value_actions:
                pi[s][act] = updated_action_probability

            if policy_action not in all_best_value_actions:
                stable_policy = False  # policy has further room to improve; not stable

        # When policy is stable: Decide on a termination criterion for the iterations - when does the code stop updating the policy?
        if stable_policy:
            print(f"FINAL POLICY:  \n{pi}\n")
            print("VALUE:  ", V)
            break
