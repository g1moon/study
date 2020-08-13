#16956번 늑대와 양
#https://www.acmicpc.net/problem/16956

R,C = map(int, input().split())
M = [list(input()) for i in range(R)]

dr, dc = [0,1,0,-1], [1,0,-1,0]

ck = False

for r in range(R):
    for c in range(C):
        if M[r][c] == 'W':
            for w in range(4):
                rr, cc = r + dr[w], c + dc[w]
                if rr < 0 or rr == R or cc <0 or cc ==C:
                    continue 
                
                if M[rr][cc] == 'S':
                    ck = True
          
if ck:
    print(0)
else:
    print(1)
    for r in range(R):
        for c in range(C):
            if M[r][c] == '.':
                M[r][c] = 'D'

    for i in M:
        print(''.join(i))