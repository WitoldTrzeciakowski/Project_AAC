
import read_file  # Assuming you have a module to handle graph reading and analysis

# Function to check if a graph has a Hamiltonian cycle
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

# Function to add an edge and check if it results in a Hamiltonian cycle
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

# Backtracking function to try adding edges and check for Hamiltonian cycle
def backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added, isDirected):
    if current_edges_added > max_edges_to_add:
        return False, graph  # Return False and the unmodified graph
    
    if is_hamiltonian_cycle(graph):
        return True, graph  # Return True and the current graph (which is Hamiltonian)

    n = len(graph)
    for u in range(n):
        for v in range(u + 1, n):
            if isDirected:
                if graph[u][v] == 0 and graph[v][u] == 0:
                    graph[u][v] = 1
                    found, updated_graph = backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added + 1, isDirected)
                    if found:
                        return True, updated_graph
                    graph[v][u] = 1
                    found, updated_graph = backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added + 1, isDirected)
                    if found:
                        return True, updated_graph
                    graph[u][v] = 0
                    found, updated_graph = backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added + 1, isDirected)
                    if found:
                        return True, updated_graph
                    graph[v][u] = 0
                elif graph[u][v] == 0 and graph[v][u] == 1:
                    graph[u][v] = 1
                    found, updated_graph = backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added + 1, isDirected)
                    if found:
                        return True, updated_graph
                    graph[u][v] = 0
                elif graph[v][u] == 0 and graph[u][v] == 1:
                    graph[v][u] = 1
                    found, updated_graph = backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added + 1, isDirected)
                    if found:
                        return True, updated_graph
                    graph[v][u] = 0
            else:
                if graph[u][v] == 0:
                    # Add edge and recursively check
                    graph[u][v] = 1
                    graph[v][u] = 1
                    found, updated_graph = backtrack_to_add_edges(graph, max_edges_to_add, current_edges_added + 1, isDirected)
                    if found:
                        return True, updated_graph
                    # Backtrack: remove the edge
                    graph[u][v] = 0
                    graph[v][u] = 0
    
    return False, graph  # If no Hamiltonian cycle found, return unmodified graph


def find_minimum_edges_to_hamiltonian(graph):
    max_edges_to_add = 1  
    graph_data = read_file.make_graph(graph) 
    informations_about_graph = read_file.investigate_adjacency_matrix_properties(graph_data) 
    directed_inside = informations_about_graph["directed"]
    
    while True:
        found, updated_graph = backtrack_to_add_edges(graph, max_edges_to_add, 0, directed_inside)
        if found:
            return max_edges_to_add, updated_graph  
        max_edges_to_add += 1  
