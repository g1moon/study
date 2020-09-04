'''
- 7 * 7
- 동서남북 방향으로 5자길이가 회문인지
'''

mat = [list(map(int, input().split())) for _ in range(7)]
#기준을 정하는데  -> 1. 가로로 보는 경우 (y가 2보다 크면 안됨(0,1,2))
            #->2. 세로로 보는 경우 (x가 2보다 크면 안됨(0,1,2))
            
# 그래서 기준을 잡고 
cnt = 0

for x in range(7): #0,1,2,3,4,5,6,7
    for y in range(3): #0,1,2
        lst = mat[x][y:y+5]
        if lst == lst[::-1]:
            cnt += 1

        for k in range(2): #0, 1, 2
            if mat[y+k][x] != mat[y+4-k][x]:
                break
        else:#break를 당하지 않고 정상적으로 포문이 끝남 
            cnt += 1
            
            
        

        
print(cnt)
            
#0하고 4를 비교해야하니까 
#그다음에 (1,3) 