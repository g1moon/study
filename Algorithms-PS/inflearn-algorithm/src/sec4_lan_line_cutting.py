#랜선자르기(결정알고리즘)
#K개의 길이가 다른 랜선
#모두 N개의 같은 길이의 랜선으로 

#N개 이상을 만들어도 됨 -> 최대 랜선 길이 

#K가지고있는 랜선 개수, 필요한 랜선개수 N
K,N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

res = 0
start = 0
end = 10000000000
res_lst=[]
while start <= end:
    res = 0
    mid = (start + end)  // 2
    for i in range(len(lst)):
        res += lst[i] // mid
    
    if res >= N: #더 적게 잘라도됨 -> 크기를 늘려도 됨
        res_lst.append(mid)
        start = mid + 1
    else:
        end = mid -1
        
print(max(res_lst))
        
        
    
        
    
    
    
    