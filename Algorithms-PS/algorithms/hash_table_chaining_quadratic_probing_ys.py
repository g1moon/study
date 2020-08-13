class HashTable:
    def __init__(self, size, max_chain):
        self.size = size #
        self.max_chain = max_chain
        self.slots = [[] for _ in range(size)]
        self.data = [[] for _ in range(size)]
        
    def __len__(self):
        # Code here #
        ret = 0
        for i in range(len(self.slots)):
            ret += len(self.slots[i])
        return ret
        
    def hash_func(self, key):
        return key % self.size
    
    def rehash_func(self, key, cnt):
        # Code here #
        return self.hash_func(key) + (cnt**2)
        
    def put(self, key, data):
        # Code here #
        call_num = 0
        val = self.hash_func(key)
        if len(self.slots[val]) == 0:
            self.slots[val].append(key)
            self.data[val].append(data)
        else:
            #있는데 key가 있으면-> replace
            if key in self.slots[val]:
                idx = self.slots[val].index(key)
                self.data[val][idx] = data

            #해당 슬롯이 max_chain임 
            
            elif len(self.slots[val]) == self.max_chain:
                isFull = False
                cnt = 1
                
                while True:
                    nxt_slot = self.rehash_func(key,cnt)
                    call_num += 1
                    #맥스체인보다 적게 들어있거나 맥스체인만큼 들어있는데 
                    #이 안에 같은 키가 있다면? -> replace
                    if len(self.slots[nxt_slot]) <= self.max_chain:
                        if key in self.slots[nxt_slot]:
                            same_key_idx = self.slots[nxt_slot].index(key)
                            self.data[nxt_slot][same_key_idx] = data
                            break
                    #   
                        elif len(self.slots[nxt_slot]) < self.max_chain:
                            self.slots[nxt_slot].append(key)
                            self.data[nxt_slot].append(data)
                            break
                    else:
                        cnt += 1

                    isFull = True
                    for i in range(len(self.slots)):
                        if len(self.slots[i]) != self.max_chain:
                            isFull = False
                            break
                    
                    if isFull:
                        print('error: full ')
                        break          
                #다른곳 찾아야함
            #key가있지도 않고, 해당 슬롯이 max_chain도 아니면 걍 넣어 
            else:
                self.slots[val].append(key)
                self.data[val].append(data)
            return call_num

        
    def get(self, key):
        # Code here #
        start_slot = self.hash_func(key)
        data = None
        stop = False
        found = False
        pos = start_slot

        cnt = 1
        while not stop and not found and len(self.slots[pos]) !=0:
            if key in self.slots[pos]:
                found = True
                data = self.data[pos][self.slots[pos].index(key)]
            else:
                pos = self.rehash_func(key+cnt, 0)
                cnt+=1
                if pos == start_slot:
                    stop = True

        if data == None:
            print('There is no corresponding key.')
            return
        return data
            
    def remove(self, data):
        key_= 0 
        start_slot = self.hash_func(0)
        pos = start_slot
        ck = True
        while True :
            #있으면 찾아서 삭제
            if data in self.data[pos]:
                while data  in self.data[pos]:
                    del_idx = self.data[pos].index(data)
                    self.data[pos].pop(del_idx)
                    self.slots[pos].pop(del_idx)
                    ck = False

            #없으면 넘어가고 다 돌면 중단
            key_ += 1
            pos = self.hash_func(key_)
            
            if pos == start_slot:
                break
        if ck:
            print('There is no corresponding data.')

    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)
        
        
        # This code is for validation; DO NOT change this code
table = HashTable(size = 7, max_chain = 2)
key = list(range(7))
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for i, j in zip(key, data):
    table[i] = j

print(table[4])
key = list(range(7, 14))
for i, j in zip(key, data):
    table[i] = j
table.remove('c')
table.remove('f')
table.put(1, 'h')
table.put(13, 'i')
print(table.data)
print('-' * 40)
table.remove('d')
print(table.put(15, 'c'))
print(table.slots)
print('-' * 40)
table.get(21) # Error message
table.remove('x') # Error message
print('-' * 40)
print(len(table))
table[5] = 'a'
table.remove('a')
print(table[15])