p = int(input("enter player: "))
o = 3-p
o_p = input("enter oppponent policy:")
print(f"""py encoder.py --policy data/attt/policies/p{o}_policy{o_p}.txt --states data/attt/states/states_file_p{p}.txt > trial/encoded_p{p}_policy{o_p}.txt
py planner.py --mdp trial/encoded_p{p}_policy{o_p}.txt > trial/planned_p{p}_policy{o_p}.txt
py decoder.py --value-policy trial/planned_p{p}_policy{o_p}.txt --states data/attt/states/states_file_p{p}.txt --player-id {p} > trial/decoded_p{p}_policy{o_p}.txt
py attt.py -p{o} data/attt/policies/p{o}_policy{o_p}.txt -p{p} trial/decoded_p{p}_policy{o_p}.txt""")