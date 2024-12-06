def is_M_symetrical(M):
    for i in range(len(M)):
        for j in range(i + 1, len(M)):
            if M[i][j] != M[j][i]:
                return False
    return True

def size_of_the_graph(matrix):
        num_vertices = len(matrix)
        num_edges = int(sum(sum(row) for row in matrix))
        return num_edges, num_vertices
