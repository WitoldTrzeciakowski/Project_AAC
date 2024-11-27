from egienvalue import calculate_largest_eigenvalue  # Correct module name assumed


def copy_matrix(matrix):
    """Creates a deep copy of a 2D list."""
    return [row[:] for row in matrix]


def greedy_edge_addition(adj_matrix, n):
    best_matrix = copy_matrix(adj_matrix)
    best_eigenvalue = calculate_largest_eigenvalue(best_matrix)

    for _ in range(n):
        current_matrix = copy_matrix(best_matrix)
        current_eigenvalue = best_eigenvalue
        for i in range(len(adj_matrix)):
            for j in range(i + 1, len(adj_matrix)):
                if adj_matrix[i][j] == 0 and adj_matrix[j][i] == 0:
                    adj_matrix[i][j] = adj_matrix[j][i] = 1
                    new_eigenvalue = calculate_largest_eigenvalue(adj_matrix)
                    if new_eigenvalue > best_eigenvalue:
                        best_eigenvalue = new_eigenvalue
                        current_matrix = copy_matrix(adj_matrix)
                    adj_matrix[i][j] = adj_matrix[j][i] = 0

        best_matrix = copy_matrix(current_matrix)
    return best_matrix
