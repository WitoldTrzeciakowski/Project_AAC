from matrix_det import determinant_of_matrix
import read_file

def compute_eigenvalues(matrix):
    """Compute eigenvalues of a square matrix."""

    # Find roots of the characteristic polynomial using a naive approach
    def characteristic_polynomial(matrix, lambda_val):
        n = len(matrix)
        identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        mat = [[matrix[i][j] - lambda_val * identity[i][j] for j in range(n)] for i in range(n)]
        #print(determinant_of_matrix(mat))
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


def can_be_isomorphic(M1, M2):
    # wielkosc grafu 
    if len(M1) != len(M2): 
        return False
    # degree sequence
    M1_degs = sorted([sum(row) for row in M1])
    M2_degs = sorted([sum(row) for row in M2]) 
    if M1_degs != M2_degs:
        return False
    return True


def are_spectra_equal(adj_matrix1, adj_matrix2):
    """Check if two graphs have the same spectrum."""
    if can_be_isomorphic(adj_matrix1, adj_matrix2):
        eigenvalues1 = compute_eigenvalues(adj_matrix1)
        eigenvalues2 = compute_eigenvalues(adj_matrix2)
        return sorted(eigenvalues1) == sorted(eigenvalues2)
    else:
        return False



file_path = 'example.txt'
graph_data = read_file.read_graph_file(file_path)

adjacency_matrices = {f"M{i+1}": data['adjacency_matrix'] for i, data in enumerate(graph_data)}

if len(adjacency_matrices) < 2:
    print("Error: At least two graphs are required for comparison.")
else:
    x = 1
    matrix1 = adjacency_matrices[f"M{x}"]
    for y in range(1,len(adjacency_matrices) + 1):
        matrix2 = adjacency_matrices[f"M{y}"]
        if are_spectra_equal(matrix1, matrix2):
            print(f"Graph M{x} and Graph M{y} may be isomorphic (spectra match).")
        else:
            print(f"Graph M{x} and Graph M{y} are not isomorphic (spectra differ).")



# # Example adjacency matrices for two graphs
# graph1 = [
#     [0, 1, 1, 0],
#     [1, 0, 1, 0],
#     [1, 1, 0, 1],
#     [0, 0, 1, 0]
# ]

# graph2 = [
#     [0, 1, 1, 1],
#     [1, 0, 0, 0],
#     [1, 0, 0, 1],
#     [1, 0, 1, 0]
# ]

# # Compute and compare spectra
# if are_spectra_equal(graph1, graph2):
#     print("The graphs may be isomorphic (spectra match).")
# else:
#     print("The graphs are not isomorphic (spectra differ).")
