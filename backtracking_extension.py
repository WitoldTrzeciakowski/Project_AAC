import numpy as np
import read_file

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

def add_edge_and_check(graph, u, v):
    original_uv = graph[u][v]
    original_vu = graph[v][u]

    # Add edge (u, v) temporarily
    graph[u][v] = 1
    graph[v][u] = 1
    has_cycle = is_hamiltonian_cycle(graph)
    
    # Remove the edge to backtrack
    graph[u][v] = original_uv
    graph[v][u] = original_vu
    return has_cycle

def backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added, isDirected):
    if current_edges_added > max_edges_to_add:
        return False
    
    if is_hamiltonian_cycle(graph):
        return True

    n = len(graph)
    for u in range(n):
        for v in range(u + 1, n):
            if isDirected:
                if graph[u][v] == 0 and graph[v][u] == 0:
                    graph[u][v] = 1
                    if backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added + 1, isDirected):
                        return True
                    graph[v][u] = 1
                    if backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added + 1, isDirected):
                        return True
                    graph[u][v] = 0
                    if backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added + 1, isDirected):
                        return True
                    graph[v][u] = 0
                elif graph[u][v] == 0 and graph[v][u] == 1:
                    graph[u][v] = 1
                    if backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added + 1, isDirected):
                        return True
                    graph[u][v] = 0
                elif graph[v][u] == 0 and graph[u][v] == 1:
                    graph[v][u] = 1
                    if backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added + 1, isDirected):
                        return True
                    graph[v][u] = 0
            else:
                if graph[u][v] == 0:
                    # Add edge and recursively check
                    graph[u][v] = 1
                    graph[v][u] = 1
                    if backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added + 1, isDirected):
                        return True
                    # Backtrack: remove the edge
                    graph[u][v] = 0
                    graph[v][u] = 0
    
    return False

def find_minimum_edges_to_hamiltonian(graph):
    max_edges_to_add = 1  # Start with trying to add just one edge
    graph_data = read_file.make_graph(graph)
    informations_about_graph = read_file.investigate_adjacency_matrix_properties(graph_data)
    directed = informations_about_graph["directed"]
    while True:
        if backtrack_to_add_edges(graph, max_edges_to_add, 0, directed):
            return max_edges_to_add  # Minimum edges found to make graph Hamiltonian
        max_edges_to_add += 1  # Increase edge addition limit if no solution found


graph = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
])
graph2 = np.array([
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])

graph3 = np.array([
    [0, 1, 1, 0],
    [1 ,0, 1, 0],
    [1 ,1, 0, 1],
    [0 ,0, 1, 0],
])

graph4 = np.array([
    [0, 1, 1, 0],
    [0 ,0, 1, 0],
    [0 ,0, 0, 0],
    [0 ,0, 1, 0],
])

print("Minimum edges to add to make the graph Hamiltonian:", find_minimum_edges_to_hamiltonian(graph))
print("Minimum edges to add to make the graph Hamiltonian:", find_minimum_edges_to_hamiltonian(graph2))
print("Minimum edges to add to make the graph Hamiltonian:", find_minimum_edges_to_hamiltonian(graph3))
print("Minimum edges to add to make the graph Hamiltonian:", find_minimum_edges_to_hamiltonian(graph4))
