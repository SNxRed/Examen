import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0  # Para manejar empates en prioridad
    
    def insert(self, item, priority):
        heapq.heappush(self.heap, (priority, self.count, item))
        self.count += 1
    
    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[-1]
        return None
    
    def peek(self):
        if self.heap:
            return self.heap[0][-1]
        return None
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def change_priority(self, item, new_priority):
        for i, (p, c, it) in enumerate(self.heap):
            if it == item:
                self.heap[i] = (new_priority, c, it)
                heapq.heapify(self.heap)
                return
        raise ValueError("Item no encontrado")
    
    def __str__(self):
        return str([(p, i) for p, _, i in sorted(self.heap)])

# Ejemplo de uso
pq = PriorityQueue()
pq.insert("tarea urgente", 1)
pq.insert("tarea normal", 3)
pq.insert("tarea importante", 2)
print(pq)  # [(1, 'tarea urgente'), (2, 'tarea importante'), (3, 'tarea normal')]
print("Pop:", pq.pop())  # tarea urgente
pq.change_priority("tarea normal", 1)
print("Después de cambiar prioridad:", pq)  # [(1, 'tarea normal'), (2, 'tarea importante')]