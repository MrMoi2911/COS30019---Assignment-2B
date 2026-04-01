import ass2a.graphs
import sys

from ass2a.bfs import bfs as BFS
from ass2a.dfs_stack import dfs_stack as DFS
from ass2a.gbfs import gbfs as GBFS
from ass2a.astar import astar as AS
from ass2a.pathconstruct import reconstruct_path
from ass2a.iddfs import iddfs as CUS1
from ass2a.beam import beam as CUS2


def main():
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        sys.exit(1)

    filename = sys.argv[1]
    method = sys.argv[2]

    coords, graph, start, goals = graphs.parse_graph_file(filename)

    if method == "BFS":
        goal, parent, nodes = BFS(graph, start, goals)

    elif method == "DFS":
        goal, parent, nodes = DFS(graph, start, goals)

    elif method == "GBFS":
        goal, parent, nodes = GBFS(graph, start, goals, coords)

    elif method == "AS":
        goal, parent, nodes = AS(graph, start, goals, coords)
    elif method == "CUS1":
        goal, parent, nodes = CUS1(graph, start, goals)
    elif method =="CUS2":
        goal, parent, nodes = CUS2(graph, start, goals, coords)
    else:
        print("Unknown method")
        sys.exit(1)

    if goal is None:
        print("No path found")
        return

    path = reconstruct_path(start, goal, parent)


    print(filename, method)
    print(goal, nodes)
    print(" ".join(map(str, path)))


if __name__ == "__main__":
    main()