import size_metric.read_file as read_file
import size_metric.graph_size as graph_size
import size_metric.easy_metric as easy_metric
import size_metric.spectral_distance as spectral_distance
import interface_hamilton_cycle
import maximum_cycle
#import Spectral_stuff.interface

print(" Algorithms and Computability Project \n Aleksandra Wieczorek, Witold Trzeciakowski, Szymon Kupisz \n")

######################### READING DATA #########################
print("...reading graphs from the file...\n")

#file_path = input("Enter file path: ")
file_path = "example.txt"

graph_data = read_file.read_graph_file(file_path)

# for i, graph in enumerate(graph_data):
#     print(f"Graph {i + 1}:")
#     print("Number of vertices:", graph["num_vertices"])
#     print("Adjacency Matrix:")
#     for row in graph["adjacency_matrix"]:
#         print(row)
#     print("Additional Data:", graph["additional_data"])
#     graph_type = read_file.investigate_adjacency_matrix_properties(graph)
#     print('Type of the graph: ', graph_type['type'])
#     print('Is directed: ',graph_type['directed'])
#     print()


####################### SIZE OF THE GRAPH ##########################

print("     SIZE OF THE GRAPH \n")
print("Number of edges and number of verices \n")
print("NOTE:: One undirected edge is counted as two directed edges ")

for i, graph in enumerate(graph_data):
    print(f"Size of Graph G{i + 1}:")
    adjacency_matrix = graph["adjacency_matrix"]
    for row in adjacency_matrix:
        print(row)
    num_edges, num_vertices = graph_size.size_of_the_graph(adjacency_matrix)
    print("Number of vertices:", num_vertices)
    print("Number of edges:", num_edges)
    print()


############## RESONABLE METRIC #############################

print("     REASONABLE METRIC - MATRIX COMPARISION \n")
print("Number of operation that need to be done for matrix representing the graph to be the same")
print("NOTE:: In this metric we count one undirected edge as two directed edges for making the metric working for all types of graphs \n")

adjacency_matrices = {f"M{i+1}": data['adjacency_matrix'] for i, data in enumerate(graph_data)}


if len(adjacency_matrices) < 2:
    print("Error: At least two graphs are required for comparison.")
else:
    x = 1
    matrix1 = adjacency_matrices[f"M{x}"]
    for y in range(1, len(adjacency_matrices) + 1):

        matrix2 = adjacency_matrices[f"M{y}"]
        max_rows = max(len(matrix1), len(matrix2))
        
        print(f"Comparing Graph{x} and Graph{y}: \n")
        for i in range(max_rows):
            row1 = matrix1[i] if i < len(matrix1) else " " * len(str(matrix1[0]))
            row2 = matrix2[i] if i < len(matrix2) else " " * len(str(matrix2[0])) 
            print(f"{row1}      {row2}")

        M3, EV_num = easy_metric.calculate_matrix_to_match(matrix1, matrix2)
        print(f"The number of edges that we need to add or delete: {EV_num[0]}")
        print(f"The number of vertices that we need to add or delete: {EV_num[1]}")
        print()


print("     REASONABLE METRIC - SPECTRA \n")
print("Isomorphic graphs have the same spectral distance, \nHowever when the spectra are the same it doesn't mean taht the graphs are isomorphic and more calucaltions needs to be done \n")

if len(adjacency_matrices) < 2:
    print("Error: At least two graphs are required for comparison.")
else:
    x = 1
    matrix1 = adjacency_matrices[f"M{x}"]
    for y in range(1,len(adjacency_matrices) + 1):
        matrix2 = adjacency_matrices[f"M{y}"]
        if spectral_distance.are_spectra_equal(matrix1, matrix2):
            print(f"Graph G{x} and Graph G{y} may be isomorphic (spectra match).")
        else:
            print(f"Graph G{x} and Graph G{y} are not isomorphic (spectra differ).")


############ Maximum cycle in a graph and the number of such cycles ###################
    print("\n       MAXIMUM CYCLE \n ")
    print("NOTE:: the heuristic solution is applicable only to the cyclic graphs. In case of the acyclic graphs, the results can be far from the exact ones")
    adjacency_matrices = {f"M{i+1}": data['adjacency_matrix'] for i, data in enumerate(graph_data)}
    for i in range(1, len(adjacency_matrices)+1):
        matrix_graph = adjacency_matrices[f"M{i}"]
        print()
        print(f"  Graph G{i}")

        print("Exact solution using the DFS algorithm")
        paths = maximum_cycle.maximum_cycle_dfs_optimized(matrix_graph)
        print("Maximum cycle length:", len(paths[0]) if paths else 0)
        print("Number of maximum cycles:", len(paths))

        print("\nApproximate solution with the use of matrix exponentiation:")
        max_length_heuristic, number_of_paths_heuristic = maximum_cycle.longest_cycle_length(matrix_graph)
        print("Maximum cycle length:", max_length_heuristic)
        print("Number of maximum cycles:", number_of_paths_heuristic)



############ Hamilton Paths and cycles #############

print("\n\n       HAMILTON CYCLE \n ")
adjacency_matrices = {f"M{i+1}": data['adjacency_matrix'] for i, data in enumerate(graph_data)}
indeks = 1
for adjecency_matrix in adjacency_matrices.values():
    print(f"   Graph G{indeks}")
    indeks += 1
    
    print("Adjacency Matrix:")
    for row in adjecency_matrix:
        print(row)
    directed = read_file.investigate_adjacency_matrix_properties(graph)["directed"]
    print(f"is the graph directed: {directed}")
    interface_hamilton_cycle.do_check_on_graph(adjecency_matrix, directed)


