'''
- 7 * 7
- 동서남북 방향으로 5자길이가 회문인지
'''

mat = [list(map(int, input().split())) for _ in range(7)]
#기준을 정하는데  -> 1. 가로로 보는 경우 (y가 2보다 크면 안됨(0,1,2))
            #->2. 세로로 보는 경우 (x가 2보다 크면 안됨(0,1,2))
            
# 그래서 기준을 잡고 
cnt = 0
#가로로 보기
for x in range(7): #0,1,2,3,4,5,6
    for y in range(0,3): #0,1,2
        #오른쪽으로 5개를 봐 
        lst = []
        for i in range(5):
            #x는 똑같고 y만 움직여줘
            ny = y + i
            lst.append(mat[x][ny])
        #한줄에 5번 끝
        if lst == lst[::-1]:
            # print(lst)
            cnt += 1
            

#세로로 보기 
for y in range(7):
    for x in range(0,3):
        lst = []
        for i in range(5):
            nx = x + i
            lst.append(mat[nx][y])
        if lst == lst[::-1]:
            # print(lst)
            cnt += 1
            
print(cnt)
            
                    