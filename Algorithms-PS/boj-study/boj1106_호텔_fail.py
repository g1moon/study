# https://www.acmicpc.net/problem/1106
# boj 1106 S2 실패 
# <메모리 : 실패, 시간 : 실패 >

'''
- dfs로 각각의 경우를 모두 고려해 해결하려했으나 시간초과...
- dp로 어떻게 코드를 수정해야할지 고민해야겠다.
'''

import sys
input = sys.stdin.readline

#12명을 늘리기위해 2개의 도시
c, n = map(int, input().split()) # 적어도 c명 늘리기 위해, n <= 20 -> intenger
lst = []
for _ in range(n):
    #a:홍보 비용  b: 그 비용으로 얻을 수 있는 고객 
    a, b = map(int, input().split())
    lst.append((a,b))

def dfs(remain, cost):
    global res
    if remain == 0:
        if cost < res:
            res = cost 
        return 
    
    for i in range(n):
        c, p = lst[i][0], lst[i][1]
        if remain - p >= 0:
            dfs(remain-p, cost + c)
        else:
            return 

res = float('inf')            
dfs(c, 0)
print(res)

