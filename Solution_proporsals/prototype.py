import numpy as np

def is_hamiltonian(adj_matrix, directed=False):
    n = len(adj_matrix)
    visited = [False] * n
    path = []

    for start in range(n):
        if hamiltonian_path(start, 1, visited, path, adj_matrix, directed, n):
            return True
    return False

def hamiltonian_path(v, depth, visited, path, adj_matrix, directed, n):
    """Recursive backtracking function to find a Hamiltonian path."""
    visited[v] = True
    path.append(v)

    if depth == n and (adj_matrix[path[-1]][path[0]] > 0 if directed else adj_matrix[path[0]][path[-1]] > 0):
        return True

    for u in range(n):
        if adj_matrix[v][u] > 0 and not visited[u]:  
            if hamiltonian_path(u, depth + 1, visited, path, adj_matrix, directed, n):
                return True
            
    visited[v] = False
    path.pop()
    return False

def add_edge(adj_matrix, u, v, directed=False):
    adj_matrix[u][v] += 1
    if not directed:
        adj_matrix[v][u] += 1

def degree(adj_matrix, v, directed=False):
    if directed:
        out_deg = sum(adj_matrix[v]) 
        in_deg = sum(row[v] for row in adj_matrix)  
        return out_deg, in_deg
    return sum(adj_matrix[v])  

def add_minimal_edges_for_hamiltonicity(adj_matrix, directed=False):
    n = len(adj_matrix)

    
    if directed:
        if all(degree(adj_matrix, v, directed=True)[0] >= n // 2 and degree(adj_matrix, v, directed=True)[1] >= n // 2 for v in range(n)):
            return adj_matrix
    else:
        if all(degree(adj_matrix, v) >= n // 2 for v in range(n)):
            return adj_matrix
    added = True
    while added:
        added = False
        for u in range(n):
            for v in range(n):
                if u != v and adj_matrix[u][v] == 0:
                    if directed:
                        out_deg, _ = degree(adj_matrix, u, directed=True)
                        _, in_deg = degree(adj_matrix, v, directed=True)
                        if out_deg + in_deg >= n:
                            add_edge(adj_matrix, u, v, directed=True)
                            added = True
                            if is_hamiltonian(adj_matrix, directed=True):
                                return adj_matrix
                    else:
                        if degree(adj_matrix, u) + degree(adj_matrix, v) >= n:
                            add_edge(adj_matrix, u, v, directed=False)
                            added = True
                            if is_hamiltonian(adj_matrix, directed=False):
                                return adj_matrix

    return adj_matrix

if __name__ == "__main__":
    adj_matrix_undirected = np.array([
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0]
    ], dtype=int)

    adj_matrix_directed = np.array([
        [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0]
    ], dtype=int)

    print("Initial Undirected Graph is Hamiltonian:", is_hamiltonian(adj_matrix_undirected, directed=False))
    hamiltonian_matrix_undirected = add_minimal_edges_for_hamiltonicity(adj_matrix_undirected, directed=False)
    print("Extended Undirected Graph is Hamiltonian:", is_hamiltonian(hamiltonian_matrix_undirected, directed=False))
    print("Extended Undirected Adjacency Matrix:\n", hamiltonian_matrix_undirected)

    print("\nInitial Directed Graph is Hamiltonian:", is_hamiltonian(adj_matrix_directed, directed=True))
    hamiltonian_matrix_directed = add_minimal_edges_for_hamiltonicity(adj_matrix_directed, directed=True)
    print("Extended Directed Graph is Hamiltonian:", is_hamiltonian(hamiltonian_matrix_directed, directed=True))
    print("Extended Directed Adjacency Matrix:\n", hamiltonian_matrix_directed)
