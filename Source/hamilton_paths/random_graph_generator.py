import numpy as np
import random

def generate_random_graph(directed=False):
    """
    Generates a random directed or undirected connected graph as an adjacency matrix.

    Parameters:
        directed (bool): True if the graph is directed, False if undirected.

    Returns:
        adj_matrix (numpy.ndarray): Adjacency matrix of the generated graph.
    """
    num_vertices = random.randint(5, 30)  # Random number of vertices between 5 and 30
    density = random.uniform(0.1, 0.9)   # Random density between 0.1 and 0.9

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

# Example usage
graph = generate_random_graph(directed=False)
print("Generated Adjacency Matrix:")
for row in graph:
    print(row)
