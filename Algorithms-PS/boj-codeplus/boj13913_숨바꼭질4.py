#boj 13913
#숨바꼭질4 

from collections import deque
import sys
sys.setrecursionlimit(200000)
ck = [False] * 100001
dist = [-1] * 100001
fro = [-1] * 100001

n,m = map(int, input().split())
queue = deque()
queue.append(n)
dist[n]= 0
ck[n] = True

while queue:
    now = queue.popleft()
    
    if 0<= now+1 <=100000 and not ck[now+1]:
        queue.append(now+1)
        dist[now+1] = dist[now] + 1
        ck[now+1] = True
        fro[now+1] = now
        
    if 0<= now-1 <=100000 and not ck[now-1]:
        queue.append(now-1)
        dist[now-1] = dist[now] + 1
        ck[now-1] = True
        fro[now-1] = now

    if 0<= now*2 <=100000 and not ck[now*2]:
        queue.append(now*2)
        dist[now*2] = dist[now] + 1
        ck[now*2] = True
        fro[now*2] = now
        
print(dist[m])

def go(n, m):
    if n != m:
        go(n, fro[m])
    print(m, end=' ')
go(n, m)
