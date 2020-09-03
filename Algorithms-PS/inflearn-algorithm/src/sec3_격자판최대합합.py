#격자판 최대합 
# 

n = int(input())

m = 0
mat = []
#입력 + 행으로 제일 큰 값
for _ in range(n):
    a = list(map(int, input().split()))
    m = max(m, sum(a))
    mat.append(a)
    
#열로 가장 큰 값 뽑기 
for col in range(n):
    col_sum = 0
    for row in range(n):
        col_sum += mat[row][col]
    m = max(m, col_sum)
    
#대각선으로 
diag_sum1 = 0
diag_sum2 = 0
for i in range(0, n):
    diag_sum1 += mat[i][i]
    diag_sum2 += mat[i][n-i-1]
        
m = max(m, diag_sum1)
m = max(m, diag_sum2)
print(m)

print(diag_sum1)
print(diag_sum2)
        
    
    

