def degree(adj_matrix, v, directed=False):
    if directed:
        out_deg = sum(adj_matrix[v]) 
        in_deg = sum(row[v] for row in adj_matrix)  
        return out_deg, in_deg
    return sum(adj_matrix[v])

def add_edge(adj_matrix, u, v, directed=False):
    adj_matrix[u][v] = 1
    if not directed:
        adj_matrix[v][u] = 1

def is_hamiltonian_by_dirac(adj_matrix, directed=False):
    n = len(adj_matrix)
    if n < 3:
        return False

    for v in range(n):
        if degree(adj_matrix, v, directed=directed) < n / 2:
            return False
    return True

def add_minimal_edges_by_dirac(adj_matrix, directed=False):
    """
    Add the minimal number of edges to satisfy Dirac's theorem.
    """
    n = len(adj_matrix)
    if n < 3:
        return adj_matrix  # Dirac's theorem doesn't apply

    for u in range(n):
        for v in range(u + 1, n):
            if adj_matrix[u][v] == 0:  # If u and v are not connected
                if degree(adj_matrix, u, directed=directed) < n / 2 or degree(adj_matrix, v, directed=directed) < n / 2:
                    add_edge(adj_matrix, u, v, directed=directed)
                    if is_hamiltonian_by_dirac(adj_matrix, directed=directed):
                        return adj_matrix

    return adj_matrix  # Return the updated graph

if __name__ == "__main__":
    # Example Undirected Graph
    adj_matrix_undirected = [
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

    print("Initial Undirected Graph satisfies Dirac:", is_hamiltonian_by_dirac(adj_matrix_undirected, directed=False))
    updated_matrix_undirected = add_minimal_edges_by_dirac(adj_matrix_undirected, directed=False)
    print("Updated Undirected Graph satisfies Dirac:", is_hamiltonian_by_dirac(updated_matrix_undirected, directed=False))
    print("Updated Undirected Adjacency Matrix:")
    for row in updated_matrix_undirected:
        print(row)
