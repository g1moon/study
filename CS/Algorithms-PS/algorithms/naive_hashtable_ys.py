class Naive_HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [[] for _ in range(size)]
        self.data = [[] for _ in range(size)]

    def hash_func(self, key):
        return key % self.size
    
    def put(self, key, data):
        val = self.hash_func(key)
        self.slots[val].append(key)
        self.data[val].append(data)
        
    def get(self, key):
        val = self.hash_func(key)
        ret = self.data[val]

        if len(self.data[val]) > 1:
            idx = self.slots[val].index(key)
            return self.data[val][idx]

        if not ret:
            print('No corresponding key')
            return None
        return ret 

# DO NOT modify this code
naive = Naive_HashTable(5)

naive.put(5, 'a')
naive.put(2, 'b')
naive.put(7, 'c')

print(naive.get(2))
print(naive.get(7))
print(naive.get(3))