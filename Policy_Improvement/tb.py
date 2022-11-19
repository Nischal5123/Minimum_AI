import pia
import numpy as np



def generate_MDP(n_states,n_actions):
states = [0,1,2,3,4]
actions = [0,1]
N_STATES = len(states)
N_ACTIONS = len(actions)
P = np.zeros((N_STATES, N_ACTIONS, N_STATES))  # transition probability
R = np.zeros((N_STATES, N_ACTIONS, N_STATES))  # rewards

P[0,0,1] = 1.0
P[1,1,2] = 1.0
P[2,0,3] = 1.0
P[3,1,4] = 1.0
P[4,0,4] = 1.0


R[0,0,1] = 1
R[1,1,2] = 10
R[2,0,3] = 100
R[3,1,4] = 1000
R[4,0,4] = 1.0

gamma = 0.75


pia.pia(gamma,R,P)