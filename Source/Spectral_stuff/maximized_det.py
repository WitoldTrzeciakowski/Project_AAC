from Spectral_stuff.egienvalue import calculate_largest_eigenvalue  # Correct module name assumed


def copy_matrix(matrix):
    """Creates a deep copy of a 2D list."""
    return [row[:] for row in matrix]


def greedy_edge_addition(adj_matrix, n):
    best_eigenvalue = calculate_largest_eigenvalue(adj_matrix)

    for _ in range(n):
        for i in range(len(adj_matrix)):
            for j in range(i + 1, len(adj_matrix)):
                if adj_matrix[i][j] == 0 and adj_matrix[j][i] == 0:
                    adj_matrix[i][j] = adj_matrix[j][i] = 1
                    new_eigenvalue = calculate_largest_eigenvalue(adj_matrix)
                    if new_eigenvalue > best_eigenvalue:
                        best_eigenvalue = new_eigenvalue
                        break
                    adj_matrix[i][j] = adj_matrix[j][i] = 0
    return adj_matrix
