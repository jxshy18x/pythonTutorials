graph1 = {
    "A": ["B", "D", "C"],
    "B": ["A", "G"],
    "C": ["A", "F"],
    "D": ["A", "E", "F"],
    "E": ["D", "F", "H"],
    "F": ["C", "D", "E"],
    "G": ["B", "H"],
    "H": ["G", "E"]
}

graph2 = {
    "E": {"F": 3, "G": 5, "H": 9},
    "F": {"E": 3, "K": 2, "L": 8},
    "G": {"E": 5, "H": 6,"K": 2, "L": 1},
    "H": {"E": 9, "G": 6, "L": 10},
    "K": {"F": 2, "G": 2},
    "L": {"F": 8, "G": 1, "H": 10}
}

def breadthFirst(startNode, goalNode, graph1):
    frontier = []
    explored = []
    frontier.append(startNode)

    while (len(frontier)!= 0):
        currentNode = frontier.pop(0)

        if (currentNode == goalNode):
            print("Goal has been found")
            explored.append(goalNode)
            print(explored)
            return True
        children = graph1[currentNode]
        print(currentNode)
        explored.append(currentNode)

        for x in children:
            if x not in explored and x not in frontier:
                frontier.append(x)

breadthFirst("A", "G", graph1)
