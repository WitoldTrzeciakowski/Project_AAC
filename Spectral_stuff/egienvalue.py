def matrix_multiply(A, B):
    """ Multiplies two matrices A and B. """
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            row.append(sum(A[i][k] * B[k][j] for k in range(len(A[0]))))
        result.append(row)
    return result

def vector_matrix_multiply(A, v):
    """ Multiplies matrix A with vector v. """
    result = []
    for i in range(len(A)):
        result.append(sum(A[i][j] * v[j] for j in range(len(A[i]))))
    return result

def normalize_vector(v):
    """ Normalize a vector to unit length. """
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v]

def calculate_largest_eigenvalue(matrix, initial_guess=None, tolerance=1e-6, max_iter=10):
    """ Computes the largest eigenvalue of a matrix using the power iteration method. """
    n = len(matrix)
    
    if initial_guess is None:
        initial_guess = [1.0] * n
    
    x = initial_guess[:] 
    lambda_old = 0.0

    for _ in range(max_iter):
        x_new = vector_matrix_multiply(matrix, x)
        lambda_new = max(abs(xi) for xi in x_new)
        x_new = normalize_vector(x_new)
        if abs(lambda_new - lambda_old) < tolerance:
            break
        
        x = x_new
        lambda_old = lambda_new

    return lambda_new