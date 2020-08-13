
dic = {'A':[4,3,2,1], 'B':[], 'C':[]}
def towerofHanoi(n, source, dest, aux):
    if (n==1):

        # print('move disk 1 from ' + source + ' to  ' + dest)
        dic[dest].append(dic[source].pop())
        print(dic)
    else:
        
        towerofHanoi(n-1, source, aux, dest)
        # dic[dest].append(dic[source].pop())
        # print(dic)
        # print('move disk ' + str(n) + ' from' + source + ' to' + dest)
        dic[dest].append(dic[source].pop())
        print(dic)
        towerofHanoi(n-1, aux, dest, source)
        
print('=======hanoi tower game =========')
print(dic)
towerofHanoi(4, 'A', 'C', 'B')