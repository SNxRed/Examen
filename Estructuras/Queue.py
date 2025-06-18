from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(list(self.items))

# Ejemplo de uso
q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print(q)  # ['a', 'b', 'c']
print("Frente:", q.peek())  # a
print("Dequeue:", q.dequeue())  # a
print(q)  # ['b', 'c']