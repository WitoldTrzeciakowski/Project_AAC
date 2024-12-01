
import random
def hamiltonian_extension_matrix(adj_matrix):
    """
    Rozszerzenie grafu do grafu Hamiltona na podstawie macierzy sąsiedztwa.

    Parametry:
        adj_matrix: list[list[int]] - kwadratowa macierz sąsiedztwa grafu (0 - brak krawędzi, 1 - istnieje krawędź).

    Zwraca:
        updated_matrix: list[list[int]] - rozszerzona macierz sąsiedztwa z cyklem Hamiltona.
    """
    n = len(adj_matrix)  
    visited = set()       
    path = []             

    degrees = [sum(row) for row in adj_matrix]
    current_node = degrees.index(max(degrees))
    path.append(current_node)
    visited.add(current_node)

    while len(path) < n:
        neighbors = [i for i, val in enumerate(adj_matrix[current_node]) if val == 1]
        unvisited_neighbors = [node for node in neighbors if node not in visited]

        if unvisited_neighbors:
            next_node = max(unvisited_neighbors, key=lambda node: sum(adj_matrix[node]))
        else:
            unvisited_nodes = [node for node in range(n) if node not in visited]
            next_node = max(unvisited_nodes, key=lambda node: sum(adj_matrix[node]))

            adj_matrix[current_node][next_node] = 1
            adj_matrix[next_node][current_node] = 1

        path.append(next_node)
        visited.add(next_node)
        current_node = next_node


    if adj_matrix[path[-1]][path[0]] == 0:
        adj_matrix[path[-1]][path[0]] = 1
        adj_matrix[path[0]][path[-1]] = 1

    return adj_matrix

def is_hamiltonian_cycle(graph):
    """
    Checks if a given graph contains a Hamiltonian cycle.

    Parameters:
        graph (list[list[int]]): Adjacency matrix of the graph.

    Returns:
        bool: True if a Hamiltonian cycle exists, False otherwise.
    """
    n = len(graph)
    if n == 0:
        return False  # No vertices, no cycle
    if n == 1:
        return graph[0][0] == 1  # Single vertex, self-loop is needed

    # Quick check: all vertices must have at least two edges for a cycle
    if any(sum(row) < 2 for row in graph):
        return False

    def backtrack(v, path_length, visited, path):
        visited[v] = True
        path.append(v)

        if path_length == n:
            # Check if there is an edge back to the starting vertex
            if graph[v][path[0]] == 1:
                return True
            visited[v] = False
            path.pop()
            return False

        # Try neighbors sorted by degree (heuristic to explore promising paths first)
        neighbors = sorted((u for u in range(n) if graph[v][u] == 1 and not visited[u]), 
                           key=lambda x: sum(graph[x]), 
                           reverse=True)

        for u in neighbors:
            if backtrack(u, path_length + 1, visited, path):
                return True

        # Backtrack
        visited[v] = False
        path.pop()
        return False

    visited = [False] * n
    path = []

    return backtrack(0, 1, visited, path)



