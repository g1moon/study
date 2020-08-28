n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst, reverse=True)

fir = lst[0]
sec = lst[1]

##
res = 0
cnt = 0
while cnt <= m:
    for _ in range(3):
        res += fir
        cnt += 1
        if cnt == m:
            break 
        
    if cnt == m:
        break 
    res += sec
    cnt += 1
    if cnt == m:
        break 
print(res)
    

    
    
        