import math

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

max_length, max_count = max_cycle_held_karp(graph1)
print("Maximum Cycle Length:", max_length)
print("Number of Maximum Cycles:", max_count)