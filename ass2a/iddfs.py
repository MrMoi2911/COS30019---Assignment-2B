def iddfs(graph, start, goals, max_depth=1000):
    total_nodes = 0

    def dls(current, depth, visited, parent):
        nonlocal total_nodes
        total_nodes += 1

        if current in goals:
            return current

        if depth == 0:
            return None

        for neighbor, cost in sorted(graph.get(current, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current

                result = dls(neighbor, depth - 1, visited, parent)
                if result:
                    return result

        return None

    for depth in range(max_depth + 1):
        visited = {start}
        parent = {start: None}

        found = dls(start, depth, visited, parent)

        if found:
            return found, parent, total_nodes

    return None, parent, total_nodes