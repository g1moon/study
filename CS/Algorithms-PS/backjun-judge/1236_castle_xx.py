# 1236번: 성 지키기
# https://www.acmicpc.net/problem/1236

def check(mat,row,col):
    for i in range(row):
        for col in range(col):
            if mat[row][col] == '.':
                return False
    return True


nm = list(map(int,input().split(' ')))
r,c= nm[0], nm[1]

mat = []
for _ in range(r):
    l = []
    input_data = input()
    for i in range(c):
        l.append(input_data[i])
    mat.append(l)


for row in range(r):
    for col in range(c):
        if mat[row][col] == 'X':
            for i in range(c):
                mat[row][i] ='a'
            for i in range(r):
                mat[i][col] ='a'

men = 0
while 1:
    for row in range(r):
        for col in range(r):
            if mat[row][col] == '.':
                men +=1 
                for i in range(c):
                    mat[row][i] ='a'
                for i in range(r):
                    mat[i][col] ='a'

    if check(mat,row,col) == True:
        break

print(men)

