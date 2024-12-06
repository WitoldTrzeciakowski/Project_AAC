def is_k2_join_kn4_plus_2k1(adj_matrix):
    n = len(adj_matrix)
    if any(len(row) != n for row in adj_matrix):
        return False
    degrees = [sum(row) for row in adj_matrix]
    k2_vertices = [i for i, degree in enumerate(degrees) if degree == n-1]
    if len(k2_vertices) != 2:
        return False
    remaining_vertices = [v for v in range(n) if v not in k2_vertices]
    submatrix = [[adj_matrix[i][j] for j in remaining_vertices] for i in remaining_vertices]
    visited = set()

    def dfs(v, submatrix):
        stack = [v]
        component = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                component.append(node)
                neighbors = [i for i, connected in enumerate(submatrix[node]) if connected]
                stack.extend(neighbors)
        return component

    components = []
    for v in range(len(submatrix)):
        if v not in visited:
            components.append(dfs(v, submatrix))
    component_sizes = sorted(len(c) for c in components)
    if component_sizes != [1, 1, n-4]:
        return False
    for v in k2_vertices:
        if not all(adj_matrix[v][rv] == 1 for rv in remaining_vertices):
            return False
    return True


def generate_k2_join_kn4_plus_2k1(n):
    adj_matrix = [[0] * n for _ in range(n)]
    adj_matrix[0][1] = adj_matrix[1][0] = 1
    for i in range(2, n-2):
        for j in range(2, n-2):
            if i != j:
                adj_matrix[i][j] = 1
    for k2_vertex in [0, 1]:
        for other_vertex in range(2, n):
            adj_matrix[k2_vertex][other_vertex] = 1
            adj_matrix[other_vertex][k2_vertex] = 1
    return adj_matrix
def is_k1_join_kn_minus_3_plus_2k1(adj_matrix):
    """Check if the graph is K1 ∨ (Kn−3 + 2K1)."""
    n = len(adj_matrix)
    if n < 5:
        return False

    # Check degrees: one vertex with degree n-1 (the K1), others should have degree n-4 or 1
    degrees = [sum(row) for row in adj_matrix]
    if degrees.count(n - 1) != 1:
        return False

    k1_vertex = degrees.index(n - 1)
    remaining_vertices = [i for i in range(n) if i != k1_vertex]

    # Verify K1 is connected to all other vertices
    if not all(adj_matrix[k1_vertex][v] == 1 for v in remaining_vertices):
        return False

    # Check the remaining vertices form Kn-3 + 2K1
    submatrix = [[adj_matrix[i][j] for j in remaining_vertices] for i in remaining_vertices]
    degrees = [sum(row) for row in submatrix]
    if degrees.count(n - 4) != n - 3 or degrees.count(0) != 2:
        return False

    return True

def is_k2_join_4k1(adj_matrix):
    """Check if the graph is K2 ∨ 4K1."""
    n = len(adj_matrix)
    if n != 6:
        return False  # Only valid for n = 6

    # Check degrees: two vertices with degree 5 (K2), others should have degree 2
    degrees = [sum(row) for row in adj_matrix]
    if degrees.count(5) != 2 or degrees.count(2) != 4:
        return False

    k2_vertices = [i for i, d in enumerate(degrees) if d == 5]
    remaining_vertices = [i for i in range(n) if i not in k2_vertices]

    # Verify K2 vertices are connected to each other
    if not adj_matrix[k2_vertices[0]][k2_vertices[1]] == 1:
        return False

    # Verify K2 vertices are connected to all remaining vertices
    for k2 in k2_vertices:
        if not all(adj_matrix[k2][v] == 1 for v in remaining_vertices):
            return False

    return True

def is_k1_join_k1_3_plus_k1(adj_matrix):
    """Check if the graph is K1 ∨ (K1,3 + K1)."""
    n = len(adj_matrix)
    if n != 6:
        return False  # Only valid for n = 6

    # Check degrees: one vertex with degree 5 (the K1), one with degree 3 (center of K1,3)
    # and four with degree 1 (leaves of K1,3 and the extra K1)
    degrees = [sum(row) for row in adj_matrix]
    if degrees.count(5) != 1 or degrees.count(3) != 1 or degrees.count(1) != 4:
        return False

    k1_vertex = degrees.index(5)
    center_vertex = degrees.index(3)
    leaf_vertices = [i for i in range(n) if degrees[i] == 1]

    # Verify K1 is connected to all other vertices
    if not all(adj_matrix[k1_vertex][i] == 1 for i in range(n) if i != k1_vertex):
        return False

    # Verify center of K1,3 is connected to exactly 3 leaf vertices
    if not all(adj_matrix[center_vertex][leaf] == 1 for leaf in leaf_vertices[:3]):
        return False

    return True

def identify_graph(adj_matrix):
    """Identify which graph (if any) the adjacency matrix represents."""
    if is_k1_join_kn_minus_3_plus_2k1(adj_matrix):
        return "K1 ∨ (Kn−3 + 2K1)"
    elif is_k2_join_4k1(adj_matrix):
        return "K2 ∨ 4K1"
    elif is_k1_join_k1_3_plus_k1(adj_matrix):
        return "K1 ∨ (K1,3 + K1)"
    else:
        return "Unknown graph"
