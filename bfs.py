import heapq

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.neighbors = []

    def add_neighbor(self, neighbor_node, cost):
        self.neighbors.append((neighbor_node, cost))

    def __lt__(self, other):
        return self.heuristic < other.heuristic


def best_first_search(start, goal):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (start.heuristic, start))

    while priority_queue:
        _,current_node = heapq.heappop(priority_queue)

        if current_node.name in visited:
            continue

        print(f"Visiting: {current_node.name}")
        visited.add(current_node.name)

        if current_node.name == goal.name:
            print("Goal reached!")
            return

        for neighbor, cost in current_node.neighbors:
            if neighbor.name not in visited:
                heapq.heappush(priority_queue, (neighbor.heuristic, neighbor))

    print("Goal not reachable.")


# Example graph construction
if __name__ == "__main__":
    # Nodes with heuristic values
    A = Node("A", 6)
    B = Node("B", 4)
    C = Node("C", 5)
    D = Node("D", 2)
    E = Node("E", 1)
    F = Node("F", 0)  # Goal node

    # Add edges (neighbor, cost)
    A.add_neighbor(B, 1)
    A.add_neighbor(C, 1)
    B.add_neighbor(D, 1)
    C.add_neighbor(D, 1)
    D.add_neighbor(E, 1)
    E.add_neighbor(F, 1)

    # Run Best First Search
    best_first_search(A, F)
