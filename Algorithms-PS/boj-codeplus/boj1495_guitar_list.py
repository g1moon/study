#boj 1495
#music_list
import copy
'''
- v[i] = i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨 
- 현재볼륨 p -> i번째 곡은 p+v[i], p-v[i]
- 0 <= P <=M

'''
import sys
#input
n, s, m = map(int, input().split()) #곡의개수, 시작볼륨, m 
v = list(map(int, input().split()))
d = [ [False] * (m+1) for _ in range(n)]

a, b = s+v[0], s-v[0]
if 0 <= a <= m: d[0][a] = True
if 0 <= b <= m: d[0][b] = True


for row in range(n-1): #0~n-1
    for col in range(m+1):
        if d[row][col] == True:
            a, b = col + v[row+1], col - v[row+1]
            
            if 0 <= a <= m: d[row+1][a] = True 
            if 0 <= b <= m: d[row+1][b] = True 



for i in range(len(d[-1])-1, 0, -1):
    if d[-1][i] == True:
        print(i)
        break 
else:
    print(-1)
        
            
for i in range(10, 0-1, -1):
    print(i)
        
  