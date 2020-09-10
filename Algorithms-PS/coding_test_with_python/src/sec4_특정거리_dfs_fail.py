'''
- (1~N) 번까지의 도시와
- (M개의 도시) 단방향 도로
- (도시X로 출발)해서 -> 도달할 할 수 있는 모든 도시중 -> 
    -> (최단거리가 정확히 K인) 모든 도시들의 번호를 출력 
    
'''
N, M, K, X = map(int, input().split())
# print(N, M, K, X)
dic = {}
for i in range(1, N+1):
    dic[i] = []

for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
# print(dic)
    
    
dist_lst = [1e9] * (N+1)

def dfs(dist, cur):
    global dist_lst
    if len(dic[cur]) == 0:
        dist_lst[cur] = min(dist_lst[cur], dist)
        return 
    
    for i in dic[cur]:
        dfs(dist+1, i)
            
dfs(0,X)

print_neg = True
print(dist_lst)
for i in range(len(dist_lst)):
    if dist_lst[i] == K:
        print(i)    
        print_neg = False

if print_neg:
    print(-1)
            