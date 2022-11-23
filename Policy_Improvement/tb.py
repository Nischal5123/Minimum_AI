import pia
import numpy as np
import random


class MDP:

    """
    The MDP description: consists in two matrices.
    the reward array R: that's a n-by-n-by-m array, where n is the number of states in the MDP and m is the number of unique actions.
    R[s,s',a] = the reward for going from s to s' by taking action a.
    If there is no transition (s,a,s') in the MDP, then the value of R[s,s'a] is zero.

    """

    def __init__(self, n_states, n_actions, min_reward=-100, max_reward=100):
        self.n_states = n_states
        self.n_actions = n_actions
        self.max_reward = max_reward
        self.min_reward = min_reward
        self.P = None
        self.R = None

    def generate_states_actions(self):
        states = np.arange(0, self.n_states, 1)
        actions = np.arange(0, self.n_actions, 1)

        return states, actions

    def generate_transitions(self):
        P = np.random.rand(self.n_states, self.n_states, self.n_actions)
        self.P = (
            P / P.sum(axis=1)[:, None]
        )  # transition probability : probabilities sum to 1

    def generate_rewards(self):
        self.R = np.random.randint(
            self.min_reward,
            high=self.max_reward,
            size=(self.n_states, self.n_states, self.n_actions),
        )
        # If there is no transition (s,a,s') in the MDP, then the value of R[s,s'a] is zero.
        self.R[self.P == 0] = 0


def main():

    # define number of states and actions
    number_of_states, number_of_actions = 5, 3

    # define distribution of reward  -inf to +inf for test -100 to +100
    minimum_reward, maximum_reward = -100, 100
    assert minimum_reward < maximum_reward

    gamma = random.uniform(0, 1)

    print(
        f"#####################  MDP designed with {number_of_states} States, {number_of_actions} Actions and gamma {gamma} ######################\n"
    )

    my_mdp = MDP(number_of_states, number_of_actions, minimum_reward, maximum_reward)
    my_mdp.generate_states_actions()
    my_mdp.generate_transitions()
    my_mdp.generate_rewards()

    pia.pia(gamma, my_mdp.P, my_mdp.R)


# #basic test
#     gamma=0.9
#     P = np.zeros((number_of_states, number_of_states, number_of_actions))
#     P[0, 1, 0] = 0.3
#     P[1, 2, 1] = 0.5
#     P[2, 3, 0] = 0.5
#     P[3, 4, 1] = 0.5
#     P[4, 4, 0] = 0.34
#     P[0, 1, 2] = 0.4
#     P[1, 2, 0] = 0.5
#     P[2, 3, 1] = 0.5
#     P[3, 4, 0] = 0.5
#     P[4, 4, 2] = 0.33
#     P[4, 4, 1] = 0.33
#     R = np.copy(P)  # rewards
#     R[R > 0] = 10
#     pia.pia(gamma, P, R)


if __name__ == "__main__":
    main()
