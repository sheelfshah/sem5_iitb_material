import numpy as np
import matplotlib.pyplot as plt

def default_plot(plot_lines, title="", xlabel="Horizon", ylabel="Regret", xlog=True):
    data = {}
    for line in plot_lines:
        (instance, algorithm, randomSeed, epsilon,
            scale, threshold, horizon, regret, highs) = line.split(", ")
        randomSeed = int(randomSeed)
        epsilon = float(epsilon)
        scale = float(scale)
        threshold = float(threshold)
        horizon = int(horizon)
        regret = float(regret)
        highs = int(highs)
        if algorithm in data:
            if horizon in data[algorithm]:
                data[algorithm][horizon].append(regret)
            else:
                data[algorithm][horizon] = [regret]
        else:
            data[algorithm] = {horizon: [regret]}

    for algorithm in data:
        for horizon in data[algorithm]:
            data[algorithm][horizon] = sum(data[algorithm][horizon]) /\
                len(data[algorithm][horizon])
        plt.plot(list(data[algorithm].keys()),
            list(data[algorithm].values()), label=algorithm)
    if xlog:
        plt.xscale("log")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.show()

def t2_plot(plot_lines, title="", xlabel="Scale", ylabel="Regret"):
    data = {}
    for line in plot_lines:
        (instance, algorithm, randomSeed, epsilon,
            scale, threshold, horizon, regret, highs) = line.split(", ")
        randomSeed = int(randomSeed)
        epsilon = float(epsilon)
        scale = float(scale)
        threshold = float(threshold)
        horizon = int(horizon)
        regret = float(regret)
        highs = int(highs)
        if instance in data:
            if scale in data[instance]:
                data[instance][scale].append(regret)
            else:
                data[instance][scale] = [regret]
        else:
            data[instance] = {scale: [regret]}

    for instance in data:
        min_regret = 10**10
        best_scale = -1
        for scale in data[instance]:
            data[instance][scale] = sum(data[instance][scale]) /\
                len(data[instance][scale])
            if data[instance][scale] < min_regret:
                min_regret = data[instance][scale]
                best_scale = scale
        print(instance, best_scale)
        plt.plot(list(data[instance].keys()),
            list(data[instance].values()), label=instance)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.show()

def t4_plot(plot_lines, title="", xlabel="Horizon", ylabel="Highs_Regret", xlog=True):
    data = {}
    for line in plot_lines:
        (instance, algorithm, randomSeed, epsilon,
            scale, threshold, horizon, regret, highs) = line.split(", ")
        randomSeed = int(randomSeed)
        epsilon = float(epsilon)
        scale = float(scale)
        threshold = float(threshold)
        horizon = int(horizon)
        regret = float(regret)
        highs = int(highs)
        if threshold in data:
            if horizon in data[threshold]:
                data[threshold][horizon].append(highs)
            else:
                data[threshold][horizon] = [highs]
        else:
            data[threshold] = {horizon: [highs]}

    with open(instance) as f:
        file_str = f.read().strip()
    lines = file_str.split("\n")
    supports = lines[::2]
    probabilitiess = lines[1::2]

    for threshold in data:
        best_highs = 0
        for (support, probabilities) in zip(supports, probabilitiess):
            support = np.array(list(map(float, support.split())))
            probabilities = np.array(list(map(float, probabilities.split())))
            exp_highs = 0
            print(threshold)
            for val, prob in zip(support, probabilities):
                if val>threshold:
                    exp_highs += prob
            print(exp_highs)
            best_highs = max(best_highs, exp_highs)

        for horizon in data[threshold]:
            data[threshold][horizon] = sum(data[threshold][horizon]) /\
                len(data[threshold][horizon])
            data[threshold][horizon] = best_highs * horizon -\
                data[threshold][horizon]
        plt.plot(list(data[threshold].keys()),
            list(data[threshold].values()))
        if xlog:
            plt.xscale("log")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title + str(threshold))
        plt.show()

with open("outputData.txt") as f:
    file_str = f.read()

lines = file_str.strip().split("\n")

# # task 1
# t1_i1_lines = lines[:1200]
# default_plot(t1_i1_lines, title="Task 1 - Instance 1")
# t1_i2_lines = lines[1200:2400]
# default_plot(t1_i2_lines, title="Task 1 - Instance 2")
# t1_i3_lines = lines[2400:3600]
# default_plot(t1_i3_lines, title="Task 1 - Instance 3")

# # task 2
# t2_lines = lines[3600:3600+3750]
# t2_plot(t2_lines, title="Task 2")

# # task 3
# t3_i1_lines = lines[3600+3750:3600+3750+300]
# default_plot(t3_i1_lines, title="Task 3 - Instance 1")
# t3_i2_lines = lines[3600+3750+300:3600+3750+600]
# default_plot(t3_i2_lines, title="Task 3 - Instance 2")

# task 4
t4_i1_lines = lines[3600+3750+600:3600+3750+600+600]
t4_plot(t4_i1_lines, title="Task 4 - Instance 1 - Threshold ")
t4_i2_lines = lines[3600+3750+600+600:3600+3750+600+1200]
t4_plot(t4_i2_lines, title="Task 4 - Instance 2 - Threshold ")