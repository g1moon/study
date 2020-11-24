#boj 11053
#kriii_board
import sys
n = int(sys.stdin.readline())
if n < 7:
    print(n)
else:
    d = [0] * (n+1)
    for i in range(1,6+1):
        d[i] = i 
    #-----------------------
    for i in range(7, n+1):
        d[i] = d[i-1] + 1
        for v in range(1, i-2+1): #range(1, i-3+1)이 더 맞음 왜냐하면 1이 적힌 상태에서부터 복사가 효과있음
            item = d[i-(2+v)] * (v+1)
            if item > d[i]:
                d[i] = item 
    print(d[n])