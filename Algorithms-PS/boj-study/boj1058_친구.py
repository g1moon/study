# https://www.acmicpc.net/problem/1058
# boj 1058 S1 친구 
# <메모리 : 126060, 시간 : 168 >

'''
- 중간점을 고려한 플로이드 와샬로 해결 
    - 조건 1 : 서로 친구 
    - 조건 2 : 친구의 친구끼리 연결된 경우 
    -> ck[i][j] = True

'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
mat = [list(input().strip()) for _ in range(n)]
ck = [ [0]*n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                if mat[i][j] == 'Y' or (mat[i][k] =='Y' and mat[k][j] == 'Y'):
                    ck[i][j] = True


res = 0
for i in ck:
    res = max(res, sum(i))
    
print(res)