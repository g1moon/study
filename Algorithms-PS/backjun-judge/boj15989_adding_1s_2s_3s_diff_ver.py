#boj 15989
#1,2,3 더하기 4
import sys
In = sys.stdin.readline
t = int(In())
l = 0
lst = []
for _ in range(t):
    a = int(In())
    if a > l: l = a
    lst.append(a)
    
d = [0] * (l+1)
d[0] = 1
#-------------------------

for i in range(l+1):
    #1부터 채우기
    if i - 1 >= 0:
        d[i] += d[i-1]
        
for i in range(l+1):
    #1부터 채우기
    if i - 2 >= 0:
        d[i] += d[i-2]
        
for i in range(l+1):
    #1부터 채우기
    if i - 3 >= 0:
        d[i] += d[i-3]
        
#_---------------------
for n in lst:
    print(d[n])
    

