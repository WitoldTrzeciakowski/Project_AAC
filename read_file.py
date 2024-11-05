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

def investigate_adjacency_matrix_properties(graph):
    type = 'graph'
    directed = False
    matrix = graph['adjacency_matrix']

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

file_path = 'example.txt'
graph_data = read_graph_file(file_path)
for i, graph in enumerate(graph_data):
    print(f"Graph {i + 1}:")
    print("Number of vertices:", graph["num_vertices"])
    print("Adjacency Matrix:")
    for row in graph["adjacency_matrix"]:
        print(row)
    print("Additional Data:", graph["additional_data"])
    graph_type = investigate_adjacency_matrix_properties(graph)
    print('Type of the graph: ', graph_type['type'])
    print('Is directed: ',graph_type['directed'])
    print()
