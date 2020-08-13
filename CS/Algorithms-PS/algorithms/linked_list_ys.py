# DO NOT change this code
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        
    def setdata(self, _data):
        self.__data = _data
        
    def setnext(self, _next):
        self.__next = _next
        
    def getdata(self):
        return self.__data
    
    def getnext(self):
        return self.__next
############################

    class LinkedList:
        def __init__(self):
        self.__head = None
        self.length = 0
        
    def __len__(self):
        return self.length
        
    def insert(self, item):
        temp = Node(item)
        temp.setnext(self.__head)
        self.__head = temp
        self.length += 1
        
    def search(self, x):
        ret = []
        idx = 0
        start = self.__head
        for _ in range(self.length):
            if start.getdata() == x:
                ret.append(idx)
            start = start.getnext()
            idx += 1
        return ret
    
    def search_diff(self, interval):
        ret = []
        start = self.__head
        idx =0
        for _ in range(self.length-1):
            
            diff =  start.getnext().getdata() - start.getdata()
            if diff == -1:
                ret.append(idx)
            idx += 1
            start = start.getnext()
        return ret

        
        
    def __le__(self, other):
        ret = False
        s_start = self.__head
        o_start = other.__head
        s = []
        o = []
        for _ in range(self.length):
            s.append(s_start.getdata())
            s_start = s_start.getnext()

        for _ in range(other.length):
            o.append(o_start.getdata())
            o_start = o_start.getnext()
        
        bln_contain = True
        for i in s:
            if i not in o:
                bln_contain = False

        if len(s) < len(o) and bln_contain:
            ret = True
        
        return ret
    
    
    # DO NOT modify this code
list1 = LinkedList()
list2 = LinkedList()

list1.insert(3)
list1.insert(2)
list1.insert(5)
list1.insert(3)

list2.insert(1)
list2.insert(2)
list2.insert(5)
list2.insert(3)
list2.insert(4)

print(list1.search(3))
print(list2.search_diff(-1))
print(list1 <= list2)
