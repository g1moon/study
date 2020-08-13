#마구간  x1~xN
#c마리의말, 
#1마구간에 1말 ,, 가장 가까운 두 말의 거리가 최대가 되게 
#c마리의 말, n개의 마구간에 배치
#두 말의 거리가 최대가 되게하는 값
def shortest_dist(lst):
    min_dist = lst[1] - lst[0]
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i] < min_dist:
            min_dist = lst[i+1] - lst[i]
    return min_dist


N,C = map(int, input().split())
lst = sorted([int(input()) for i in range(N)])
start = lst[1] - lst[0]
end = lst[-1] - lst[0]

while start <= end:
    cnt  = 1
    gap = (start + end) // 2
    gap = 190
    left = 0
    right = 1
    while True:
        if left > len(lst)-1 or right  > len(lst)-1:
            break
        
        if lst[right] - lst[left] >= gap:
            cnt +=1 
            left = right 
            right = right+1
        
        else:
            right += 1
    
    
    if cnt == C: #더 넓혀도 된다.
        ret = gap
        start = gap + 1
    elif cnt > C:#말이 너무 많아 -> 간격을 좀 넓히자
        start = gap + 1
    else:
        end = gap -1
    print(cnt)
    break

    
        
