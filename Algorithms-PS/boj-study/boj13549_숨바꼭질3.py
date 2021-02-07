# https://www.acmicpc.net/problem/13549
# boj 13549 G5 숨바꼭질3 
# 시간초과 
'''
- 
'''
from collections import deque
a, b = map(int, input().split())
q = deque()
q.append(a)
ck = [float('inf')]*1000001
ck[a] = 0  #a까지의 최소거리는 0 
while q:
    x = q.popleft()
    cnt = ck[x] 

    if 0 <= x+1 <= 100000:
        if ck[x+1] > cnt+1: 
            ck[x+1] = cnt+1
            q.append(x+1)
        
    if 0 <= x-1 <= 100000:
        if ck[x-1] > cnt+1: 
            ck[x-1] = cnt+1
            q.append(x-1)
        
    if 0 <= 2*x <= 100000:
        if ck[2*x] > cnt: 
            ck[2*x] = cnt
            q.append(2*x)
    
print(ck[b])
    
    
'''
- 수빈이는 점N, 동생은 점K
- 수빈이는 걷기: 1초후 -> (X-1 or X+1)
        순가이동: 0초후 -> (2*X)
- 수빈 동생 위치있을떄 -> 수빈이가 동생을 찾을 수 있는 가장 빠른 시간   
'''
    
    
    
    
    
    
    
    