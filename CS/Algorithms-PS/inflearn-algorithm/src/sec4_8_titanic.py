#2명 이하로만 탈 수 있음.
#무게도 M으로 제한되어있음
#N명의 승객 몸무게 가 주어져있을 때 
#승객 모두가 탈출하기 위한 구명보트의 최소 개수 
#각 
N,M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse = 1)


base = 0
cnt = 0
while lst:
    Found = False
    for i in range(1, len(lst)):
        if lst[base] + lst[i] <= M:
            cnt += 1
            pop1, pop2 = lst[base], lst[i]
            lst.pop(lst.index(pop1))
            lst.pop(lst.index(pop2))
            Found = True
            break
        
    if not Found:
        lst.pop(0)
        cnt += 1
        
print(cnt)
    
        
            
            
    
    
        
    
    