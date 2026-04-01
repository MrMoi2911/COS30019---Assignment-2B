from collections import deque

def bfs(graph, start, goals):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    nodes_created = 1

    while queue:
        current = queue.popleft()

        if current in goals:
            return current, parent, nodes_created

        for neighbor, cost in sorted(graph.get(current, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
                nodes_created += 1

    return None, parent, nodes_created