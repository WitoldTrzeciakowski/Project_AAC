from egienvalue import calculate_largest_eigenvalue
from graph_checks import is_k2_join_kn4_plus_2k1, generate_k2_join_kn4_plus_2k1,identify_graph
from maximized_det import greedy_edge_addition


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
    size = len(graph)
    # Handle small graphs
    if size < 14:
        if size <= 4:
            print("Not possible")
            return

        print("Graph size in range 4 < n < 14. Applying spectral extension and theorem.")
        print("Initial Graph:")
        for row in graph:
            print(row)

        graph = add_edges_to_ensure_min_degree(graph)
        exception = identify_graph(graph)
        if exception in {"K1 ∨ (Kn−3 + 2K1)", "K2 ∨ 4K1", "K1 ∨ (K1,3 + K1)"}:
            print(f"Graph matches exceptional case: {exception}")
            print("Hamiltonian path not guaranteed by the theorem.")
            return
        iterations = 0
        while calculate_largest_eigenvalue(graph) <= size - 3:
            iterations += 1
            graph = greedy_edge_addition(graph, 1)
            print(calculate_largest_eigenvalue(graph))
            if iterations > size*size:
                break

        print("Graph After Spectral Extension:")

        print(f"Iterations: {iterations}")
        if calculate_largest_eigenvalue(graph) > size - 3:
            print("Spectral radius condition satisfied.")
            if is_hamiltonian_cycle(graph):
                print("Graph contains a Hamiltonian cycle.")
            else:
                print("Graph contains a Hamiltonian path but not a cycle.")
        else:
            print("Spectral radius condition not satisfied. Hamiltonian path not guaranteed.")
        return
    graph = add_edges_to_ensure_min_degree(graph)
    for row in graph:
        print (row)
    size = len(graph[1])
    exception_graph = generate_k2_join_kn4_plus_2k1(size)
    iterations=0
    while (calculate_largest_eigenvalue(graph) < calculate_largest_eigenvalue(exception_graph) \
            or is_k2_join_kn4_plus_2k1(graph))\
            and (calculate_largest_eigenvalue(graph) <= size - 3 or identify_graph(graph) in
            {"K1 ∨ (Kn−3 + 2K1)", "K2 ∨ 4K1", "K1 ∨ (K1,3 + K1)"}):
        iterations+=1
        graph = greedy_edge_addition(graph,1)
    for row in graph:
        print (row)
    print(iterations)
    print(is_hamiltonian_cycle(graph))

spectral_extension(adj_matrix)
small_graph = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
]
spectral_extension(small_graph)
adj_matrix_test_10 = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
]
spectral_extension(adj_matrix_test_10)



