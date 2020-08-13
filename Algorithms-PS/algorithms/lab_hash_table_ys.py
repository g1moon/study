class HashTable:
    def __intit__(self):
        self.size = 11
        self.slots = [None] * self.size #key를저장하는 곳
        self.data = [None] * self.size #데이터저장하는곳
        
    def hash_function(self, key, size):
        return key % size
    #key에다가 더하는게 아니라 이 키로 만든 값에 1을 더해서 하는 것
    def rehash(self, old_hash, size):
        return (old_hash+1) % size
    
    def put(self,key,data):
        #hash function은 key와 size를 받는다 
        hash_value = self.hash_function(key, len(self.slots))
        
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
            
        else:
            #비어있지 않은경우 
            #1. key값이 같다 -> Replace
            #2. 해당 슬롯이 차있다 -> 다른 곳을 찾음 rehash로
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                #해쉬값임 next_slot은
                next_slot = self.rehash(hash_value, len(self.slots))
                #None이거나 , key가 같을때까지 아마 or일거임
                while (self.slots[next_slot] != None) or  self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                    
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                    
                else:
                    self.data[next_slot]
                    
                    
    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        
        data = None
        stop = False
        found = False
        pos = start_slot
        
        #키가 None이거나 
        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos, len(self.slots))
                #만약 이게 처음 스타트 슬롯이야 ~ 그럼 한바퀴 다 돈거임 stop을 트루로
                if pos == start_slot:
                    stop = True
        return data      
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data) 

h = HashTable()
h[54] = 'cat'