import read_file

def count_edges_vertices(graph):
    num_vertices = graph["num_vertices"]
    adjacency_matrix = graph["adjacency_matrix"]
    num_edges = int(sum(sum(row) for row in adjacency_matrix) / 2 )

    return num_edges, num_vertices

def chromatic_index(graph):
    # By Vizing’s Theorem 
    # and generalization of this for mulit but i am not sure about this
    # https://web.pdx.edu/~caughman/501%20Dunaway.pdf -> mulitgraph
    adjacency_matrix = graph["adjacency_matrix"]
    max_element = max(max(sublist) for sublist in adjacency_matrix)
    v_deg = [sum(deg) for deg in adjacency_matrix]
    if max_element == 1:
        return max(v_deg) , max(v_deg) + 1
    else: 
        return max(v_deg) + max_element, -1

file_path = 'example.txt'
graph_data = read_file.read_graph_file(file_path)

for i, graph in enumerate(graph_data):
    num_edges, num_vertices = count_edges_vertices(graph)
    chromatic_index_1 , chromatic_index_2 = chromatic_index(graph)
    print(f"Size of Graph {i + 1}:")
    print("Number of vertices:", num_vertices)
    print("Number of edges:", num_edges)
    if chromatic_index_2 == -1:
        print(f"Chromatic index is at most {chromatic_index_1} and it is a multigraph")
    else: 
        print(f"Chromatic index is at most {chromatic_index_1} or {chromatic_index_2} \nFrom what i know checking which one is correct is NP-Complete <3")
    print()
