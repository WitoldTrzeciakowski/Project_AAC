import numpy as np
def determinant_of_matrix(matrix, tol=1e-12):
    """
    Calculate the determinant of a matrix using LU decomposition with partial pivoting.

    Parameters:
        matrix (list or numpy.ndarray): The input square matrix.
        tol (float): Tolerance for detecting singularity or near-singularity.

    Returns:
        float: The determinant of the matrix.
    """
    n = len(matrix)
    c = np.array(matrix, dtype=float)  
    p = list(range(n))  
    row_swaps = 0  

    for j in range(n):
        pivot = 0
        pivot_ind = -1
        for i in range(j, n):
            if abs(c[i, j]) > abs(pivot):
                pivot = c[i, j]
                pivot_ind = i
        if abs(pivot) < tol:
            #print(f"Matrix is singular or nearly singular at column {j}.")
            return 0  
        if pivot_ind != j:
            c[[j, pivot_ind]] = c[[pivot_ind, j]]   
            p[j], p[pivot_ind] = p[pivot_ind], p[j]
            row_swaps += 1
        for k in range(j + 1, n):
            c[k, j] /= c[j, j]  
            for q in range(j + 1, n):
                c[k, q] -= c[k, j] * c[j, q]
    diagonal_product = np.prod(np.diag(c)) 
    determinant_sign = (-1) ** row_swaps 
    determinant = determinant_sign * diagonal_product
    return determinant

import numpy as np

def eigenvalues_of_matrix(matrix):
    # Ensure the input is a numpy array
    matrix = np.array(matrix, dtype=int)
    
    # Calculate eigenvalues using numpy's built-in function
    eigenvalues = np.linalg.eigvals(matrix)
    
    # Round eigenvalues to 2 decimal points
    rounded_eigenvalues = np.round(eigenvalues, 2)
    
    # Sort the rounded eigenvalues
    sorted_eigenvalues = np.sort(rounded_eigenvalues)
    
    return sorted_eigenvalues

# matrix1 = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]]
# matrix2 = [[0, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0]]

# print(eigenvalues_of_matrix(matrix1))
# print(eigenvalues_of_matrix(matrix2))
