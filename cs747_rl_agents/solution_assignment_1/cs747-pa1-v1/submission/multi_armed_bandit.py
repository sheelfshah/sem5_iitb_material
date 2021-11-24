import numpy as np

class BernoulliArm:
    def __init__(self, p):
        self.__p = p

    def pull(self, num_pulls=1):
        return np.random.binomial(size=num_pulls, n=1, p=self.__p)

class GeneralArm:
    def __init__(self, support, probabilities):
        self.support = support
        self.__probabilities = probabilities

    def pull(self, num_pulls=1):
        return np.random.choice(self.support, p=self.__probabilities,
            size=num_pulls)

class MABandit:
    def __init__(self, filename):
        with open(filename) as f:
            file_str = f.read().strip()
        means = list(map(float, file_str.split("\n")))
        self.arms = [BernoulliArm(mean) for mean in means]
        self.__best_mean = max(means)
        self.__regret = 0

    def pull(self, arm_index, num_pulls=1):
        rewards = self.arms[arm_index].pull(num_pulls)
        self.__regret += ((self.__best_mean * num_pulls) - rewards.sum())
        return rewards

    @property
    def regret(self):
        return np.around(self.__regret, 3)

class GeneralMABandit:
    def __init__(self, filename):
        with open(filename) as f:
            file_str = f.read().strip()
        lines = file_str.split("\n")
        supports = lines[::2]
        probabilitiess = lines[1::2]

        self.__best_mean = 0
        self.arms = []
        for (support, probabilities) in zip(supports, probabilitiess):
            support = np.array(list(map(float, support.split())))
            probabilities = np.array(list(map(float, probabilities.split())))
            self.arms.append(GeneralArm(support, probabilities))
            mean = (support * probabilities).sum()
            self.__best_mean = max(self.__best_mean, mean)
        
        self.__regret = 0

    def pull(self, arm_index, num_pulls=1):
        rewards = self.arms[arm_index].pull(num_pulls)
        self.__regret += ((self.__best_mean * num_pulls) - rewards.sum())
        return rewards

    @property
    def regret(self):
        return np.around(self.__regret, 3)