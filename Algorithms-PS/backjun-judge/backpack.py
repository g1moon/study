n, k = map(int, input().split())

wgt_lst, val_lst = [], []
for _ in range(n):
    wgt, val = map(int, input().split())
    wgt_lst.append(wgt)
    val_lst.append(val)

#dp table
dp = [[0] * (k+1) for _ in range(n+1)]
# print(dp)


#idx, tmp_k
for idx in range(1, n+1):
    wgt, val = wgt_lst[idx-1], val_lst[idx-1]
    for tmp_k in range(k+1):
        if wgt > tmp_k:
            dp[idx][tmp_k] = dp[idx-1][tmp_k] #이전거 복사
        else:
            dp[idx][tmp_k] = max(dp[idx-1][tmp_k], 
                                 dp[idx-1][tmp_k-wgt] + val)
            
print(max(dp[-1]))
    
        
         
        
        
