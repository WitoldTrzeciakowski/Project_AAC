import time
import random
import numpy as np
from size_metric.easy_metric import calculate_matrix_to_match
from size_metric.spectral_distance import are_spectra_equal

def measure_execution_time(func, *args, **kwargs):
    """
    Measures the execution time of a function.
    Args:
        func: The function to measure.
        *args: Positional arguments for the function.
        **kwargs: Keyword arguments for the function.
    Returns:
        result: The result of the function call.
        elapsed_time: Time in seconds the function took to execute.
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed_time = time.perf_counter() - start_time
    return result, elapsed_time

def generate_random_graph(directed, num_vertices):
    """
    Generates a random directed or undirected connected graph as an adjacency matrix.

    Parameters:
        directed (bool): True if the graph is directed, False if undirected.

    Returns:
        adj_matrix (numpy.ndarray): Adjacency matrix of the generated graph.
    """
    #num_vertices = random.randint(2,100)  # Random number of vertices between 5 and 20
    density = random.uniform(0.1, 0.8)   # Random density between 0.1 and 0.9

    # Ensure a spanning tree is created for connectivity
    adj_matrix = np.zeros((num_vertices, num_vertices), dtype=int)

    # Create a spanning tree
    vertices = list(range(num_vertices))
    random.shuffle(vertices)
    for i in range(1, num_vertices):
        u = vertices[i]
        v = random.choice(vertices[:i])  # Connect the current vertex to one of the previous vertices
        adj_matrix[u][v] = 1
        if not directed:
            adj_matrix[v][u] = 1

    # Add additional edges based on density
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if directed or i != j:  # Avoid self-loops
                if random.random() < density and adj_matrix[i][j] == 0:
                    adj_matrix[i][j] = 1
                    if not directed:
                        adj_matrix[j][i] = 1

    return adj_matrix

def test_computational_performance():
    # Functions to test
    functions = {
        "Operation for matrices to match": lambda g: calculate_matrix_to_match(g[0], g[1]),
        "Spectra Equality": lambda g: are_spectra_equal(g[0], g[1]),
    }

    results = {func_name: {} for func_name in functions.keys()}
    num_iterations = 100
    num_vertices_list = [5, 10, 15, 20]

    for num_vertices in num_vertices_list:
        directed = random.choice([True, False])
        for func_name, func in functions.items():
            total_time = 0
            successful_runs = 0
            for _ in range(1):
                try:
                    # Generate random graph of a specific size
                    graph1 = generate_random_graph(directed, num_vertices)
                    graph = (graph1, graph1)

                    _, elapsed_time = measure_execution_time(func, graph)
                    total_time += elapsed_time
                    successful_runs += 1
                except Exception as e:
                    print(f"Error in {func_name}: {str(e)}")
            
            if successful_runs > 0:
                avg_time = total_time / successful_runs
            else:
                avg_time = float('inf')  # Indicate failure for all runs

            results[func_name][num_vertices] = avg_time

    return results


# if __name__ == "__main__":
#     performance_results = test_computational_performance()
#     print(performance_results)
#     avg_time_visualization(performance_results)
