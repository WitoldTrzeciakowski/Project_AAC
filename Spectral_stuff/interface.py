from egienvalue import calculate_largest_eigenvalue
from graph_checks import is_k2_join_kn4_plus_2k1, generate_k2_join_kn4_plus_2k1
from matrix_det import determinant_of_matrix
from maximized_det import greedy_edge_addition
import numpy as np

def is_hamiltonian_cycle(graph):
    n = len(graph)
    visited = [False] * n
    path = []

    # Start backtracking from vertex 0
    def backtrack(v, path_length):
        visited[v] = True
        path.append(v)

        if path_length == n:
            # Check if there is an edge back to the starting vertex
            if graph[v][path[0]] == 1:
                return True
            visited[v] = False
            path.pop()
            return False

        for u in range(n):
            if graph[v][u] == 1 and not visited[u]:
                if backtrack(u, path_length + 1):
                    return True

        # Backtrack
        visited[v] = False
        path.pop()
        return False

    return backtrack(0, 1)

adj_matrix_14 = [
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
]

def spectral_extension(graph):
    if len (graph) < 14:
        print("Not possible")
        return
    size = len(graph[1])
    exception_graph = generate_k2_join_kn4_plus_2k1(size)
    iterations=0
    while calculate_largest_eigenvalue(graph) < calculate_largest_eigenvalue(exception_graph):
        iterations+=1
        graph = greedy_edge_addition(graph,1)
        for row in graph:
            print (row)
        print(is_hamiltonian_cycle(graph))
        print("NEXT GRAPH: ")
    print(iterations)

spectral_extension(adj_matrix_14)





