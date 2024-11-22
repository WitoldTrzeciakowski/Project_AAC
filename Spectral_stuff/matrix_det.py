def get_cofactor(mat, p, q, n):
    temp = []
    for row in range(n):
        if row != p:
            new_row = [mat[row][col] for col in range(n) if col != q]
            temp.append(new_row)
    return temp

def determinant_of_matrix(mat):
    n = len(mat)
    if n == 1:
        return mat[0][0]
    D = 0
    sign = 1
    for f in range(n):
        temp = get_cofactor(mat, 0, f, n)
        D += sign * mat[0][f] * determinant_of_matrix(temp)
        sign = -sign
    return D

