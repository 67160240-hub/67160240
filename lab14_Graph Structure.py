class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.graph.get(node, []))
        return result

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_recursive(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.graph.get(node, []):
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result


if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'F')

    print("BFS:", g.bfs('A'))
    print("DFS:", g.dfs('A'))
