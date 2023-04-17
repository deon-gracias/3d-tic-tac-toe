import random
import numpy as np

# Define the distance matrix
dist_matrix = np.array([[0, 10, 15, 20],
                        [10, 0, 35, 25],
                        [15, 35, 0, 30],
                        [20, 25, 30, 0]])

# Define the parameters
num_cities = len(dist_matrix)
pop_size = 100
num_generations = 1000
mutation_prob = 0.05

# Define the fitness function
def fitness(chromosome):
    distance = 0
    for i in range(num_cities-1):
        distance += dist_matrix[chromosome[i], chromosome[i+1]]
    distance += dist_matrix[chromosome[num_cities-1], chromosome[0]]
    return 1/distance

# Define the initialization function
def initialize_population():
    population = []
    for i in range(pop_size):
        chromosome = list(range(num_cities))
        random.shuffle(chromosome)
        population.append(chromosome)
    return population

# Define the selection function
def selection(population):
    fitnesses = [fitness(chromosome) for chromosome in population]
    fittest = np.argsort(fitnesses)[-int(pop_size/2):]
    return [population[i] for i in fittest]

# Define the crossover function
def crossover(parent1, parent2):
    child = [-1]*num_cities
    start, end = sorted([random.randint(0, num_cities-1) for _ in range(2)])
    for i in range(start, end+1):
        child[i] = parent1[i]
    j = 0
    for i in range(num_cities):
        if child[i] == -1:
            while parent2[j] in child:
                j += 1
            child[i] = parent2[j]
            j += 1
    return child

# Define the mutation function
def mutation(chromosome):
    if random.random() < mutation_prob:
        i, j = sorted([random.randint(0, num_cities-1) for _ in range(2)])
        chromosome[i:j+1] = reversed(chromosome[i:j+1])
    return chromosome

# Define the main function
def solve_tsp():
    population = initialize_population()
    for i in range(num_generations):
        population = selection(population)
        offspring = [crossover(population[random.randint(0, len(population)-1)], 
                               population[random.randint(0, len(population)-1)]) for _ in range(pop_size)]
        offspring = [mutation(chromosome) for chromosome in offspring]
        population = population + offspring
    fitnesses = [fitness(chromosome) for chromosome in population]
    best_index = np.argmax(fitnesses)
    best_chromosome = population[best_index]
    return best_chromosome, 1/fitnesses[best_index]

# Call the main function
best_chromosome, best_distance = solve_tsp()
print('Best chromosome:', best_chromosome)
print('Best distance:', best_distance)
