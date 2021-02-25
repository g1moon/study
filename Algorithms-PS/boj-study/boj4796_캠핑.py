# https://www.acmicpc.net/problem/4796
# boj 4796 S5 캠핑
# <메모리 : 123320, 시간 : 124 >
'''
- 남은 날짜 최대한으로 이용
    -> 8일중 5일 사용 가능한데 -> 4일 남았으면 -> 4일 전부 이용 가능
    -> 근데 만약            -> 7일 남았으면 -> 7일 전부 사용 불가능(5일만 사용가능)
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

