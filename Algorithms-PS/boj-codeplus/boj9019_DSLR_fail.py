#boj 9019
#DSLR
from collections import deque
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    fro = [-1] * 10001
    ck = [False] * 10001
    dist = [[]  for _ in range(10001)]
    
    q = deque()
    q.append(a)
    # dist[a] = 0
    ck[a] = True
    
    while q:
        cur = q.popleft()
        ck[cur] = True
        
        #1
        new = 2 * cur 
        if new > 9999:
            new = new % 10000
        new = str(new)
        if len(new) != 4:
            while len(new) < 4:
                new = '0' + new 
        new = int(new)
        if ck[new] == False:
            ck[new] = True
            dist[new] = dist[cur] + ['D']
            q.append(new)
        
        
        
        #2
        if cur  == 0 :
            new = 9999
        else:
            new = cur - 1

        new = str(new)
        if len(new) != 4:
            while len(new) < 4:
                new = '0' + new 
        new = int(new)
        if ck[new] == False:
            ck[new] = True
            # dist[new] = dist[cur] + 1
            dist[new] = dist[cur] + ['S']
            q.append(new)
        
        #3
        s = str(cur)
        s1 = s[1:]
        s2 = s[0]
        s = s1 + s2
        new = str(s)
        if len(new) != 4:
            while len(new) < 4:
                new = '0' + new 
        new = int(new)
        if ck[new] == False:
            ck[new] = True
            dist[new] = dist[cur] + ['L']
            q.append(new)
        
        #4
        s = str(cur)
        s1 = s[1:]
        s2 = s[0]
        s = s2 + s1
        new = str(new)
        if len(new) != 4:
            while len(new) < 4:
                new = '0' + new 
        new = int(new)
        if ck[new] == False:
            ck[new] = True
            dist[new] = dist[cur] + ['R']
            q.append(new)
        
    res = map(str, dist[b])
    res = ''.join(res)
    print(res)