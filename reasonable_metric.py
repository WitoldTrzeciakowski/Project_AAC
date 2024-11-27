from read_file import read_graph_file
from graph_size import is_M_symetrical

def are_isomorphic(M1, M2):
    if M1 == M2: 
        return True
    
    # wielkosc grafu 
    if len(M1) != len(M2): 
        return False
    
    # degree sequence
    M1_degs = sorted([sum(row) for row in M1])
    M2_degs = sorted([sum(row) for row in M2]) 
    if M1_degs != M2_degs:
        return False
    
    # ilosc edge
    M1_edges = int(sum(M1_degs) / 2 )
    M2_edges = int(sum(M2_degs) / 2 )
    if M1_edges != M2_edges:
        return False


    
    return True

def reasonable_metric(M1, M2):
    if are_isomorphic(M1, M2):
        return 0
    

    return "Cokolwike"

file_path = 'example.txt'
graph_data = read_graph_file(file_path)
adjacency_matrices = {f"M{i+1}": data['adjacency_matrix'] for i, data in enumerate(graph_data)}

for key, matrix in adjacency_matrices.items():
    print(f"{key}:\n{matrix}")

# to poprawic dla wiekszej ilosc grafow oraz gdyby byl tylko 1 w pliku 
x, y = 1, 2 
matrix1 = adjacency_matrices[f"M{x}"]
matrix2 = adjacency_matrices[f"M{x}"]

print(is_M_symetrical(matrix2))

#result = are_isomorphic(matrix1, matrix2)
#print(f"Are M{x} and M{x} isomorphic?", result)


