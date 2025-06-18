class Map:
    def __init__(self):
        self.items = {}
    
    def put(self, key, value):
        self.items[key] = value
    
    def get(self, key):
        return self.items.get(key, None)
    
    def remove(self, key):
        if key in self.items:
            del self.items[key]
    
    def keys(self):
        return list(self.items.keys())
    
    def values(self):
        return list(self.items.values())
    
    def items(self):
        return list(self.items.items())
    
    def __str__(self):
        return str(self.items)

# Ejemplo de uso
m = Map()
m.put("a", 1)
m.put("b", 2)
print(m.get("a"))  # 1
print("Claves:", m.keys())  # ['a', 'b']
m.remove("a")
print(m)  # {'b': 2}