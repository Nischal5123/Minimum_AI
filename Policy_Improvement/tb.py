import pia
import numpy as np
import random

"""
tb.py file which creates sample inputs gamma, matrix R and matrix P, then calls pia on these inputs.

"""


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
        """
        This naming (rather than s0, s1...) makes it easy to use states and actions as indices in an array.
        """
        states = np.arange(0, self.n_states, 1)
        actions = np.arange(0, self.n_actions, 1)

        return states, actions

    def generate_transitions(self):
        """
        P: The transition probability array P: this is also n-by-n-by-m,
        where P(s,s',a) =  probability of transitioning to s' given that agent took action a in state s.

        """
        P = np.random.rand(self.n_states, self.n_states, self.n_actions)
        self.P = (
            P / P.sum(axis=1)[:, None]
        )  # transition probability : probabilities sum to 1

    def generate_rewards(self):
        """
        the reward array R: that's a n-by-n-by-m array, where n is the number of states in the MDP and m is the number of unique actions.
        """
        self.R = np.random.randint(
            self.min_reward,
            high=self.max_reward,
            size=(self.n_states, self.n_states, self.n_actions),
        )
        # If there is no transition (s,a,s') in the MDP, then the value of R[s,s'a] is zero.
        self.R[self.P == 0] = 0






def main():  # This criterion is linked to a Learning Outcome : Testbench tb creates good test cases E.g. randomized, more than one test case

    # define number of states and actions
    number_of_states, number_of_actions = 3, 3

    # define distribution of reward  giving range to randomly pull the number from: limit int34
    minimum_reward, maximum_reward = -1000, 1000
    assert minimum_reward < maximum_reward

    # the discount factor, which is a float strictly between 0 and 1.
    gamma = float(random.uniform(0, 1))

    print(
        f"#####################  MDP designed with {number_of_states} States, {number_of_actions} Actions and gamma {gamma} ######################\n"
    )

    my_mdp = MDP(number_of_states, number_of_actions, minimum_reward, maximum_reward)
    my_mdp.generate_states_actions()
    my_mdp.generate_transitions()
    my_mdp.generate_rewards()
    print(f"REWARD: \n{my_mdp.R}\n")

    # interpretations i.e. 2 separate arguments for R and P
    pi, V = pia.pia(gamma, my_mdp.P, my_mdp.R)
    print(f"FINAL POLICY:  \n{pi}\n")
    print(f"VALUE: \n{V}")








if __name__ == "__main__":
    main()
