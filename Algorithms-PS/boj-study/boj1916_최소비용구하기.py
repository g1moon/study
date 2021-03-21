# https://www.acmicpc.net/problem/1309
# boj 1309 S1 동물원 
# <메모리 : 127304, 시간 : 136 >

'''
- 가장 유명한 사람 = 각 사람의 (2-친구) 
- a가 b의 2-친구려면 -> (a-b가 친구) or (a와 친구 and b와 친구인 c)
'''
import sys
import heapq
input = sys.stdin.readline

#input
n = int(input()) #도시의 개수 
m = int(input()) #버스의 개수 
mat = [ [] for _ in range(n+1)]

for _ in range(m):
    s, d, c = map(int, input().split())
    mat[s].append((c, d))
    
start, dest = map(int, input().split())


dist = [float('inf') for _ in range(n+1)]
dist[start] = 0
queue = [(0, start)]

while queue:
    popped = heapq.heappop(queue)
    cur_cost, cur = popped[0], popped[1]
    
    for nxt_cost, nxt in mat[cur]:
        if dist[nxt] > cur_cost + nxt_cost:
            dist[nxt] = cur_cost + nxt_cost
            heapq.heappush(queue, (dist[nxt], nxt))
            
print(dist[dest])