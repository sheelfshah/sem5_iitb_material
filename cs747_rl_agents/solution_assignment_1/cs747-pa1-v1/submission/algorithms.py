import numpy as np

class epsilon_greedy_t1:
    def __init__(self, bandit, epsilon, horizon):
        self.bandit = bandit
        self.eps = epsilon
        self.T = horizon
        self.reward_sums = np.array([
            self.bandit.pull(i)[0] for i in range(len(self.bandit.arms))
        ])
        self.pulls = np.array([1] * len(self.bandit.arms))

    def greedy_arm(self):
        means = self.reward_sums / self.pulls
        # deterministic tie breaking
        return means.argmax()

    def random_arm(self):
        return np.random.choice(len(self.bandit.arms))

    def run(self):
        while self.pulls.sum() < self.T:
            if np.random.uniform() > self.eps:
                greedy_arm = self.greedy_arm()
                reward = self.bandit.pull(greedy_arm)[0]
                self.pulls[greedy_arm] += 1
                self.reward_sums[greedy_arm] += reward
            else:
                random_arm = self.random_arm()
                reward = self.bandit.pull(random_arm)[0]
                self.pulls[random_arm] += 1
                self.reward_sums[random_arm] += reward

class ucb_t1:
    def __init__(self, bandit, scale, horizon):
        self.bandit = bandit
        self.scale = scale
        self.T = horizon
        self.reward_sums = np.array([
            self.bandit.pull(i)[0] for i in range(len(self.bandit.arms))
        ])
        self.pulls = np.array([1] * len(self.bandit.arms))

    def ucb_greedy_arm(self, time):
        ucb = ((self.reward_sums / self.pulls) +
            np.sqrt(self.scale * np.log(time) / self.pulls))
        return ucb.argmax()

    def run(self):
        while self.pulls.sum() < self.T:
            ucb_greedy_arm = self.ucb_greedy_arm(self.pulls.sum())
            reward = self.bandit.pull(ucb_greedy_arm)[0]
            self.pulls[ucb_greedy_arm] += 1
            self.reward_sums[ucb_greedy_arm] += reward

class kl_ucb_t1:
    def __init__(self, bandit, horizon):
        self.bandit = bandit
        self.T = horizon
        self.reward_sums = np.array([
            self.bandit.pull(i)[0] for i in range(len(self.bandit.arms))
        ])
        self.pulls = np.array([1] * len(self.bandit.arms))

    def kl_ucbound(self, i, time):
        p_hat = (self.reward_sums[i] / self.pulls[i])
        if p_hat == 1:
            return p_hat

        def KL(x, y):
            if x==0 or x==1:
                return 0
            if y==1:
                return 10**10
            return x * np.log(x / y) + (1 - x) * np.log((1 - x) / (1 - y))

        max_val = (np.log(time) + 3*np.log(np.log(time))) / self.pulls[i]

        num_steps = 10
        step = (1 - p_hat) / num_steps
        for i in range(num_steps):
            q = p_hat + i*step
            if KL(p_hat, q) >= max_val:
                return q
        return 1


    def kl_ucb_greedy_arm(self, time):
        kl_ucb = np.array([
            self.kl_ucbound(i, time)
            for i in range(len(self.bandit.arms))])
        return kl_ucb.argmax()

    def run(self):
        while self.pulls.sum() < self.T:
            kl_ucb_greedy_arm = self.kl_ucb_greedy_arm(self.pulls.sum())
            reward = self.bandit.pull(kl_ucb_greedy_arm)[0]
            self.pulls[kl_ucb_greedy_arm] += 1
            self.reward_sums[kl_ucb_greedy_arm] += reward

class thompson_sampling_t1:
    def __init__(self, bandit, horizon):
        self.bandit = bandit
        self.T = horizon
        self.successes = np.array([0] * len(self.bandit.arms))
        self.failures = np.array([0] * len(self.bandit.arms))

    def run(self):
        while (self.successes.sum() + self.failures.sum()) < self.T:
            beta_samples = np.array([
                np.random.beta(self.successes[i] + 1, self.failures[i] + 1)
                for i in range(len(self.bandit.arms))
            ])
            beta_greedy_arm = beta_samples.argmax()
            reward = self.bandit.pull(beta_greedy_arm)[0]
            if reward == 1:
                self.successes[beta_greedy_arm] += 1
            else:
                self.failures[beta_greedy_arm] += 1

class alg_t3:
    def __init__(self, bandit, horizon):
        self.bandit = bandit
        self.T = horizon
        self.K = len(self.bandit.arms)
        self.reward_counts = [
            {} for _ in range(self.K)
        ]
        for i in range(self.K):
            for val in self.bandit.arms[i].support:
                self.reward_counts[i][val] = 1

    def run(self):
        for t in range(self.T):
            dir_sample_means = []
            for i in range(self.K):
                support = list(self.reward_counts[i].keys())
                reward_counts = list(self.reward_counts[i].values())
                dir_sample_means.append(np.array(support) @ np.random.dirichlet(
                    np.array(reward_counts))
                )
            dir_greedy_arm = np.argmax(dir_sample_means)
            reward = self.bandit.pull(dir_greedy_arm)[0]
            self.reward_counts[dir_greedy_arm][reward] += 1

class alg_t4:
    def __init__(self, bandit, horizon, threshold):
        self.bandit = bandit
        self.T = horizon
        self.threshold = threshold
        self.successes = np.array([0] * len(self.bandit.arms))
        self.failures = np.array([0] * len(self.bandit.arms))

    def run(self):
        while (self.successes.sum() + self.failures.sum()) < self.T:
            beta_samples = np.array([
                np.random.beta(self.successes[i] + 1, self.failures[i] + 1)
                for i in range(len(self.bandit.arms))
            ])
            beta_greedy_arm = beta_samples.argmax()
            reward = self.bandit.pull(beta_greedy_arm)[0]
            if reward > self.threshold:
                self.successes[beta_greedy_arm] += 1
            else:
                self.failures[beta_greedy_arm] += 1
        return self.successes.sum()