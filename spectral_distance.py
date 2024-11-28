from matrix_det import determinant_of_matrix
import read_file
from QR_algorithm import qr_algorithm

def can_be_isomorphic(M1, M2):
    if len(M1) != len(M2): 
        return False
    M1_degs = sorted([sum(row) for row in M1])
    M2_degs = sorted([sum(row) for row in M2]) 
    if M1_degs != M2_degs:
        return False
    return True


def are_spectra_equal(adj_matrix1, adj_matrix2):
    """Check if two graphs have the same spectrum."""
    if can_be_isomorphic(adj_matrix1, adj_matrix2):
        eigenvalues1 = qr_algorithm(adj_matrix1)
        eigenvalues2 = qr_algorithm(adj_matrix2)
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

