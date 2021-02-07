# https://www.acmicpc.net/problem/1260
# boj 1260 S2 (DFS와 BFS)
# <메모리 : 124400 / 시간: 284>
'''
- 같은 조건이면 -> 더 낮은 정점으로 간다
    -> dic에서 오름차순 정렬해줌
'''
import sys
input = sys.stdin.readline
dic = {} 
N, M, V = map(int, input().split()) #정점의개수, 간선의개수, 탐색시작정점번호

#dic
dic = {i:[] for i in range(1, N+1)}
for _ in range(M):
  a,b = map(int,input().split())
  dic[a].append(b)
  dic[b].append(a)
for k,v in dic.items():
      v.sort()

#
visited_dfs = []
visited_bfs = []

#dfs
def dfs(cur):
      visited_dfs.append(cur)
      for i in dic[cur]:
            if i in visited_dfs:
                  continue 
            dfs(i)

#bfs
q = [V]
while q:
      cur = q.pop(0)
      if cur not in visited_bfs:
        visited_bfs.append(cur)
      for i in dic[cur]:
            if i not in visited_bfs: #방문한곳이아니라면?
                  q.append(i)



print(' '.join(list(map(str,visited_dfs))))                  
print(' '.join(list(map(str,visited_bfs))))

    

