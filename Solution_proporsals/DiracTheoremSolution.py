def degree(adj_matrix, v, directed=False):
    if directed:
        out_deg = sum(adj_matrix[v])  # Out-degree
        in_deg = sum(row[v] for row in adj_matrix)  # In-degree
        return out_deg, in_deg
    return sum(adj_matrix[v])  # Degree for undirected graph


def add_edge(adj_matrix, u, v, directed=False):
    adj_matrix[u][v] = 1
    if not directed:
        adj_matrix[v][u] = 1


def is_hamiltonian_by_dirac(adj_matrix, directed=False):
    """
    Check if the graph satisfies Dirac's theorem.
    Dirac's theorem states that for a simple graph with n ≥ 3 vertices, 
    if each vertex has degree at least n / 2, the graph is Hamiltonian.

    Parameters:
        adj_matrix (list[list[int]]): Adjacency matrix.
        directed (bool): Whether the graph is directed.

    Returns:
        bool: True if the graph satisfies Dirac's theorem, False otherwise.
    """
    n = len(adj_matrix)
    if n < 3:
        return False  # Dirac's theorem does not apply

    for v in range(n):
        if directed:
            out_deg, in_deg = degree(adj_matrix, v, directed=True)
            if min(out_deg, in_deg) < n / 2:  # Ensure both out-degree and in-degree are checked
                return False
        else:
            if degree(adj_matrix, v, directed=False) < n / 2:  # Degree for undirected
                return False
    return True


def add_minimal_edges_by_dirac(adj_matrix, directed=False):
    """
    Add the minimal number of edges to satisfy Dirac's theorem.

    Parameters:
        adj_matrix (list[list[int]]): Adjacency matrix of the graph.
        directed (bool): Whether the graph is directed.

    Returns:
        list[list[int]]: Updated adjacency matrix.
    """
    n = len(adj_matrix)
    if n < 3:
        return adj_matrix  # Dirac's theorem doesn't apply
    
    # Initialize degree dictionary
    if directed:
        # For directed graphs, store (out-degree, in-degree)
        degrees = {i: (0, 0) for i in range(n)}
        for u in range(n):
            for v in range(n):
                if adj_matrix[u][v] == 1:
                    degrees[u] = (degrees[u][0] + 1, degrees[u][1])  # Increment out-degree of u
                    degrees[v] = (degrees[v][0], degrees[v][1] + 1)  # Increment in-degree of v
    else:
        # For undirected graphs, store just the degree
        degrees = {i: 0 for i in range(n)}
        for u in range(n):
            for v in range(n):
                if adj_matrix[u][v] == 1:
                    degrees[u] += 1
                    degrees[v] += 1

    def add_edge(adj_matrix, u, v, directed=False):
        """
        Adds an edge between vertices u and v.
        Updates the adjacency matrix and degree dictionary.
        """
        if directed:
            adj_matrix[u][v] = 1
            degrees[u] = (degrees[u][0] + 1, degrees[u][1])  # Increment out-degree of u
            degrees[v] = (degrees[v][0], degrees[v][1] + 1)  # Increment in-degree of v
        else:
            adj_matrix[u][v] = 1
            adj_matrix[v][u] = 1
            degrees[u] += 1
            degrees[v] += 1

    # Check and add edges to satisfy Dirac's theorem
    for u in range(n):
        for v in range(n):
            if u != v and adj_matrix[u][v] == 0:  # No edge between u and v
                if directed:
                    out_deg_u, in_deg_u = degrees[u]
                    out_deg_v, in_deg_v = degrees[v]
                    if out_deg_u < n / 2 or in_deg_v < n / 2:
                        add_edge(adj_matrix, u, v, directed=True)
                else:
                    if degrees[u] < n / 2 or degrees[v] < n / 2:
                        add_edge(adj_matrix, u, v, directed=False)

    return adj_matrix
