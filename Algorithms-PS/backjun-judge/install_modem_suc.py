n,c = list(map(int, input().split(' ')))

arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)

start = arr[1]- arr[0]
end = arr[-1] - arr[0]
res = 0

while start <= end:
    mid = (start + end ) // 2 #mid는 갭임 
    val = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] >= val + mid:
            val = arr[i]
            cnt += 1
            
    if cnt >= c: #더 많이 설치했어 -> 갭을 조금 늘려볼까? 
        start = mid + 1 #더 증가시켜보고 
        res = mid #우선 저장
        print(f'{1}, start:{start}, end:{end}, gap:{mid}')
    else: #적게 설치했어 -> 갭을 줄여보자
        end = mid -1
        print(f'{2}, start:{start}, end:{end}, gap:{mid}')
    
print(res)
        
        
        
    
    
    