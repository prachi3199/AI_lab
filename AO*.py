class Node:
    def __init__(self, name, children=None, cost=0, is_and_node=False):
        self.name = name
        self.children = children or []  # list of tuples: (child_node, cost)
        self.cost = cost                # cost of current node
        self.is_and_node = is_and_node # AND or OR node

class AOStar:
    def __init__(self, root):
        self.root = root
        self.solution = []

    def search(self, node):
        if not node.children:  # If it's a terminal node
            self.solution.append(node.name)
            return node.cost

        if node.is_and_node:
            total_cost = node.cost
            for child, cost in node.children:
                total_cost += self.search(child) + cost
            self.solution.append(node.name)
            return total_cost

        else:  # OR node
            min_cost = float('inf')
            best_child = None
            for child, cost in node.children:
                total = self.search(child) + cost
                if total < min_cost:
                    min_cost = total
                    best_child = child
            self.solution.append(node.name)
            return node.cost + min_cost

    def show_solution(self):
        print("Solution Path:", " -> ".join(reversed(self.solution)))


# 🧠 Example AO* Tree
# Goal: Solve problem starting from node A
# A -> (B OR C)
# B -> (D AND E)
# C -> (F)
# D, E, F are terminal nodes

# Terminal nodes
D = Node('D', cost=3)
E = Node('E', cost=2)
F = Node('F', cost=4)

# AND Node B
B = Node('B', children=[(D, 1), (E, 1)], is_and_node=True)

# OR Node C
C = Node('C', children=[(F, 2)], is_and_node=False)

# Root OR Node A
A = Node('A', children=[(B, 2), (C, 1)], is_and_node=False)

# Run AO*
ao = AOStar(A)
total_cost = ao.search(A)
ao.show_solution()
print("Total Cost:", total_cost)
