# https://www.acmicpc.net/problem/1916
# boj 1916 G5 최소비용 구하기 
# <메모리 : 128756, 시간 : 224 >

'''
- 우선순위 큐를 활용한 다익스트라로 해결 
- 
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

#dij 
dist = [float('inf') for _ in range(n+1)]
dist[start] = 0
queue = [(0, start)]

while queue:
    popped = heapq.heappop(queue)
    cur_cost, cur = popped[0], popped[1]
    
    #현재 노드에서 갈 수 있는 다음 노드를 살피고 
    #다음으로 가는게 -> 이득이면 업데이트하고 큐에 추가 
    for nxt_cost, nxt in mat[cur]:
        new_cost = cur_cost + nxt_cost
        
        if dist[nxt] > new_cost: #기존 > 현재에서 다음으로 
            dist[nxt] = new_cost
            heapq.heappush(queue, (dist[nxt], nxt))
            
print(dist[dest])