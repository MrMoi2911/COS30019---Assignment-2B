import heapq
from heuristic import heuristic

def gbfs(graph, start, goals, coords):
    pq = []
    visited = set()
    parent = {start: None}
    nodes_created = 1
    counter = 0  

    heapq.heappush(
        pq,
        (heuristic(start, goals, coords), counter, start)
    )
    counter += 1

    while pq:
        _, _, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)

        if current in goals:
            return current, parent, nodes_created

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                parent[neighbor] = current

                heapq.heappush(
                    pq,
                    (heuristic(neighbor, goals, coords), counter, neighbor)
                )
                counter += 1
                nodes_created += 1

    return None, parent, nodes_created