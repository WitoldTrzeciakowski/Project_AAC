from Spectral_stuff.egienvalue import calculate_largest_eigenvalue
from Spectral_stuff.graph_checks import is_k2_join_kn4_plus_2k1, generate_k2_join_kn4_plus_2k1,identify_graph
from Spectral_stuff.maximized_det import greedy_edge_addition


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

def is_hamiltonian_cycle(adjacency_matrix):
    vertices_count = len(adjacency_matrix)
    
    def is_safe_to_add(v, pos, path):
        # Check if there is an edge from the last vertex in the path to v
        if adjacency_matrix[path[pos - 1]][v] == 0:
            return False
        # Check if v is already included in the path
        if v in path:
            return False
        return True

    def hamiltonian_cycle_util(path, pos):
        if pos == vertices_count:
            # Check if there is an edge from the last vertex to the first vertex
            return adjacency_matrix[path[pos - 1]][path[0]] == 1

        for v in range(vertices_count):
            if is_safe_to_add(v, pos, path):
                path[pos] = v
                if hamiltonian_cycle_util(path, pos + 1):
                    return True
                path[pos] = -1  # Backtrack

        return False

    path = [-1] * vertices_count
    path[0] = 0  # Start the path at vertex 0

    if hamiltonian_cycle_util(path, 1):
        return True
    return False

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
            return
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
            if iterations > size*size:
                print("failure of spectral extension method")
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
    size = len(graph[1])
    exception_graph = generate_k2_join_kn4_plus_2k1(size)
    iterations=0
    eginvalue_exceptiong_graph = calculate_largest_eigenvalue(exception_graph)
    while (calculate_largest_eigenvalue(graph) < eginvalue_exceptiong_graph  \
            or is_k2_join_kn4_plus_2k1(graph)):
        iterations+=1
        if iterations > size*size:
            return None
        graph = greedy_edge_addition(graph,1)
    return graph

def check_spectral_theorems(graph):
    size = len(graph)
    if calculate_largest_eigenvalue(graph) <= size - 3:
        exception = identify_graph(graph)
        if exception not in {"K1 ∨ (Kn−3 + 2K1)", "K2 ∨ 4K1", "K1 ∨ (K1,3 + K1)"}:
            return True
    exception_graph = generate_k2_join_kn4_plus_2k1(size)
    if (calculate_largest_eigenvalue(graph) >= calculate_largest_eigenvalue(exception_graph) \
    and not is_k2_join_kn4_plus_2k1(graph)):
        return True
    return False




