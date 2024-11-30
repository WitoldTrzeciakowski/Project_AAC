
from functools import lru_cache

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
            
def find_max_cycles_with_paths(adj_matrix):
    n = len(adj_matrix)

    @lru_cache(None)
    def dp(node, visited_mask, start):
        max_length, count = 0, 0
        all_paths = []

        for neighbor in range(n):
            if adj_matrix[node][neighbor] > 0:
                if neighbor == start: 
                    # Found a cycle
                    max_length = max(max_length, 1)
                    count += 1
                    all_paths.append([node, neighbor])  # Cycle path
                elif not (visited_mask & (1 << neighbor)):
                    # Continue DFS to find more cycles
                    next_length, next_count, next_paths = dp(
                        neighbor, visited_mask | (1 << neighbor), start
                    )
                    if next_length + 1 > max_length:
                        max_length = next_length + 1
                        count = next_count
                        all_paths = [[node] + path for path in next_paths]
                    elif next_length + 1 == max_length:
                        count += next_count
                        all_paths.extend([[node] + path for path in next_paths])

        return max_length, count, all_paths

    max_length = 0
    max_count = 0
    max_cycles = []

    for start in range(n):
        visited_mask = 1 << start
        cycle_length, cycle_count, cycles = dp(start, visited_mask, start)

        if cycle_length > max_length:
            max_length = cycle_length
            max_count = cycle_count
            max_cycles = cycles
        elif cycle_length == max_length:
            max_count += cycle_count
            max_cycles.extend(cycles)

    # Filter cycles to ensure they are unique (in case of duplicates)
    unique_cycles = []
    unique_length = 0
    seen = set()
    for cycle in max_cycles:
        # Normalize cycle (rotate to smallest starting point and make tuple for hashing)
        min_index = cycle.index(min(cycle))
        normalized_cycle = tuple(cycle[min_index:] + cycle[:min_index])
        if normalized_cycle not in seen:
            if len(cycle) == unique_length:
                seen.add(normalized_cycle)
                unique_cycles.append(cycle)
            if len(cycle) > unique_length:
                unique_length = len(cycle)
                seen.clear()
                seen.add(normalized_cycle)
                while len(unique_cycles) > 0:
                    unique_cycles.pop()
                unique_cycles.append(cycle)

    return max_length, unique_cycles


def sanitize_cycles_dp(cycles):
    seen = set()
    result = []
    
    for cycle in cycles:
        cycle_operand = cycle.copy()
        cycle_operand.pop()
        sorted_tuple = tuple(sorted(cycle_operand))
        if sorted_tuple not in seen:
            seen.add(sorted_tuple)
            result.append(cycle_operand)
    
    return result

graph1 = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

graph2 = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0],
]


adj_matrix = [
    [0, 1, 0, 0, 1], 
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
]

dfs_paths = maximum_cycle_dfs_optimized(graph2)
paths_sanitized = sanitize_cycles(dfs_paths)
print(f"Maximum Cycle Length (DFS): {len(paths_sanitized[0])}, Count: {len(paths_sanitized)}")

max_len_dp, max_cycles_dp = find_max_cycles_with_paths(graph2)
sanitized_dp_cycles = sanitize_cycles_dp(max_cycles_dp)
print(f"Maximum Cycle Length (Dynamic Programming): {max_len_dp}, Count: {len(sanitized_dp_cycles)}")