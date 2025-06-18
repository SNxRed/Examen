from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(dict)
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = {}
    
    def add_edge(self, v1, v2, weight=1):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj_list[v1][v2] = weight
        self.adj_list[v2][v1] = weight  # Para grafo no dirigido
    
    def get_vertices(self):
        return list(self.adj_list.keys())
    
    def get_edges(self):
        edges = []
        for v1 in self.adj_list:
            for v2, weight in self.adj_list[v1].items():
                if (v2, v1, weight) not in edges:  # Evitar duplicados en no dirigido
                    edges.append((v1, v2, weight))
        return edges
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result
    
    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in reversed(list(self.adj_list[vertex].keys())):  # Para orden consistente
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result
    
    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.adj_list}
        distances[start] = 0
        heap = [(0, start)]
        visited = set()
        
        while heap:
            current_dist, current_vertex = heapq.heappop(heap)
            if current_vertex in visited:
                continue
            visited.add(current_vertex)
            
            for neighbor, weight in self.adj_list[current_vertex].items():
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
        
        return distances
    
    def __str__(self):
        return str(dict(self.adj_list))

# Ejemplo de uso
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 8)
print("Vértices:", g.get_vertices())  # ['A', 'B', 'C', 'D']
print("Aristas:", g.get_edges())  # [('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1), ('B', 'D', 5), ('C', 'D', 8)]
print("BFS desde A:", g.bfs('A'))  # ['A', 'B', 'C', 'D']
print("DFS desde A:", g.dfs('A'))  # ['A', 'C', 'D', 'B']
print("Dijkstra desde A:", g.dijkstra('A'))  # {'A': 0, 'B': 3, 'C': 2, 'D': 8}