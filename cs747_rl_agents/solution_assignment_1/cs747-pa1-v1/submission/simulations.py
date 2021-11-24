from bandit import *
from itertools import product

def run_simulations(instances, algorithms, randomSeeds,
    epsilons, scales, thresholds, horizons):
    # warning: opens file in "a" mode
    f = open("outputData.txt", "a")
    for (instance, algorithm, randomSeed, epsilon, scale,
        threshold, horizon) in product(instances, algorithms, randomSeeds,
            epsilons, scales, thresholds, horizons):
        ans = run(instance, algorithm, randomSeed, epsilon, scale,
            threshold, horizon)
        f.write(ans + "\n")
        print(ans)
    f.close()

# task 1
instances = ["../instances/instances-task1/i-%d.txt" % i for i in [1, 2, 3]]
algorithms = ["epsilon-greedy-t1", "ucb-t1",
    "kl-ucb-t1", "thompson-sampling-t1"]
randomSeeds = [i for i in range(50)]
epsilons = [0.02]
scales = [2]
thresholds = [0]
horizons = [100, 400, 1600, 6400, 25600, 102400]
run_simulations(instances, algorithms, randomSeeds,
    epsilons, scales, thresholds, horizons)

# task 2
instances = ["../instances/instances-task2/i-%d.txt" % i for i in [1, 2, 3, 4, 5]]
algorithms = ["ucb-t2"]
randomSeeds = [i for i in range(50)]
epsilons = [0.02]
scales = [i * 0.02 for i in range(1, 16)]
thresholds = [0]
horizons = [10000]
run_simulations(instances, algorithms, randomSeeds,
    epsilons, scales, thresholds, horizons)

# task 3
instances = ["../instances/instances-task3/i-%d.txt" % i for i in [1, 2]]
algorithms = ["alg-t3"]
randomSeeds = [i for i in range(50)]
epsilons = [0.02]
scales = [2]
thresholds = [0]
horizons = [100, 400, 1600, 6400, 25600, 102400]
run_simulations(instances, algorithms, randomSeeds,
    epsilons, scales, thresholds, horizons)

# task 4
instances = ["../instances/instances-task4/i-%d.txt" % i for i in [1, 2]]
algorithms = ["alg-t4"]
randomSeeds = [i for i in range(50)]
epsilons = [0.02]
scales = [2]
thresholds = [0.2, 0.6]
horizons = [100, 400, 1600, 6400, 25600, 102400]
run_simulations(instances, algorithms, randomSeeds,
    epsilons, scales, thresholds, horizons)
