import numpy as np
from egienvalue import calculate_largest_eigenvalue

def largest_eigenvalue(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    return max(abs(eigenvalues))

def greedy_edge_addition(adj_matrix, n):
    best_matrix = np.copy(adj_matrix)
    best_eigenvalue = largest_eigenvalue(best_matrix)
    
    for _ in range(n):
        current_matrix = np.copy(best_matrix)
        current_eigenvalue = best_eigenvalue
        for i in range(len(adj_matrix)):
            for j in range(i + 1, len(adj_matrix)):
                if adj_matrix[i][j] == 0:  
                    adj_matrix[i][j] = adj_matrix[j][i] = 1
                    new_eigenvalue = largest_eigenvalue(adj_matrix)
                    if new_eigenvalue > best_eigenvalue:
                        best_eigenvalue = new_eigenvalue
                        current_matrix = np.copy(adj_matrix) 
                    adj_matrix[i][j] = adj_matrix[j][i] = 0  

        best_matrix = np.copy(current_matrix)  
    return best_matrix
