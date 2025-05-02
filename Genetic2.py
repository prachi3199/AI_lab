import random

target = "HELLO"
population_size = 100
mutation_rate = 0.01
generations = 1000
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def random_individual():
    return ''.join(random.choice(chars) for _ in range(len(target)))

def fitness(individual):
    return sum(1 for i, j in zip(individual, target) if i == j)

def mutate(individual):
    return ''.join(
        ch if random.random() > mutation_rate else random.choice(chars)
        for ch in individual
    )

def crossover(p1, p2):
    idx = random.randint(0, len(p1) - 1)
    return p1[:idx] + p2[idx:]

def genetic_algorithm_string():
    population = [random_individual() for _ in range(population_size)]
    for gen in range(generations):
        # Sort population by fitness
        population = sorted(population, key=fitness, reverse=True)
        #print("Population: ",population)

        print("Generation: ",gen)
        print("Individual: ",population[0])
        # Check if target string is found
        if fitness(population[0]) == len(target):
            print(f"Found target '{population[0]}' at generation {gen}")
            break

        # Elitism: Carry forward the top 10 individuals
        next_gen = population[:10]

        # Create new individuals by crossover and mutation
        while len(next_gen) < population_size:
            p1, p2 = random.sample(population[:50], 2)
            child = mutate(crossover(p1, p2))
            next_gen.append(child)

        # Update the population
        population = next_gen

    # Output best result
    print(f"Best Match: {population[0]} | Fitness: {fitness(population[0])}")

# Run the genetic algorithm
genetic_algorithm_string()
