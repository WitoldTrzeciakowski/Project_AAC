import random
import math

def approximate_hamiltonian_cycles(adj_matrix, iterations=10000):
    iterations = len(adj_matrix) * len(adj_matrix)
    n = len(adj_matrix) 
    hamiltonian_count = 0

    def is_hamiltonian_cycle(path):
        for i in range(n):
            if adj_matrix[path[i]][path[(i + 1) % n]] == 0:
                return False
        return True

    for _ in range(iterations):
        path = random.sample(range(n), n)
        path.append(path[0])
        if is_hamiltonian_cycle(path):
            hamiltonian_count += 1

    total_possible_permutations = math.factorial(n)
    estimated_cycles = (hamiltonian_count / iterations) * total_possible_permutations

    return estimated_cycles



