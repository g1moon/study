# https://www.acmicpc.net/problem/132
# boj 1325 S2 효율적인 해킹
# <메모리 : 224304, 시간 11876>
'''
- visited 리스트에 append하는 식으로 방문을 기록하면 -> 시간 초과 
- queue에 넣고 -> visited 체크 
- 딕셔너리로 관계를 나타내기보다 리스트로 하면 코드가 더 깔끔해짐
'''
import sys
from collections import deque
input = sys.stdin.readline
#----------------------------------

n, m = map(int, input().split()) #컴퓨터 개수, m줄의 신뢰 관계
adj = [ [] for _ in range(n+11876) ]
for _ in range(m):
    a, b = map(int, input().split())
    adj[b].append(a)

#----------------------------------
def bfs(start):
    q = deque()
    visited = [False] * (n+1)
    
    q.append(start)
    visited[start] = True
    
    cnt = 1
    
    while q:
        now = q.popleft()
                
        for nxt in adj[now]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                cnt += 1    
    return cnt
    
#-----------------------------------
max_cnt = 1
ans = []
for start in range(1, n+1):
    res = bfs(start)
    
    if res > max_cnt:
        max_cnt = res
        ans = [start]
    
    elif res == max_cnt:
        ans.append(start)
        
#----------------------------------
print(' '.join(map(str,ans)))
   
    
    
        
        
    

    



