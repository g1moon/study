# https://www.acmicpc.net/problem/2644
# boj 2644 촌수계산(S2)
# <메모리 : 121220, 시간 : 104> 
'''
- 관계를 나타내는 딕셔너리를 만든다
    - input이 2, 3이면 dic[2].append(3), dic[3].append(2)
- 출발점에서 도착점까지 dfs를 통해 탐색         
- dfs(현재 지점, 지금까지의 촌수)
'''
#dfs
def dfs(num, res):
    global ans, changed
    if num == t:
        changed = True
        ans = res
        return     
    for i in dic[num]:
        if ck[i] == False:
            ck[i] = True
            dfs(i, res+1)
            ck[i] = False

#         
n = int(input()) #전체사람의 수 
f, t = map(int, input().split())
m = int(input())
ck = [False] * (n+1)
ans = 0
changed = False

#딕셔너리 만들기
dic = {}
for _ in range(m):
    x, y = map(int,input().split())
    if x in dic.keys():
        dic[x].append(y)
    else:
        dic[x] = [y]
        
    if y in dic.keys():
        dic[y].append(x)
    else:
        dic[y] = [x]

#dfs
dfs(f,0)         

#print
if changed:
    print(ans)
else:
    print(-1)  



       

    
    