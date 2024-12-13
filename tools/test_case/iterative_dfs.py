def dfs_iterative(graph, start):
    stack = [start]
    visited = set()
    path = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            # Add neighbors to the stack in reverse order to mimic recursive behavior
            stack.extend(reversed(graph[node]))

    return path


# Example usage
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

path = dfs_iterative(graph, "A")
print("DFS Path:", path)
