'''
- N * N 격자판으로 이루어져 있음 (홀 수 )
- 다이아몬드 격자판만 수확하고, 나머지 격자안의 사과는 남겨둠 
'''
#input()
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
# print(mat)

start_lst = []
end_lst = []
basis = n//2

start, end = basis, basis
res = 0

start_down = True
for row in range(0, n): # 0 1 2 3 4 
    for col in range(start, end+1):
        res += mat[row][col]
    
    if row < basis:
        start -= 1
        end += 1
    
    else:
        start += 1
        end -= 1
    
print(res)