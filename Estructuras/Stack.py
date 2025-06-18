class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

# Ejemplo de uso
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)  # [1, 2, 3]
print("Tope:", s.peek())  # 3
print("Pop:", s.pop())  # 3
print(s)  # [1, 2]