def find_all_longest_cycles(adj_matrix):
    def backtrack(path, visited):
        current = path[-1]
        # Jeśli wracamy do początkowego wierzchołka i cykl jest Hamiltona
        if len(path) > 1 and current == path[0] and len(path) == len(adj_matrix) + 1:
            all_cycles.append(path[:])
            return

        for neighbor in range(len(adj_matrix)):
            if adj_matrix[current][neighbor] == 1:  # Jeśli istnieje krędźaw
                if neighbor not in visited or (neighbor == path[0] and len(path) == len(adj_matrix)):
                    path.append(neighbor)
                    if neighbor != path[0]: 
                        visited.add(neighbor)
                    backtrack(path, visited)
                    path.pop()
                    if neighbor != path[0]: 
                        visited.remove(neighbor)

    n = len(adj_matrix)
    all_cycles = []
    for start_node in range(n):
        backtrack([start_node], {start_node})
    max_length = max(len(cycle) for cycle in all_cycles) if all_cycles else 0
    longest_cycles = [cycle for cycle in all_cycles if len(cycle) == max_length]

    return longest_cycles
