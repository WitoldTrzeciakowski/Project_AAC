def is_M_symetrical(M):
    for i in range(len(M)):
        for j in range(i + 1, len(M)):
            if M[i][j] != M[j][i]:
                return False
    return True


def count_edges_vertices(graph):
    num_vertices = graph["num_vertices"]
    adjacency_matrix = graph["adjacency_matrix"]
    # dwa przypadki dla directed i undirected
    if is_M_symetrical(adjacency_matrix):
        num_edges = int(sum(sum(row) for row in adjacency_matrix) / 2 )
    else:
        num_edges = int(sum(sum(row) for row in adjacency_matrix))
    # jesli liczymy undirected edge jako dwa directed 
    #num_edges = int(sum(sum(row) for row in adjacency_matrix))
    
    return num_edges, num_vertices

