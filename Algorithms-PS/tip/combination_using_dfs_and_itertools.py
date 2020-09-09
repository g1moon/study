
lst =[0,1,2,3,4,5]
M = 4
#dfs로 조합-------------------------------
res = [0] * M
def dfs(idx):
    global res
    if idx == M:
        print(res)
        return 

    if idx == 0:      
        for i in range(0, len(lst)):
            res[idx] = i
            dfs(idx+1)
    else:
        for i in range(res[idx-1]+1 ,len(lst)): #이미들어간거
            res[idx] = i
            dfs(idx+1)
            
#
dfs(0)
#라이브러리------------------------------------------
from itertools import combinations
print(len(list(combinations(lst, M))))
print(list(combinations(lst, M)))

