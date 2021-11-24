import argparse
import numpy as np

from mdp import MDP

np.random.seed(0)

def run(mdp, algorithm):
    m = MDP(mdp)
    # default for task 2
    if algorithm is None:
        algorithm = "hpi"

    if algorithm == "vi":
        V = m.value_iteration()
        pi = m.pi_from_Q(m.Q_from_V(V))
    elif algorithm == "hpi":
        pi = m.howards_policy_iteration()
        V = m.V_from_pi(pi)
    elif algorithm == "lp":
        V = m.linear_programming()
        pi = m.pi_from_Q(m.Q_from_V(V))
    else:
        # error
        print(algorithm)
    return V, pi

if __name__ == '__main__':
    # managing args parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("--mdp", help="path to mdp instance file")
    parser.add_argument("--algorithm", help="""algorithm is one of vi, hpi, lp""")
    kwargs = vars(parser.parse_args())
    V, pi = run(**kwargs)
    for v_i, pi_i in zip(V, pi):
        print("{:.7f}".format(v_i), pi_i)