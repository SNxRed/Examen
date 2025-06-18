class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def get(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
    
    def contains(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for k, _ in bucket:
            if k == key:
                return True
        return False
    
    def resize(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [[] for _ in range(new_size)]
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)
    
    def __str__(self):
        return str(self.table)

# Ejemplo de uso
ht = HashTable()
ht.insert("clave1", "valor1")
ht.insert("clave2", "valor2")
print(ht.get("clave1"))  # valor1
print("Contiene 'clave3'?", ht.contains("clave3"))  # False
ht.remove("clave1")
print(ht)  # [[], [], [('clave2', 'valor2')], [], [], [], [], [], [], []]