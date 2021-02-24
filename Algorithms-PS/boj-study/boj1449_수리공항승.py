# https://www.acmicpc.net/problem/9465
# boj 9465 S2 스티커 
# <메모리 : 185980, 시간 : 340 >
#예제는 다 맞는데 어느 부분에서 틀린건지 모르겠네요... 
'''
-가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다
- (길이가 L인 테이프 무한개)
- 좌우 0.5 간격을 줘야 -> 물이 다시 안 샌다.
'''
from collections import deque

def solution(n, l, lst):
    cnt = 1
    leaky_lst = []
    for i in lst:
        leaky_lst.append(i)
        leaky_lst.append(i-0.5)
        leaky_lst.append(i+0.5)
    leaky_lst.sort()
    base = leaky_lst[0] + l
    for i in range(1,len(leaky_lst)):
        if base >= leaky_lst[i]:
            continue 
        else:
            base = leaky_lst[i] + l
            cnt += 1
            
    return cnt

 
        
    
    
#--------------
import sys 
input = sys.stdin.readline
n, l = map(int, input().split())
lst = list(map(int, input().split()))
print(solution(n,l,lst))