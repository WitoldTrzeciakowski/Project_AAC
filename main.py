import read_file
import graph_size
import easy_metric
import spectral_distance
#import Spectral_stuff.interface

print(" Algorithms and Computability Project \n Aleksandra Wieczorek, Witold Trzeciakowski, Szymon Kupisz \n")

######################### READING DATA #########################
print("     Reading Graphs from the file \n")

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

print("     Size of the graph\n")
print("Number of edges and number of verices \n")

for i, graph in enumerate(graph_data):
    print(f"Size of Graph {i + 1}:")
    for row in graph["adjacency_matrix"]:
        print(row)
    num_edges, num_vertices = graph_size.count_edges_vertices(graph)
    print("Number of vertices:", num_vertices)
    print("Number of edges:", num_edges)
    print()


############## RESONABLE METRIC #############################

print("     Reasonable Metric\n")
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


print("     Reasonable Metric\n")
print("Isomorphic graphs have the same spectral distance, \nHowever when the spectra are the same it doesn't mean taht the graphs are isomorphic and more calucaltions needs to be done ")

if len(adjacency_matrices) < 2:
    print("Error: At least two graphs are required for comparison.")
else:
    x = 1
    matrix1 = adjacency_matrices[f"M{x}"]
    for y in range(1,len(adjacency_matrices) + 1):
        matrix2 = adjacency_matrices[f"M{y}"]
        if spectral_distance.are_spectra_equal(matrix1, matrix2):
            print(f"Graph M{x} and Graph M{y} may be isomorphic (spectra match).")
        else:
            print(f"Graph M{x} and Graph M{y} are not isomorphic (spectra differ).")



## TODO::   - wyswietlac maciez obok metryki zbey bylo widac zi zeby nie trzeba bylo przewijac 
#           - edge raczej dwa razy liczyc w size zeby bylo tak samo i tej czesci 