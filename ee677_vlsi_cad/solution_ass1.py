class Node:
    def __init__(self, op="", left=None, right=None, value=None):
        # op: str, left: Node, right: Node, value: bool
        self.op = op
        self.left = left
        self.right = right
        self.evaluated = False
        if left is None:
             self.evaluated = True
             self.value = value
             self.depth = 0
        else:
            self.depth = max(left.depth, right.depth) + 1

    def evaluate(self):
        # assumes left and right are evaluated
        if self.op == "AND":
            self.value = self.left.value and self.right.value
        elif self.op == "OR":
            self.value = self.left.value or self.right.value
        elif self.op == "XOR":
            self.value = self.left.value != self.right.value
        self.evaluated = True

def solve(nodes):
    while True:
        all_evaluated = True
        for key in nodes:
            node = nodes[key]
            if not node.evaluated:
                all_evaluated = False
                if node.left.evaluated and node.right.evaluated:
                    node.evaluate()
        if all_evaluated:
            break

def read(filename):
    """Netlist format:
    input1 input2 ...
    value_input1 value_input2 ...
    output1 output2 ...
    out_variable gatename in_variable1 in_variable2
    out_variable gatename in_variable1 in_variable2
    .
    .
    .
    """
    with open(filename) as f:
        f_str = f.read().strip()
    lines = f_str.split("\n")
    nodes = {}
    inputs = lines[0].split()
    values = lines[1].split()
    for input_, value in zip(inputs, values):
        nodes[input_] = Node(value=True if value=="1" else False)
    for line in lines[3:]:
        o, op, i1, i2 = line.split()
        nodes[o] = Node(op, nodes[i1], nodes[i2])
    return nodes, lines[2].split()

if __name__ == '__main__':
    filename = input("Enter filename where netlist is: ")
    nodes, outputs = read(filename)
    solve(nodes)
    for output in outputs:
        print(output, ":", int(nodes[output].value))