
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def make_set(self, vertex):
        self.parent[vertex] = vertex
        self.size[vertex] = 1

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  # Kompresja ścieżki
        return self.parent[vertex]

    def union(self, v, u):
        root_v = self.find(v)
        root_u = self.find(u)

        if root_v == root_u:
            return

        # Łączenie przez rangę (rozmiar)
        if self.size[root_v] < self.size[root_u]:
            root_v, root_u = root_u, root_v

        self.parent[root_u] = root_v
        self.size[root_v] += self.size[root_u]



def find_minimal_extension_to_hamiltonian_cycle(graph):
    n = len(graph)
    uf = UnionFind()

    for vertex in range(n):
        uf.make_set(vertex)

    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                uf.union(i, j)

    components = {}
    for vertex in range(n):
        root = uf.find(vertex)
        if root not in components:
            components[root] = []
        components[root].append(vertex)

    component_roots = list(components.keys())
    if len(component_roots) > 1:
        for i in range(len(component_roots) - 1):
            root1 = component_roots[i]
            root2 = component_roots[i + 1]
            v = components[root1][0]
            u = components[root2][0]
            graph[v][u] = 1
            graph[u][v] = 1
            uf.union(v, u)

    degrees = [sum(row) for row in graph]
    vertices_with_low_degree = [v for v, d in enumerate(degrees) if d < 2]

    # Próba parowania wierzchołków ze stopniem < 2
    while len(vertices_with_low_degree) >= 2:
        v = vertices_with_low_degree.pop()
        u = vertices_with_low_degree.pop()
        if graph[v][u] == 0:
            graph[v][u] = 1
            graph[u][v] = 1
            uf.union(v, u)
            if sum(graph[v]) < 2:
                vertices_with_low_degree.append(v)
            if sum(graph[u]) < 2:
                vertices_with_low_degree.append(u)
    if len(vertices_with_low_degree) == 1:
        v = vertices_with_low_degree.pop()
        for u in range(n):
            if graph[v][u] == 0 and sum(graph[u]) >= 2:
                graph[v][u] = 1
                graph[u][v] = 1
                uf.union(v, u)
                break
        else:
            for u in range(n):
                if graph[v][u] == 0:
                    graph[v][u] = 1
                    graph[u][v] = 1
                    uf.union(v, u)
                    break
    path = []
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        path.append(v)
        for u in range(n):
            if graph[v][u] == 1 and not visited[u]:
                dfs(u)

    dfs(0)

    if len(path) == n:
        if graph[path[-1]][path[0]] == 1:
            return graph
        else:
            graph[path[-1]][path[0]] = 1
            graph[path[0]][path[-1]] = 1

    return graph
