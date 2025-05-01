from queue import PriorityQueue

# Graph with costs
graph = {
    'A': [('B', 1), ('C', 2), ('D', 1)],
    'B': [('E', 3)],
    'C': [],
    'D': [('G', 4)],
    'E': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 4,
    'G': 0
}

def a_star(start, goal):
    pq = PriorityQueue()
    pq.put((0 + heuristic[start], 0, start, [start]))  # (f(n), g(n), current, path)

    visited = set()

    while not pq.empty():
        f, g, current, path = pq.get()

        if current in visited:
            continue
        visited.add(current)

        print("Visiting:", current, "| Path:", path, "| Cost:", g)

        if current == goal:
            print("🎯 Goal reached:", current)
            print("✅ Final path:", path)
            print("🧮 Total cost:", g)
            return

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                pq.put((new_f, new_g, neighbor, path + [neighbor]))

# Run A* search
a_star('A', 'G')
