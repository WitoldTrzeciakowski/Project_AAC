import random
import math

def approximate_hamiltonian_cycles(adj_matrix, iterations=10000):
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


adj_matrix = [
    [0, 1, 1, 0, 0],  
    [1, 0, 1, 1, 0],  
    [1, 1, 0, 0, 1],  
    [0, 1, 0, 0, 1],  
    [0, 0, 1, 1, 0],  
]

estimated_cycles = approximate_hamiltonian_cycles(adj_matrix, iterations=100000)
print(f"Przybliżona liczba cykli Hamiltona: {round(estimated_cycles)}")
