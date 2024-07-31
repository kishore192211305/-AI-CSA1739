from collections import deque

def bfs(graph, start):
    # Create a queue for BFS and enqueue the start node
    queue = deque([start])
    # Mark the start node as visited
    visited = set([start])
    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        print(node, end=' ')
        
        # Get all adjacent vertices of the dequeued node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # If a neighbor has not been visited, mark it as visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage:
if __name__ == "__main__":
    # Graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    print("BFS starting from node A:")
    bfs(graph, 'A')
