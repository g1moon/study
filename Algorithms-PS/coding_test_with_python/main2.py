'''
- (1~N) 번까지의 도시와
- (M개의 도시) 단방향 도로
- (도시X로 출발)해서 -> 도달할 할 수 있는 모든 도시중 -> 
    -> (최단거리가 정확히 K인) 모든 도시들의 번호를 출력 
    
'''
N, M, K, X = map(int, input().split())
print(N, M, K, X)
dic = {}
for _ in range(M):
    f, t = map(int, input().split())
    try: dic[f].append(t)
    except: dic[f] = [t]
    
res = [0] *  300,000
def dfs(idx):
    global res 
    try: dfs[res[idx-1]]
    except:
        print(res)
        return
        
    if idx == 0:
        for start in dic.keys():
            res[idx] = start
            dfs(idx+1)
    else:
        for i in dic[res[idx-1]]:
            res[idx] = i
            dfs(idx+1)
            
dfs(0)
            
            