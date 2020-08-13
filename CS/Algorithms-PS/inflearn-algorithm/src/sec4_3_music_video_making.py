#뮤직비디오
#M개의 DVD에 모든 동여상을 녹화 
#이때 DVD 녹화 길이를 최소로 한다 
#1. M개의 DVD는 모두 같은 크기여야함 

N,m = map(int, input().split())
lst = list(map(int, input().split()))

start, end  = 0, 10000000

while start <= end:
    run_time = 0
    idx = 0
    res = 0
    mid = (start + end) // 2
    while True:
        run_time += lst[idx] 
        if idx == len(lst)-1:
            if run_time <= mid:
                res += 1
                break
            else:
                res +=2
                break
            
        
        
        if run_time > mid:
            res +=1
            run_time = 0
        else:
            idx += 1

    ##############################
    #몇개로 만들수 있는지 나오겠지?res
    if res <= m: #간격을 줄여야해
        ret = mid 
        end = mid - 1
    elif res > m: #너무 많이 만들어짐, 간격을 늘려야해
        start = mid + 1
print(ret)
        
    