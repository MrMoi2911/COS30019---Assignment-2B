def dfs_stack(graph, start, goals):
    stack = [start]
    visited = set()
    parent = {start: None}
    nodes_created = 1

    while stack:
        current = stack.pop()

        if current in visited:
            continue
        visited.add(current)

        if current in goals:
            return current, parent, nodes_created

        for neighbor, cost in sorted(reversed(graph.get(current, []))):
            if neighbor not in visited:
                parent[neighbor] = current
                stack.append(neighbor)
                nodes_created += 1

    return None, parent, nodes_created