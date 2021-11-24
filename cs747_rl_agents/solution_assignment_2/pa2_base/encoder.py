import argparse
import numpy as np

def run(policy, states):
    with open(policy) as f:
        policy_str = f.read().strip()
    with open(states) as f:
        states_str = f.read().strip()
    
    states = states_str.split("\n")
    state_indices = {}
    for i, state in enumerate(states):
        state_indices[state] = i
    S = len(states)
    # state S is terminal state for win
    # state S+1 is terminal for loss/draw
    
    policy = {}
    for line in policy_str.split("\n")[1:]:
        words = line.split()
        policy[words[0]] = list(map(float, words[1:]))

    opponent = policy_str[0]
    player = '1' if opponent == '2' else '2'

    print("numStates", S+2)
    print("numActions 9")
    print("end", S, S+1)

    for s in states:
        for a in range(9):
            if s[a] != '0':
                # illegal moves incurs negative reward and ends episode
                print("transition", state_indices[s], a, S+1, -100, 1)
                continue
            s_for_opp = s[:a] + player + s[a+1:]
            if s_for_opp in policy:
                # opp can play
                win_prob, draw_prob = 0, 0
                for a_opp, prob in enumerate(policy[s_for_opp]):
                    if prob > 0:
                        s_ = s_for_opp[:a_opp] + opponent + s_for_opp[a_opp+1:]
                        if s_ in state_indices:
                            # s_ is valid for player
                            print("transition", state_indices[s],
                                a, state_indices[s_], 0, prob)
                        else:
                            if player_wins(s_, opponent):
                                win_prob += prob
                            else:
                                # invalid state, but not win => draw
                                draw_prob += prob
                    # else ignore
                print("transition", state_indices[s], a, S, 1, win_prob)
                print("transition", state_indices[s], a, S+1, 0, draw_prob)
            else:
                # player loses/draws
                print("transition", state_indices[s], a, S+1, 0, 1)

    print("mdptype episodic")
    print("discount 1")

def player_wins(state, opponent):
    if (state[0]==opponent) and (state[1]==opponent) and (state[2]==opponent):
        return True
    if (state[3]==opponent) and (state[4]==opponent) and (state[5]==opponent):
        return True
    if (state[6]==opponent) and (state[7]==opponent) and (state[8]==opponent):
        return True
    if (state[0]==opponent) and (state[3]==opponent) and (state[6]==opponent):
        return True
    if (state[1]==opponent) and (state[4]==opponent) and (state[7]==opponent):
        return True
    if (state[2]==opponent) and (state[5]==opponent) and (state[8]==opponent):
        return True
    if (state[0]==opponent) and (state[4]==opponent) and (state[8]==opponent):
        return True
    if (state[2]==opponent) and (state[4]==opponent) and (state[6]==opponent):
        return True
    return False

if __name__ == '__main__':
    # managing args parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy", help="path to policy file of opponent")
    parser.add_argument("--states", help="path to state file")
    kwargs = vars(parser.parse_args())
    run(**kwargs)