import sys
import subprocess
import os

states_path = {
    1: "data/attt/states/states_file_p1.txt",
    2: "data/attt/states/states_file_p2.txt"
}

def run(states, policy, player, run_id):
    cmd_encoder = "python", "encoder.py", "--policy", policy, "--states", states
    print("Generating the MDP encoding using encoder.py")
    f = open('task3_attt_mdp', 'w')
    subprocess.call(cmd_encoder, stdout=f)
    f.close()

    cmd_planner = "python", "planner.py", "--mdp", "task3_attt_mdp"
    print("Generating the value policy file using planner.py using default algorithm")
    f = open('task3_attt_planner', 'w')
    subprocess.call(cmd_planner, stdout=f)
    f.close()

    cmd_decoder = "python", "decoder.py", "--value-policy", "task3_attt_planner", "--states", states, "--player-id", str(
        player)
    print("Generating the decoded policy file using decoder.py")
    f = open('task3_attt_policy_' + str(run_id), 'w')
    subprocess.call(cmd_decoder, stdout=f)
    f.close()

    f = open('task3_attt_planner', 'r')
    v_0 = f.read().split()[0]
    print(f"Player : {player}, Value of corresponding state 0: {v_0}")
    f.close()

    os.remove('task3_attt_mdp')
    os.remove('task3_attt_planner')
    return 'task3_attt_policy_' + str(run_id)

def one_up(current_policy_path, current_player, run_id):
    print(f"Learning p{current_player}'s policy in run {run_id}")
    new_policy_path = run(states_path[current_player],
        current_policy_path, current_player, run_id)
    print()
    return new_policy_path, 3 - current_player

# these parameters are varied
current_policy_path = "data/attt/policies/p2_policy1.txt"
current_player = 1
runs = 20

for run_id in range(runs):
    current_policy_path, current_player = one_up(
        current_policy_path, current_player, run_id)

with open('task3_attt_policy_' + str(run_id)) as f:
    p1 = f.read()

with open('task3_attt_policy_' + str(run_id-2)) as f:
    p2 = f.read()

with open('task3_attt_policy_' + str(run_id-1)) as f:
    p3 = f.read()

with open('task3_attt_policy_' + str(run_id-3)) as f:
    p4 = f.read()

print("Has player's policy converged:", p1==p2)
print("Has opponent's policy converged:", p3==p4)
print("""The initial policy and start player were varied and
    for each case, both policies were found to converge.
    Now, attt.py was used to manually play against the final policies
    or make the policies play each other and based on this
    conclusions about the converged policies were drawn""")
# results are in the report