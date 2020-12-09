from random import randrange

import numpy as np

from lesson11.domain import Chromosome


# генерация первой популяции
def first_population(params, result, population_size):
    population = []
    for i in range(population_size):
        gene_list = []
        for j in range(len(params)):
            gene = randrange(result)
            gene_list.append(gene)
        population.append(Chromosome(0.0, gene_list))
    return population

# подсчет "выживаемости" хромосомы
def calculate_chromosome_accuracy(population, fit_sum):
    for chromosome in population:
        chromosome.accuracy = chromosome.fitness / fit_sum


# проверка найденных значений
# и присвоение им шанса на попадание в следующую популяцию (естественный отбор)
def fit_function(params, result, population):
    fit_sum = 0
    for i in range(len(population)):
        chromosome_result = 0
        chromosome = population[i]

        for j in range(0, len(params)):
            chromosome_result += chromosome.gene_list[j] * params[j]

        if chromosome_result == result:
            print("Solution is:", chromosome.gene_list)
            return True

        chromosome.fitness = chromosome_result
        fit_sum += chromosome_result

    calculate_chromosome_accuracy(population, fit_sum)
    return False


# выбор двух хромосом-родителей
def selection(current_population):
    candidates = []
    for chromosome in current_population:
        candidates.append(chromosome.accuracy)

    parent_first = np.random.choice(current_population, 1, p=candidates)[0]
    parent_second = np.random.choice(current_population, 1, p=candidates)[0]

    return parent_first, parent_second


def mutation(params, gene_list, mutation_chance):
    mutation_p = randrange(0, 101)
    if mutation_p < mutation_chance:
        rand2 = randrange(0, len(params))
        gene_list[rand2] = randrange(0, 31)
    return Chromosome(0.0, gene_list)

# генерация новой популяции
def reproduction(params, population, dominant_parent, another_parent, mutation_chance):
    new_population = []
    for i in range(len(population)):
        random_gene = randrange(0, len(params))
        gene_list = dominant_parent.gene_list
        gene_list[random_gene] = another_parent.gene_list[random_gene]
        new_chromosome = mutation(params, gene_list, mutation_chance)
        new_population.append(new_chromosome)
    return new_population


def start(params, result, population_size):
    population = first_population(params, result, population_size)
    solution_not_found = not fit_function(params, result, population)

    while solution_not_found:
        parent_first, parent_second = selection(population)

        if parent_first.accuracy > parent_second.accuracy:
            dominant_parent = parent_first
            another_parent = parent_second
        else:
            dominant_parent = parent_second
            another_parent = parent_first

        population = reproduction(params, population, dominant_parent, another_parent, mutation_chance)
        solution_not_found = not fit_function(params, result, population)


eq_result = 32
# количество хромосом
default_population_size = 7
# вероятность мутации в процентах
mutation_chance = 90
eq_params = [2, 2, 3, 4]

start(eq_params, eq_result, default_population_size)

# example of answer
# Solution is: [3, 5, 4, 1]
