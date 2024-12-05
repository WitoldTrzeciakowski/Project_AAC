def read_graph_file(file_path):
    graphs = []
    with open(file_path, 'r') as f:
        num_graphs = int(f.readline().strip())
        
        for _ in range(num_graphs):
            num_vertices = int(f.readline().strip())
            adjacency_matrix = []
            
            for _ in range(num_vertices):
                row = list(map(int, f.readline().strip().split()))
                adjacency_matrix.append(row)
            
            additional_data = []
            while True:
                line = f.readline().strip()
                if not line:  
                    break
                additional_data.append(line)
            
            graphs.append({
                "num_vertices": num_vertices,
                "adjacency_matrix": adjacency_matrix,
                "additional_data": additional_data
            })
    
    return graphs

def make_graph(adjacency_matrix):
    graph = {
        "adjacency_matrix": adjacency_matrix,
    }
    return graph

def investigate_adjacency_matrix_properties(graph):
    type = 'simple graph'
    directed = False
    matrix = graph["adjacency_matrix"]

    for i in range (0, len(matrix), 1):
        for j in range(0, i, 1):
            if matrix[i][j] != matrix[j][i] :
                directed = True
            if matrix[i][j] > 1 or matrix[j][i] > 1 :
                type='multigraph'
    return {
        "type": type,
        "directed": directed
    }

def prepare_adjacency_matrix_for_hamiltonian_path(adj_matrix):
    n = len(adj_matrix)
    
    for i in range(n):
        for j in range(n):
            adj_matrix[i][j] = 1 if adj_matrix[i][j] > 0 else 0
        adj_matrix[i][i] = 0

    return adj_matrix
