# https://www.acmicpc.net/problem/1449
# boj 1449 S3 수리공 항승
# <메모리 : 123560, 시간 : 132 >
'''
- 막아야하는 모든 부분을 리스트에 넣고 (누수점-0.5, 누수점, 누수점+0.5)
- 정렬시켜서 앞에서부터 막으면서 카운트
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
