
import random
import matplotlib.pyplot as plt

# GA parameters
population_size = 10
chromosome_length = 10
generations = 50
mutation_rate = 0.01

# Create initial population (random binary strings)
def create_population():
    return [[random.randint(0, 1) for _ in range(chromosome_length)]
            for _ in range(population_size)]

# Fitness = number of 1s in chromosome
def fitness(chromosome):
    return sum(chromosome)

# Tournament selection
def select_parents(population):
    selected = []
    for _ in range(population_size):
        a = random.choice(population)
        b = random.choice(population)
        winner = a if fitness(a) > fitness(b) else b
        selected.append(winner)
    return selected

# Single-point crossover
def crossover(p1, p2):
    point = random.randint(1, chromosome_length - 1)
    return p1[:point] + p2[point:]

# Mutation: flip bits
def mutate(chromosome):
    return [bit if random.random() > mutation_rate else 1 - bit for bit in chromosome]

# GA main loop
population = create_population()
best_per_gen = []

for gen in range(generations):
    parents = select_parents(population)
    next_generation = []

    for i in range(0, population_size, 2):
        p1, p2 = parents[i], parents[i+1]
        child1 = mutate(crossover(p1, p2))
        child2 = mutate(crossover(p2, p1))
        next_generation.extend([child1, child2])

    population = next_generation[:population_size]
    best = max(population, key=fitness)
    best_per_gen.append(fitness(best))

# Final result
best_solution = max(population, key=fitness)
print(f"Best solution: {''.join(map(str, best_solution))}")
print(f"Max number of 1s: {fitness(best_solution)}")

# Plotting
plt.plot(best_per_gen)
plt.title("Best Fitness Over Generations")
plt.xlabel("Generation")
plt.ylabel("Number of 1s (Fitness)")
plt.grid(True)
plt.show()
