n = int(input())
mat = [ list(map(int, input().split())) for _ in range(n)]
m = int(input())
cmd_lst = [list(map(int, input().split())) for _ in range(m)]


for i in range(len(cmd_lst)):
    a, dir, rcnt = cmd_lst[i]
    #a-1행을 dir방향으로 rot_cnt번
    if dir == 0:
        org_lst = mat[a-1]
        for _ in range(rcnt):
            item = org_lst.pop(0)
            org_lst.append(item)
        mat[a-1] = org_lst
    
    
    else:
        org_lst = mat[a-1]
        temp_lst = []
        for _ in range(rcnt):
            item = org_lst.pop()
            temp_lst.append(item)
        
        mat[a-1] = temp_lst[::-1] + org_lst
        
# print(mat)
#===============================================
start, end = 0, (n-1)
res = 0
for row in range(0, n):
    for col in range(start, end+1):
        res += mat[row][col]
        
    if row < n//2:
        start += 1
        end -= 1
    
    else:
        start -=1
        end += 1

print(res)
        
        
    