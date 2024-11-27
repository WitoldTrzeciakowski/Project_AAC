import read_file 

def calculate_matrix_to_match(matrix1, matrix2):
    
    if len(matrix1) < len(matrix2):
        M_smaller = matrix1
        M_bigger = matrix2
    else:
        M_smaller = matrix2
        M_bigger = matrix1
    
    rows_smaller = len(M_smaller)
    cols_smaller = len(M_smaller[0]) if rows_smaller > 0 else 0
    
    rows_bigger = len(M_bigger)
    cols_bigger = len(M_bigger[0]) if rows_bigger > 0 else 0
    
    expanded_M_smaller = [[0 for _ in range(cols_bigger)] for _ in range(rows_bigger)]
    
    for i in range(rows_smaller):
        for j in range(cols_smaller):
            expanded_M_smaller[i][j] = M_smaller[i][j]
    
    M3 = [[M_bigger[i][j] - expanded_M_smaller[i][j] for j in range(cols_bigger)] for i in range(rows_bigger)]

    M3_abs = [[abs(M_bigger[i][j] - expanded_M_smaller[i][j]) for j in range(cols_bigger)] for i in range(rows_bigger)]
    added_E = sum(sum(row) for row in M3_abs)# kazdy undirected graf traktujemy jako directed 
    added_V = len(M_bigger) - len(M_smaller)

    return M3, (added_E, added_V)

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
        M3, EV_num = calculate_matrix_to_match(matrix1, matrix2)
        print(f"Distance between Graph{x} and Graph{y}:")
        print(f"The number of edges that we need to add or delete: {EV_num[0]} \nThe number of vertices that we need to add or delete: {EV_num[1]}" )
        print()
