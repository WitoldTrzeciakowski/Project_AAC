import read_file 

def calculate_matrix_to_match(M_smaller, M_bigger):
    rows_smaller = len(M_smaller)
    cols_smaller = len(M_smaller[0]) if rows_smaller > 0 else 0
    
    rows_bigger = len(M_bigger)
    cols_bigger = len(M_bigger[0]) if rows_bigger > 0 else 0
    
    expanded_M_smaller = [[0 for _ in range(cols_bigger)] for _ in range(rows_bigger)]
    
    for i in range(rows_smaller):
        for j in range(cols_smaller):
            expanded_M_smaller[i][j] = M_smaller[i][j]
    
    M3 = [[M_bigger[i][j] - expanded_M_smaller[i][j] for j in range(cols_bigger)] for i in range(rows_bigger)]
    
    return M3

file_path = 'example.txt'
graph_data = read_file.read_graph_file(file_path)

adjacency_matrices = {f"M{i+1}": data['adjacency_matrix'] for i, data in enumerate(graph_data)}

for key, matrix in adjacency_matrices.items():
    print(f"{key}:\n{matrix}")

if len(adjacency_matrices) < 2:
    print("Error: At least two graphs are required for comparison.")
else:
    x, y = 1, 2 
    
    matrix1 = adjacency_matrices[f"M{x}"]
    matrix2 = adjacency_matrices[f"M{y}"]
    
    if len(matrix1) < len(matrix2):
        M3 = calculate_matrix_to_match(matrix1, matrix2)
    else:
        M3 = calculate_matrix_to_match(matrix2, matrix1)
    
    print("Matrix to add to smaller one so it will become bigger one - M3:")
    print(M3)
