import math

def heuristic(node, goals, coords):
    x1, y1 = coords[node]
    return min(
        math.sqrt((x1 - coords[g][0])**2 + (y1 - coords[g][1])**2)
        for g in goals
    )