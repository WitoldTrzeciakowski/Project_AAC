from matrix_det import determinant_of_matrix
def compute_eigenvalues(matrix):
    """Compute eigenvalues of a square matrix."""

    # Find roots of the characteristic polynomial using a naive approach
    def characteristic_polynomial(matrix, lambda_val):
        n = len(matrix)
        identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        mat = [[matrix[i][j] - lambda_val * identity[i][j] for j in range(n)] for i in range(n)]
        print(determinant_of_matrix(mat))
        return determinant_of_matrix(mat)

    # Compute eigenvalues by finding roots of the characteristic polynomial
    eigenvalues = []
    resolution = 0.01  # Resolution for root finding
    lower_bound = -100  # Adjust based on expected eigenvalues
    upper_bound = 100   # Adjust based on expected eigenvalues
    
    for lambda_val in [lower_bound + i * resolution for i in range(int((upper_bound - lower_bound) / resolution))]:
        if abs(characteristic_polynomial(matrix, lambda_val)) < resolution:
            if not eigenvalues or abs(eigenvalues[-1] - lambda_val) > resolution:
                eigenvalues.append(round(lambda_val, 2))
    
    return eigenvalues

def are_spectra_equal(adj_matrix1, adj_matrix2):
    """Check if two graphs have the same spectrum."""
    eigenvalues1 = compute_eigenvalues(adj_matrix1)
    eigenvalues2 = compute_eigenvalues(adj_matrix2)
    return sorted(eigenvalues1) == sorted(eigenvalues2)

# Example adjacency matrices for two graphs
graph1 = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

graph2 = [
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0]
]

# Compute and compare spectra
if are_spectra_equal(graph1, graph2):
    print("The graphs may be isomorphic (spectra match).")
else:
    print("The graphs are not isomorphic (spectra differ).")
