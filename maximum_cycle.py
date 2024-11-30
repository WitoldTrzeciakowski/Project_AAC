import math

def held_karp_max_cycles_with_paths(adj_matrix):

    n = len(adj_matrix)  
    dp = [[-math.inf] * n for _ in range(1 << n)]  
    paths = [[[] for _ in range(n)] for _ in range(1 << n)]  

    for i in range(n):
        dp[1 << i][i] = 0  
        paths[1 << i][i] = [[i]]  

    for mask in range(1 << n):
        for u in range(n):  
            if not (mask & (1 << u)):  
                continue
            for v in range(n): 
                if u == v or not (mask & (1 << v)):  
                    continue
                if adj_matrix[v][u]:  
                    new_length = dp[mask ^ (1 << u)][v] + 1
                    if new_length > dp[mask][u]:
                        dp[mask][u] = new_length
                        paths[mask][u] = [path + [u] for path in paths[mask ^ (1 << u)][v]] 
                    elif new_length == dp[mask][u]:
                        paths[mask][u].extend(path + [u] for path in paths[mask ^ (1 << u)][v]) 

    max_cycle_length = -math.inf
    max_cycle_paths = []
    final_mask = (1 << n) - 1 

    for u in range(n):
        if adj_matrix[u][0]:  
            cycle_length = dp[final_mask][u] + 1
            if cycle_length > max_cycle_length:
                max_cycle_length = cycle_length
                max_cycle_paths = [path + [0] for path in paths[final_mask][u]] 
            elif cycle_length == max_cycle_length:
                max_cycle_paths.extend(path + [0] for path in paths[final_mask][u])

    return max_cycle_length if max_cycle_length != -math.inf else None, max_cycle_paths

def analyze_paths(paths):
    final_paths = []
    for path in paths:
        if path[0] != path[-1]:
            continue
        else:
            flag = False
            for path_analyze in final_paths:
                if path_analyze == path[::-1]:
                    flag = True
                    break
            if flag == False:
                final_paths.append(path)
    return final_paths

def max_cycle_held_karp(adj_matrix):

    n = len(adj_matrix)
    dp = [[-math.inf] * n for _ in range(1 << n)] 
    count = [[0] * n for _ in range(1 << n)]

    for i in range(n):
        dp[1 << i][i] = 0 
        count[1 << i][i] = 1 

    for mask in range(1 << n):
        for u in range(n): 
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if u == v or not (mask & (1 << v)):
                    continue
                if adj_matrix[v][u]:
                    new_length = dp[mask ^ (1 << u)][v] + 1
                    if new_length > dp[mask][u]:
                        dp[mask][u] = new_length
                        count[mask][u] = count[mask ^ (1 << u)][v]
                    elif new_length == dp[mask][u]:
                        count[mask][u] += count[mask ^ (1 << u)][v]

    max_cycle_length = -math.inf
    max_cycle_count = 0
    final_mask = (1 << n) - 1

    for u in range(n):
        if adj_matrix[u][0]:
            cycle_length = dp[final_mask][u] + 1
            if cycle_length > max_cycle_length:
                max_cycle_length = cycle_length
                max_cycle_count = count[final_mask][u]
            elif cycle_length == max_cycle_length:
                max_cycle_count += count[final_mask][u]

    return max_cycle_length if max_cycle_length != -math.inf else None, max_cycle_count

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

def find_max_cycle_length(adj_matrix):
    def dfs_cycle(start_node):
        visited = [] 
        current_node = start_node
        while True:
            visited.append(current_node)
            neighbors = [
                (i, sum(adj_matrix[i]) - adj_matrix[i][current_node]) 
                for i in range(len(adj_matrix)) 
                if adj_matrix[current_node][i] == 1 and i not in visited
            ]
            
            if not neighbors:
                break
            
            neighbors.sort(key=lambda x: x[1])  
            current_node = neighbors[0][0]  

        if adj_matrix[visited[-1]][visited[0]] == 1:
            return visited 
        return None

    all_cycles = []
    for start_node in range(len(adj_matrix)):
        cycle = dfs_cycle(start_node)
        if cycle:
            all_cycles.append(cycle)

    if not all_cycles:
        return 0, 0  

    max_length = max(len(cycle) for cycle in all_cycles)
    max_length_count = sum(1 for cycle in all_cycles if len(cycle) == max_length)

    return max_length, max_length_count


adj_matrix = [
    [0, 1, 0, 0, 1], 
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
]

max_length, max_count = find_max_cycle_length(graph2)
print(f"Maximum Cycle Length: {max_length}, Count: {max_count}")


max_length, max_count = max_cycle_held_karp(graph2)
print("Maximum Cycle Length:", max_length)
print("Number of Maximum Cycles:", max_count)
max_length, max_paths = held_karp_max_cycles_with_paths(graph2)
max_paths_sanitized = analyze_paths(max_paths)
print("Maximum Cycle Length:", max_length)
print("Maximum Cycle Paths:", len(max_paths_sanitized))