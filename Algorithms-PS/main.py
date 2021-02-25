# https://www.acmicpc.net/problem/2225
# boj 2225 G5 합분해 
# <메모리 : 123320, 시간 : 124 >
#예제는 다 맞는데 어느 부분에서 틀린건지 모르겠네요... 
'''
- 캠핑장은 연속하는 20일중 10일만 사용 가능
- P일중 L일동안만 사용 -> V일짜리 휴가
'''

def solution(l,p,v):
    
    res = (v//p) * l
    
    if l < v%p:
        res += l
    else:
        res += v%p    
    return res
    
    
#--------------
import sys 
input = sys.stdin.readline

t = 1
while True:
    l,p,v = map(int, input().split())
    if l == 0 and p == 0 and v ==0:
        break 
    print(f'Case {t}: {solution(l,p,v)}')
    t+=1 

