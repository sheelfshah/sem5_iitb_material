import argparse
import numpy as np
import matplotlib.pyplot as plt

from multi_armed_bandit import MABandit, GeneralMABandit
from algorithms import (
    epsilon_greedy_t1, ucb_t1, kl_ucb_t1, thompson_sampling_t1,
    alg_t3, alg_t4
    )

def run(instance, algorithm, randomSeed, epsilon, scale, threshold, horizon):
    np.random.seed(randomSeed)
    if algorithm == "epsilon-greedy-t1":
        mab = MABandit(instance)
        epsilon_greedy_t1(mab, epsilon, horizon).run()
        ans = [instance, algorithm, randomSeed, epsilon,
            scale, threshold, horizon, mab.regret, 0]
        return ", ".join(map(str, ans))
    elif algorithm == "ucb-t1" or algorithm == "ucb-t2":
        mab = MABandit(instance)
        ucb_t1(mab, scale, horizon).run()
        ans = [instance, algorithm, randomSeed, epsilon,
            scale, threshold, horizon, mab.regret, 0]
        return ", ".join(map(str, ans))
    elif algorithm == "kl-ucb-t1":
        mab = MABandit(instance)
        kl_ucb_t1(mab, horizon).run()
        ans = [instance, algorithm, randomSeed, epsilon,
            scale, threshold, horizon, mab.regret, 0]
        return ", ".join(map(str, ans))
    elif algorithm == "thompson-sampling-t1":
        mab = MABandit(instance)
        thompson_sampling_t1(mab, horizon).run()
        ans = [instance, algorithm, randomSeed, epsilon,
            scale, threshold, horizon, mab.regret, 0]
        return ", ".join(map(str, ans))
    elif algorithm == "alg-t3":
        gmab = GeneralMABandit(instance)
        alg_t3(gmab, horizon).run()
        ans = [instance, algorithm, randomSeed, epsilon,
            scale, threshold, horizon, gmab.regret, 0]
        return ", ".join(map(str, ans))
    elif algorithm == "alg-t4":
        gmab = GeneralMABandit(instance)
        highs = alg_t4(gmab, horizon, threshold).run()
        ans = [instance, algorithm, randomSeed, epsilon,
            scale, threshold, horizon, gmab.regret, highs]
        return ", ".join(map(str, ans))

if __name__ == '__main__':
    # managing args parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", help="path to intsnace file")
    parser.add_argument("--algorithm", help="""al is one of epsilon-greedy-t1,\
        ucb-t1, kl-ucb-t1, thompson-sampling-t1, ucb-t2, alg-t3, alg-t4""")
    parser.add_argument("--randomSeed", help="non-negative random seed", type=int)
    parser.add_argument("--epsilon", help="epsilon value, 0.02 if irrelevant", type=float)
    parser.add_argument("--scale", help="scaling factor for task 2", type=float)
    parser.add_argument("--threshold", help="task 4 threshold", type=float)
    parser.add_argument("--horizon", help="time horizon for the algorithm", type=int)
    kwargs = vars(parser.parse_args())
    print(run(**kwargs))