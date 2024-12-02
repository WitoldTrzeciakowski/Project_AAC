from functools import lru_cache

def maximum_cycle_dfs(adjacency_matrix):
    paths = []
    paths_sorted = []
    maximum_path_length = 0
    for starting_point in range (0, len(adjacency_matrix)):
        stack = [[starting_point, [starting_point]]]
        global adding_flag
        while len(stack) > 0:
            analyzed_path_data = stack.pop()
            initial_point_of_path = analyzed_path_data[0]
            analyzed_path = analyzed_path_data[1]
            last_point = analyzed_path[-1]
            current_options = adjacency_matrix[last_point]
            adding_flag = False
            ind = 0
            for option in current_options:
                if option != 0:
                    flag = False
                    for point in analyzed_path:
                        if point == ind:
                            flag = True
                            break
                    if flag == False :
                        operational_path = analyzed_path.copy()
                        operational_path.append(ind)
                        stack.append([initial_point_of_path, operational_path])
                        adding_flag = True
                ind+=1
            if adding_flag == False:
                if adjacency_matrix[last_point][initial_point_of_path] > 0:
                    current_length_of_path = len(analyzed_path)
                    if current_length_of_path == maximum_path_length:
                        sorted_path = sorted(analyzed_path)
                        is_present_flag = False
                        for analyzed_sorted_path in paths_sorted:
                            is_present_local = True
                            for i in range (0, len(analyzed_path)):
                                if sorted_path[i] != analyzed_sorted_path[i]:
                                    is_present_local = False
                                    break
                            if is_present_local == True:
                                is_present_flag = True
                                break
                        if is_present_flag == False:
                            paths.append(analyzed_path)
                            paths_sorted.append(sorted_path)
                    if current_length_of_path > maximum_path_length:
                        maximum_path_length = current_length_of_path
                        sorted_path = sorted(analyzed_path)
                        while len(paths) > 0:
                            paths.pop()
                        paths.append(analyzed_path)
                        paths_sorted.append(sorted_path)
    return paths

def maximum_cycle_dfs_optimized(adjacency_matrix):
    paths = set()
    maximum_path_length = 0
    n = len(adjacency_matrix)

    def dfs(node, start_node, visited, path):
        nonlocal maximum_path_length
        
        visited[node] = True
        path.append(node)

        for neighbor in range(n):
            if adjacency_matrix[node][neighbor] != 0: 
                if neighbor == start_node and len(path) > 2:
                    cycle_length = len(path)
                    if cycle_length > maximum_path_length:
                        maximum_path_length = cycle_length
                        paths.clear()
                        paths.add(tuple(path))
                    elif cycle_length == maximum_path_length:
                        paths.add(tuple(path))

                elif not visited[neighbor]:
                    dfs(neighbor, start_node, visited, path)

        visited[node] = False
        path.pop()

    for starting_point in range(n):
        visited = [False] * n 
        dfs(starting_point, starting_point, visited, [])

    return [list(cycle) for cycle in paths]

def sanitize_cycles(cycles):
    seen = set()
    result = []
    
    for cycle in cycles:
        sorted_tuple = tuple(sorted(cycle))
        if sorted_tuple not in seen:
            seen.add(sorted_tuple)
            result.append(cycle)
    
    return result
            

def find_max_cycles(adj_matrix):

    n = len(adj_matrix)

    @lru_cache(None)
    def dp(node, visited_mask, start):
        max_length, count = 0, 0

        for neighbor in range(n):  
            if adj_matrix[node][neighbor] > 0:
                if neighbor == start: 
                    max_length = max(max_length, 1)
                    count += 1
                elif not (visited_mask & (1 << neighbor)): 
                    next_length, next_count = dp(
                        neighbor, visited_mask | (1 << neighbor), start
                    )
                    if next_length + 1 > max_length:
                        max_length, count = next_length + 1, next_count
                    elif next_length + 1 == max_length:
                        count += next_count

        return max_length, count

    max_length = 0
    max_count = 0

    for start in range(n): 
        visited_mask = 1 << start
        cycle_length, cycle_count = dp(start, visited_mask, start)

        if cycle_length > max_length:
            max_length, max_count = cycle_length, cycle_count
        elif cycle_length == max_length:
            max_count += 1

    return max_length, max_count

def matrix_exponentiation_cycle_detection(adj_matrix, n):

    def multiply_matrices(A, B, size):
        result = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    def matrix_power(matrix, power, size):
        result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
        base = matrix
        while power:
            if power % 2 == 1:
                result = multiply_matrices(result, base, size)
            base = multiply_matrices(base, base, size)
            power //= 2
        return result

    powered_matrix = matrix_power(adj_matrix, n, n)

    max_length_of_cycle = 0
    number_of_cycles = 0
    for i in range(n):
        if powered_matrix[i][i] > 0:
            if max_length_of_cycle < powered_matrix[i][i]:
                number_of_cycles = 1
                max_length_of_cycle = powered_matrix[i][i]
            if max_length_of_cycle == powered_matrix[i][i]:
                number_of_cycles+=1

    return max_length_of_cycle, number_of_cycles

def find_max_cycle_length_and_count(adj_matrix):
    n = len(adj_matrix)  # Number of nodes
    max_cycle_length = 0
    cycle_count = 0

    def dfs(node, start, visited, path_length):
        nonlocal max_cycle_length, cycle_count
        visited[node] = True

        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1:  # There's an edge
                if neighbor == start and path_length > 2:  # Cycle found
                    max_cycle_length = max(max_cycle_length, path_length)
                    cycle_count += 1  # Increment the cycle count
                elif not visited[neighbor]:  # Continue DFS
                    dfs(neighbor, start, visited, path_length + 1)

        visited[node] = False  # Backtrack

    # Start DFS from every node
    for i in range(n):
        visited = [False] * n
        dfs(i, i, visited, 1)

    return max_cycle_length, cycle_count

def longest_cycle_length(adj_matrix):
    def matrix_mult(A, B):
        """Multiplies two matrices A and B."""
        n = len(A)
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
        return result

    def matrix_power(A, k):
        """Exponentiates matrix A to the power of k."""
        n = len(A)
        result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # Identity matrix
        base = A
        while k > 0:
            if k % 2 == 1:
                result = matrix_mult(result, base)
            base = matrix_mult(base, base)
            k //= 2
        return result

    n = len(adj_matrix)
    longest_cycle = 0

    # Check powers from 1 to n

    power_matrix = matrix_power(adj_matrix, n)
    max_length_of_cycle = 0
    number_of_cycles = 0
    for i in range(n):
        if power_matrix[i][i] > 0:
            if max_length_of_cycle < power_matrix[i][i]:
                number_of_cycles = 1
                max_length_of_cycle = power_matrix[i][i]
            if max_length_of_cycle == power_matrix[i][i]:
                number_of_cycles+=1

    for k in range(1, n+1):
        power_matrix = matrix_power(adj_matrix, k)
        total_cycles = sum(power_matrix[i][i] for i in range(len(adj_matrix)))
        total_cycles //=(2*k)
        if total_cycles > 0:
            longest_cycle = k

    return longest_cycle, number_of_cycles

def find_max_cycle(adj_matrix):
    def dfs(node, visited, path, start_node):
        nonlocal max_length
        if node in visited:
            if node == start_node:
                max_length = max(max_length, len(path))
            return
        visited.add(node)
        path.append(node)
        for neighbor, is_edge in enumerate(adj_matrix[node]):
            if is_edge:
                dfs(neighbor, visited, path, start_node)
        visited.remove(node)
        path.pop()

    max_length = 0
    n = len(adj_matrix)
    for i in range(n):
        visited = set()
        dfs(i, visited, [], i)
    return max_length

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
    num_vertices = random.randint(5, 10)  # Random number of vertices between 5 and 30
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

graph = generate_random_graph()
print(graph)

paths = maximum_cycle_dfs(graph)

paths2 = maximum_cycle_dfs_optimized(graph)
paths_sanitized = sanitize_cycles(paths2)

max_len, max_count = find_max_cycles(graph)

max_len_2, count = matrix_exponentiation_cycle_detection(graph, len(graph))

print(paths)
print(paths_sanitized)
print(max_len, max_count)
print(max_len_2, count)
print(find_max_cycle_length_and_count(graph))
print(longest_cycle_length(graph))
print(find_max_cycle(graph))
