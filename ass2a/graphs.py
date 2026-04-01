def parse_graph_file(filename):
    coords = {}
    graph = {}
    start = None
    goals = []

    section = None

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line == "Nodes:":
                section = "nodes"
                continue
            elif line == "Edges:":
                section = "edges"
                continue
            elif line == "Origin:":
                section = "origin"
                continue
            elif line == "Destinations:":
                section = "destinations"
                continue


            if section == "nodes":
                node, coord = line.split(":")
                node = int(node.strip())

                x, y = coord.strip()[1:-1].split(",")
                coords[node] = (int(x), int(y))

      
            elif section == "edges":
                pair, cost = line.split(":")
                a, b = pair.strip()[1:-1].split(",")

                a = int(a)
                b = int(b)
                cost = int(cost.strip())

                if a not in graph:
                    graph[a] = []

                graph[a].append((b, cost))

    
            elif section == "origin":
                start = int(line)

   
            elif section == "destinations":
                goals = [int(x.strip()) for x in line.split(";")]

    return coords, graph, start, goals