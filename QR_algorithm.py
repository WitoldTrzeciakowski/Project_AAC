def transpose(matrix):
    """
    Transpose a matrix.
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiply(A, B):
    """
    Multiply two matrices A and B.
    """
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def identity_matrix(size):
    """
    Create an identity matrix of given size.
    """
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def gram_schmidt(A):
    """
    Perform the Gram-Schmidt process to obtain Q and R matrices.
    """
    n = len(A)
    Q = [[0] * n for _ in range(n)]
    R = [[0] * n for _ in range(n)]
    
    for j in range(n):
        v = [A[i][j] for i in range(n)]
        for i in range(j):
            R[i][j] = sum(Q[k][i] * A[k][j] for k in range(n))
            v = [v[k] - R[i][j] * Q[k][i] for k in range(n)]
        R[j][j] = sum(v[k] * 2 for k in range(n)) * 0.5
        for k in range(n):
            Q[k][j] = v[k] / R[j][j]
    
    return Q, R

def qr_algorithm(matrix, max_iterations=1000, tolerance=1e-10):
    """
    Use the QR algorithm to compute all eigenvalues of a square matrix.
    """
    n = len(matrix)
    A = [row[:] for row in matrix]  # Make a copy of the matrix
    for _ in range(max_iterations):
        Q, R = gram_schmidt(A)
        A_next = matrix_multiply(R, Q)
        if all(abs(A_next[i][j] - A[i][j]) < tolerance for i in range(n) for j in range(n)):
            break
        A = A_next
    return [A[i][i] for i in range(n)]  # Eigenvalues are on the diagonal of A

