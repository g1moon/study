#if opening -> push
#if closing -> pop 
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.insert(0, item)
        
    def pop(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    


def par_checker(symbol_str):
    s = Stack()
    balanced = True
    idx = 0
    
    while idx < len(symbol_str) and balanced:
        symbol = symbol_str[idx]
        if symbol =='(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
                
        idx = idx + 1
        
        if balanced and s.is_empty():
            return True
        else:
            return False
        
print(par_checker('()()'))