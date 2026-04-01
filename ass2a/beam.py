from heuristic import heuristic

def beam(graph, start, goals, coords, beam_width=2):
    pq = [start]
    visited = set()
    parent = {start: None}
    nodes_created = 1
    counter = 0 

    while pq:
        next_frontier = []

        for current in pq:
            if current in visited:
                continue
            visited.add(current)
            if current in goals:
                return current, parent, nodes_created

            for neighbor, cost in graph.get(current, []):
                if neighbor not in visited:
                    parent[neighbor] = current
                    next_frontier.append((neighbor, counter))
                    counter += 1
                    nodes_created += 1

        
        next_frontier.sort(
            key=lambda item: (
                heuristic(item[0], goals, coords),
                item[1]
            )
        )

        pq = [node for node, _ in next_frontier[:beam_width]]

    return None, parent, nodes_created