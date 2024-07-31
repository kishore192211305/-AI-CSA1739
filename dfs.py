def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def main():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))

    for i in range(num_nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighbors of {node} (space-separated): ").split()
        graph[node] = neighbors

    start_node = input("Enter the start node: ")
    print("DFS Traversal: ")
    dfs(graph, start_node)

main()
