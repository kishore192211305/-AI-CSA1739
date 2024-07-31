import math

class Node:
    def __init__(self, value=None, is_terminal=False):
        self.value = value
        self.is_terminal = is_terminal
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def is_terminal_node(self):
        return self.is_terminal

    def get_children(self):
        return self.children

    def get_value(self):
        return self.value

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal_node():
        return node.get_value()

    if maximizing_player:
        max_eval = -math.inf
        for child in node.get_children():
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for child in node.get_children():
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def build_tree():
    nodes = {}
    num_nodes = int(input("Enter the number of nodes: "))

    for _ in range(num_nodes):
        node_id = input("Enter node ID: ")
        is_terminal = input(f"Is node {node_id} a terminal node? (yes/no): ").strip().lower() == 'yes'
        value = None
        if is_terminal:
            value = int(input(f"Enter the value for terminal node {node_id}: "))
        nodes[node_id] = Node(value=value, is_terminal=is_terminal)

    for node_id in nodes:
        num_children = int(input(f"Enter the number of children for node {node_id}: "))
        for _ in range(num_children):
            child_id = input(f"Enter child node ID for {node_id}: ")
            if child_id in nodes:
                nodes[node_id].add_child(nodes[child_id])
            else:
                print(f"Child node {child_id} does not exist.")

    root_id = input("Enter the root node ID: ")
    depth = int(input("Enter the depth of the search: "))
    
    return nodes[root_id], depth

def main():
    root, depth = build_tree()
    optimal_value = alpha_beta(root, depth, -math.inf, math.inf, True)
    print("Optimal value:", optimal_value)

if __name__ == "__main__":
    main()
