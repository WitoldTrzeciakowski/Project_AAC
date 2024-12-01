import numpy as np
import random

def generate_random_graph(directed = False):
    """
    Generuje losowy graf skierowany lub nieskierowany w formie macierzy sąsiedztwa.

    Parametry:
        num_vertices: int - liczba wierzchołków w grafie.
        density: float - gęstość grafu (wartość z przedziału [0, 1]), im większa, tym więcej krawędzi.
        directed: bool - True, jeśli graf ma być skierowany, False, jeśli nieskierowany.

    Zwraca:
        adj_matrix: numpy.ndarray - macierz sąsiedztwa wygenerowanego grafu.
    """
    num_vertices = random.randint(1,30)
    density =random.random()  
    # Upewnij się, że gęstość jest w poprawnym zakresie
    if not (0 <= density <= 1):
        raise ValueError("Density must be between 0 and 1.")

    # Inicjalizacja pustej macierzy sąsiedztwa
    adj_matrix = np.zeros((num_vertices, num_vertices), dtype=int)

    # Przechodzimy po parach wierzchołków i dodajemy krawędzie z prawdopodobieństwem zależnym od gęstości
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and random.random() < density:
                adj_matrix[i, j] = 1
                if not directed:
                    adj_matrix[j, i] = 1  # Nieskierowana krawędź

    return adj_matrix


if __name__ == "__main__":

    print("Losowy graf nieskierowany:")
    undirected_graph = generate_random_graph()
    print(undirected_graph)

    print("\nLosowy graf skierowany:")
    directed_graph = generate_random_graph()
    print(directed_graph)