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
