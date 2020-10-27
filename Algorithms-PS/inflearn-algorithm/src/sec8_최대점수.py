'''
- (N개의 문제를)
- (얻는 점수, 푸는데 걸리는 시간)
- (제한시간 M안에 N개의 문제중 최대점수)

- 1번문제부터 ~ 마지막 문젞₩
'''
#input()
N, M = map(int, input().split())
lst = [ tuple(map(int, input().split())) for _ in range(N)]
dy = [ [0] * (M+1) for _ in range(N+1)]

for x in range(N): #0번문제까지만 고려 ~ N(5)번쨰 문제까지 고려
    pv, pt = lst[x][0], lst[x][1]
    for y in range(pt, M+1 ): #해당 인덱스 시간 ~ M 
        dy[x][y] = max(dy[x][y], dy[x-1][y-pt] + pv) #이전행 참조하게 !
    
    #다음 행으로 넘어갈 떄 복사해주기
    if x != N:   
        for col in range(len(dy[0])):
            dy[x+1][col] = dy[x][col]

print(max(dy[-1]))
