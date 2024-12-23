from size_metric.QR_algorithm import qr_algorithm

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

