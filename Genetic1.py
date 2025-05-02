import numpy as np
import random
import matplotlib.pyplot as plt

# Objective function
def fitness(x):
    return x * np.sin(10 * np.pi * x) + 1.0
# Generate random population
def generate_population(size):
    return np.random.uniform(0, 1, size)

# Crossover
def crossover(p1, p2):
    alpha = np.random.rand()
    return alpha * p1 + (1 - alpha) * p2

# Mutation
def mutate(x, mutation_rate=0.1):
    if np.random.rand() < mutation_rate:
        x += np.random.normal(0, 0.05)
    return np.clip(x, 0, 1)

# Genetic Algorithm
def genetic_algorithm(pop_size=20, generations=50):
    population = generate_population(pop_size)
    best_scores = []

    for gen in range(generations):
        # Evaluate fitness
        fitness_vals = np.array([fitness(x) for x in population])
        best_scores.append(fitness_vals.max())

        # Selection: Roulette Wheel
        probs = fitness_vals / fitness_vals.sum()
        selected = np.random.choice(population, size=pop_size, p=probs)

        # Crossover and Mutation
        next_gen = []
        for _ in range(0, pop_size, 2):
            p1, p2 = random.sample(list(selected), 2)
            child1 = mutate(crossover(p1, p2))
            child2 = mutate(crossover(p2, p1))

            next_gen.extend([child1, child2])

        population = np.array(next_gen[:pop_size])

    # Plot performance
    plt.plot(best_scores)
    plt.title("Genetic Algorithm Optimization")
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.grid(True)
    plt.show()

    # Output best result
    best_x = population[np.argmax([fitness(x) for x in population])]
    print(f"Best solution: x = {best_x:.4f}, f(x) = {fitness(best_x):.4f}")

# Run the genetic algorithm
genetic_algorithm()
