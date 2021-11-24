import argparse
import numpy as np

def run(value_policy, states, player_id):
    print(player_id)
    
    with open(value_policy) as f:
        value_policy_str = f.read().strip()
    with open(states) as f:
        states_str = f.read().strip()
    
    states = states_str.split("\n")
    value_policies = value_policy_str.split("\n")
    for i, state in enumerate(states):
        print(state, end=" ")
        a = int(value_policies[i].split()[-1])
        policy = ['0'] * 9
        policy[a] = '1'
        print(" ".join(policy))


if __name__ == '__main__':
    # managing args parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("--value-policy", help="path to value-policy")
    parser.add_argument("--states", help="path to state file")
    parser.add_argument("--player-id", help="id of player whose policy is generated")
    kwargs = vars(parser.parse_args())
    run(**kwargs)