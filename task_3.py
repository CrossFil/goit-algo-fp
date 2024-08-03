import heapq

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))
        
        # Якщо граф не орієнтований, додаємо зворотнє ребро
        if to_vertex not in self.edges:
            self.edges[to_vertex] = []
        self.edges[to_vertex].append((from_vertex, weight))

def dijkstra(graph, start_vertex):

    distances = {vertex: float('infinity') for vertex in graph.edges}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань більша за вже збережену, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад використання
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    start_vertex = 'A'
    distances = dijkstra(g, start_vertex)
    for vertex, distance in distances.items():
        print(f"Відстань від вершини {start_vertex} до вершини {vertex} дорівнює {distance}")
