import heapq
from heuristic import heuristic

def astar(graph, start, goals, coords):
    pq = []
    parent = {start: None}
    g_cost = {start: 0}
    nodes_created = 1
    counter = 0 

    heapq.heappush(pq, (heuristic(start, goals, coords), counter, start))
    counter += 1

    while pq:
        _, _, current = heapq.heappop(pq)

        if current in goals:
            return current, parent, nodes_created

        for neighbor, cost in graph.get(current, []):
            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current

                f = new_g + heuristic(neighbor, goals, coords)

                
                heapq.heappush(pq, (f, counter, neighbor))
                counter += 1
                nodes_created += 1

    return None, parent, nodes_created