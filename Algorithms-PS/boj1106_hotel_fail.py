# https://www.acmicpc.net/problem/11060
# boj 11060 S2 점프 점프
# <메모리 : 29380, 시간 : 76 >

'''
- j가 n보다 작을 때 -> dp 테이블을 이용해 확인
    -> dp[j] = min(dp[j], dp[i]+1)
'''

import sys
input = sys.stdin.readline

#12명을 늘리기위해 2개의 도시
c, n = map(int, input().split()) # 적어도 c명 늘리기 위해, n <= 20 -> intenger
cost_lst, pot_lst = [], []
lst = []
for _ in range(n):
    #a:홍보 비용  b: 그 비용으로 얻을 수 있는 고객 
    a, b = map(int, input().split())
    cost_lst.append(a)
    pot_lst.append(b)
    lst.append((a,b))

lst.sort(reverse = True)
ans = 0    
idx = 0 

while True:
    cost, pot = lst[idx]
        
    if c - pot < 0:
        idx += 1
        continue

    elif c - pot == 0:
        print(ans + cost )
        break 
    
    #else 
    c -= pot 
    ans += cost

    
    
    
    
