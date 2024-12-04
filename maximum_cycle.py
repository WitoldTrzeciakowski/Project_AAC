import size_metric.read_file

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

    return_list =  [list(cycle) for cycle in paths]
    list_sanitized = sanitize_cycles(return_list)
    return list_sanitized


def sanitize_cycles(cycles):
    seen = set()
    result = []
    
    for cycle in cycles:
        sorted_tuple = tuple(sorted(cycle))
        if sorted_tuple not in seen:
            seen.add(sorted_tuple)
            result.append(cycle)
    
    return result

def longest_cycle_length(adj_matrix):
    def matrix_mult(A, B):
        n = len(A)
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
        return result

    def matrix_power(A, k):
        n = len(A)
        result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        base = A
        while k > 0:
            if k % 2 == 1:
                result = matrix_mult(result, base)
            base = matrix_mult(base, base)
            k //= 2
        return result

    n = len(adj_matrix)
    longest_cycle = 0
    number_of_cycles = 0
    matrix_properties = size_metric.read_file.investigate_adjacency_matrix_properties({
        "adjacency_matrix": adj_matrix
    })
    divider = 1
    if matrix_properties["directed"] == False:
        divider = 2

    for k in range(1, n+1):
        power_matrix = matrix_power(adj_matrix, k)
        total_cycles = sum(1 for i in range(n) if power_matrix[i][i] > 0)
        total_cycles //= divider
        if total_cycles > 0:
            number_of_cycles = total_cycles
            longest_cycle = k

    return longest_cycle, number_of_cycles