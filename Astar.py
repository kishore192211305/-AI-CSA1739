from heapq import heappop, heappush

def a_star_search(graph, heuristics, start, goal):
    open_set = []
    heappush(open_set, (heuristics[start], 0, start, []))  # (f_score, g_score, current_node, path)
    closed_set = set()

    while open_set:
        f_score, g_score, current_node, path = heappop(open_set)
        
        if current_node in closed_set:
            continue
        
        path = path + [current_node]
        
        if current_node == goal:
            return path, g_score
        
        closed_set.add(current_node)
        
        for neighbor, cost in graph[current_node].items():
            if neighbor not in closed_set:
                heappush(open_set, (g_score + cost + heuristics[neighbor], g_score + cost, neighbor, path))
    
    return None, float('inf')

def main():
    # Input for the graph
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))

    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighbors and costs for {node} (format: neighbor1 cost1 neighbor2 cost2 ...): ").split()
        graph[node] = {neighbors[i]: int(neighbors[i + 1]) for i in range(0, len(neighbors), 2)}

    # Input for heuristics
    heuristics = {}
    for _ in range(num_nodes):
        node, heuristic = input("Enter the node and its heuristic value: ").split()
        heuristics[node] = int(heuristic)

    # Input for start and goal nodes
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    
    # Perform A* search
    path, cost = a_star_search(graph, heuristics, start_node, goal_node)
    
    if path:
        print("Path:", path)
        print("Cost:", cost)
    else:
        print("No path found")


main()
