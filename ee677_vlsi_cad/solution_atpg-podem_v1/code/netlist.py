gate_ids = {
    "and2_": 3, "not": 1, "nand4_": 8, "nand2_": 5
}

def read_text_netlist(filename):
    """converts txt file to netlist of strs
    returns [[node_id, gate_type, connected_nodes]]
    """
    with open(filename) as f:
        f_str = f.readlines()
    
    identifier = 0
    netlist = []
    for line in f_str:
        temp_str = ''
        device = []
        
        if line=="\n":
            continue
        device.append(identifier)
        device += line.strip().split()
        identifier += 1
        netlist.append(device)
    return netlist

def netlist_to_nodes(netlist):
    """converts str based netlist to int based
    i.e. each gate/node is mapped to an int
    """
    global gate_ids
    count = 1
    old_nodes = []
    new_nodes = []
    inputs = []
    outputs = []
    node_map = [[]]
    for device in netlist:
        gate = device[1][:-1]
        device[1] = gate_ids[gate]

        for i in range(2, len(device)):
            if device[i].startswith("in"):
                if device[i] in old_nodes:
                    device[i] = new_nodes[old_nodes.index(device[i])]
                else:
                    inputs.append(count)
                    old_nodes.append(device[i])
                    new_nodes.append(count)
                    device[i] = count
                    count += 1

            elif device[i].startswith("out"):
                if device[i] in old_nodes:
                    device[i] = new_nodes[old_nodes.index(device[i])]
                else:
                    outputs.append(count)
                    old_nodes.append(device[i])
                    new_nodes.append(count)
                    device[i] = count
                    count += 1
            else:
                if device[i] in old_nodes:
                    device[i] = new_nodes[old_nodes.index(device[i])]
                else:
                    old_nodes.append(device[i])
                    new_nodes.append(count)
                    device[i] = count
                    count += 1
    
    for i in range(len(old_nodes)):
        node_map.append([old_nodes[i], new_nodes[i]])
    return count - 1, inputs, outputs, node_map
