class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    
    def remove(self, data):
        if not self.head:
            return
        
        current = self.head
        prev = None
        
        # Caso especial: eliminar el head
        if current.data == data:
            if current.next == self.head:  # Único nodo
                self.head = None
            else:
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return
        
        # Buscar nodo a eliminar
        while current.next != self.head:
            prev = current
            current = current.next
            if current.data == data:
                prev.next = current.next
                return
    
    def traverse(self):
        if not self.head:
            return []
        elements = [self.head.data]
        current = self.head.next
        while current != self.head:
            elements.append(current.data)
            current = current.next
        return elements
    
    def josephus_problem(self, k):
        if not self.head:
            return None
        
        current = self.head
        while self.size() > 1:
            # Mover k-1 pasos
            for _ in range(k-1):
                current = current.next
            # Eliminar el siguiente nodo
            print(f"Eliminando {current.next.data}")
            self.remove(current.next.data)
            current = current.next
        return self.head.data
    
    def size(self):
        if not self.head:
            return 0
        count = 1
        current = self.head.next
        while current != self.head:
            count += 1
            current = current.next
        return count

# Ejemplo de uso
cl = CircularLinkedList()
for i in range(1, 6):
    cl.append(i)
print("Lista circular:", cl.traverse())  # [1, 2, 3, 4, 5]
cl.remove(3)
print("Después de eliminar 3:", cl.traverse())  # [1, 2, 4, 5]

# Problema de Josephus
cl_josephus = CircularLinkedList()
for i in range(1, 6):
    cl_josephus.append(i)
print("Superviviente:", cl_josephus.josephus_problem(2))  # Elimina 2, 4, 1, 5, sobrevive 3