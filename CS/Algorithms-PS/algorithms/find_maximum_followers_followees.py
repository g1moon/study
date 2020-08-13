mat = [[0,0,0,1,0],[1,0,0,1,0],[1,0,0,1,1],[1,0,0,0,0],[0,0,0,1,0]]
col_dic={}
row_dic={}

for i in range(5):
    col_dic[i] = 0 

for i in range(5):
    row_dic[i] = 0

for r in range(5):
    for c in range(5):
        if mat[r][c] !=0:
            col_dic[c] += 1
            row_dic[r] += 1  


c = list(col_dic.items())
r = row_dic.items()
    
c = sorted(c, key = lambda x: x[1], reverse=True)
r = sorted(r, key = lambda x: x[1], reverse=True)

print(f'Maximum followers per a followee: {c[0][1]}') #followee
print(f'Maximum followees per a follower: {r[0][1]}') #follower

