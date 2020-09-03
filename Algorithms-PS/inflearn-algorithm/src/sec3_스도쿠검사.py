'''
- 각 행에 1부터 9까지 숫자가 중복없이 있고
- 각 열에 1부터 9까지의 숫자가 중복없이 나오고 
- 각 3 * 3 사각형에 1부터 9가 중복없이 나옴
'''

mat = [ list(map(int, input().split())) for _ in range(9)]
# print(mat)

lst = [(0,2), (3,5), (6,8)]
right_lst = [1,2,3,4,5,6,7,8,9]
row_st, row_end = 0, 2
col_st, col_end = 0, 2

fail = False
for j in range(3):
    for i in range(3):
        ck_lst = []
        for row in range(row_st, row_end +1):
            for col in range(col_st, col_end+1): #0~2
                ck_lst.append(mat[row][col])
        row_st += 3
        row_end += 3
        if set(ck_lst) != set(right_lst):
            fail = True
            
    row_st, row_end = 0, 2
    col_st += 3
    col_end += 3

        

for row in range(9):
    ck_lst = []
    for col in range(9):
        ck_lst.append(mat[row][col])
    if set(ck_lst) != set(right_lst):
        fail = True    
for col in range(9):
    ck_lst = []
    for row in range(9):
        ck_lst.append(mat[row][col])
    if set(ck_lst) != set(right_lst):
        fail = True

        
if fail:
    print("NO")
else:
    print('YES')
            
                
    