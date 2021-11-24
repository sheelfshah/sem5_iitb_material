import numpy as np
from copy import deepcopy
from pulp import *

class MDP:
    # full description of an MDP, with relevant methods
    def __init__(self, filename):
        with open(filename) as f:
            file_str = f.read().strip()
        lines = file_str.split("\n")

        self.S = int(lines[0].split()[-1])
        self.A = int(lines[1].split()[-1])
        self.terminal_states = list(map(int, lines[2].split()[1:]))
        
        self.T = np.zeros((self.S, self.A, self.S))
        self.R = np.zeros((self.S, self.A, self.S))
         
        for line in lines[3:]:
            if line.startswith("transition"):
                [s1, a, s2] = list(map(int, line.split()[1:4]))
                [r, p] = list(map(float, line.split()[4:]))
                self.T[s1][a][s2] = p
                self.R[s1][a][s2] = r
            elif line.startswith("mdptype"):
                self.is_episodic = line.endswith("episodic")
            elif line.startswith("discount"):
                self.G = float(line.split()[-1])
            # else ignore
        # self.display()

    def display(self):
        print("S:", self.S)
        print("A:", self.A)
        print("T:", self.T)
        print("R:", self.R)
        print("G:", self.G)
        print("is_epsiodic:", self.is_episodic)

    def Q_from_V(self, V):
        return (self.T * (self.R + self.G * V)).sum(axis=2)

    def pi_from_Q(self, Q):
        return Q.argmax(axis=1)

    def V_from_pi(self, pi):
        A = np.zeros((self.S, self.S))
        B = np.zeros(self.S)
        for s in range(self.S):
            A[s] = self.T[s][pi[s]] * self.G
            A[s][s] -= 1
            B[s] = -(self.T[s][pi[s]] * self.R[s][pi[s]]).sum()
        return np.linalg.solve(A, B)

    def value_iteration(self, max_runs=100000, epsilon=10**-10):
        V = np.random.uniform(size=self.S)
        for i in range(max_runs):
            V_ = (self.T * (self.R + self.G * V)).sum(axis=2).max(axis=1)
            if np.sqrt(sum((V_ - V)**2)) < epsilon:
                return V_
            V = V_

    def howards_policy_iteration(self):
        pi = np.random.choice(self.A, self.S)
        while True:
            q_pi = self.Q_from_V(self.V_from_pi(pi))
            pi_ = q_pi.argmax(axis=1)
            if np.all(pi_ == pi):
                return pi_
            pi = pi_

    def linear_programming(self):
        problem = LpProblem("V_start", LpMinimize)
        value_vars = [LpVariable("v"+str(i), None, None) for i in range(self.S)]
        for s in range(self.S):
            for a in range(self.A):
                constraint = 0
                for s_ in range(self.S):
                    constraint += self.T[s][a][s_] * (
                        self.R[s][a][s_] + self.G * value_vars[s_])
                problem += (constraint <= value_vars[s])
        problem += lpSum(value_vars)
        status = problem.solve(PULP_CBC_CMD(msg=0))
        V = np.zeros(self.S)
        for i in range(self.S):
            V[i] = value(value_vars[i])
        return V