from egienvalue import calculate_largest_eigenvalue
from graph_checks import is_k2_join_kn4_plus_2k1, generate_k2_join_kn4_plus_2k1
from matrix_det import determinant_of_matrix
from maximized_det import greedy_edge_addition
import numpy as np

def add_edges_to_ensure_min_degree(adj_matrix, min_degree=2):
    n = len(adj_matrix)
    degrees = [sum(row) for row in adj_matrix] 
    for i in range(n):
        while degrees[i] < min_degree:
            potential_vertices = [j for j in range(n) if adj_matrix[i][j] == 0 and i != j]
            if potential_vertices:
                j = potential_vertices[0]
                adj_matrix[i][j] = adj_matrix[j][i] = 1
                degrees[i] += 1
                degrees[j] += 1  
            else:
                break  


    return adj_matrix
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

adj_matrix = [
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]


def spectral_extension(graph):
    if len (graph) < 14:
        print("Not possible")
        return
    graph = add_edges_to_ensure_min_degree(graph)
    for row in graph:
        print (row)
    size = len(graph[1])
    exception_graph = generate_k2_join_kn4_plus_2k1(size)
    iterations=0
    while calculate_largest_eigenvalue(graph) < calculate_largest_eigenvalue(exception_graph):
        iterations+=1
        graph = greedy_edge_addition(graph,1)
    for row in graph:
        print (row)
    print(iterations)
    print(is_hamiltonian_cycle(graph))

spectral_extension(adj_matrix)





