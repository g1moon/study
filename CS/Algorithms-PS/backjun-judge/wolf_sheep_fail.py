#16956번 늑대와 양
#https://www.acmicpc.net/problem/16956

#크기가 r*c
#행,열
R,C = map(int, input().split())
farm = [ list(input())  for i in range(R)]

#동남서북
dr = [0,1,0,-1]
dc = [1,0,-1,0]

ck =True
for r in range(R):
    for c in range(C):
        if farm[r][c] == 'S':
            for i in range(4):
                try:
                    if farm[r+dr[i]][c+dc[i]] == 'W':
                        ck = False
                        break
                except: pass
for r in range(R):
    for c in range(C):
        try:
            for i in range(4):                  
                if farm[r+dr[i]][c+dc[i]] == '.':
                    farm[r+dr[i]][c+dc[i]] = 'D'
        except:pass


if ck:
    print(1)
    for i in farm:
        print(''.join(i))
else:
    print(0)

