# https://www.acmicpc.net/problem/11725
# boj 11725 S1
# 실패, 예제는 모두 맞는데 런타임에러가 나네요.. 
'''
- 그래프 만들고 루트노트(1)부터 dfs탐색
    -> 자식 노드에 접근해서 dfs호출하는데,
        방문한 곳이 아니어야 함 
'''
n = int(input())
gr = [ [] for i in range(n+1)]
res = [0] * (n+1)

for _ in range(n-1):
    i, j = map(int ,input().split())
    gr[i].append(j)
    gr[j].append(i)
    
    
def dfs(idx):
    for i in gr[idx]:
        if res[i] == 0:
            res[i] = idx
            dfs(i)

#res 출력       
dfs(1)
for i in range(2, len(res)):
    print(res[i])
    




        
        