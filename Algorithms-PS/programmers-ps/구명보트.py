'''
- 구명보트는 한번에 최대 2명, 무게제한 있음
- 구명보트를 최대한 적게 사용해 -> 모든 사람 구출 
- 모든 사람을 구출하기윈한 -> 구명보트 최소 
'''
def solution(people, limit):
    
    lst = sorted(people, reverse = True)
    cnt = 0 
    pos = []
    
    while True:
    #반복문 돌면서 가능한거 넣어주고 
        t = 0
        tmp_t = 0 
        cnt += 1
        for i in range(len(lst)):
            if t + lst[i] <= limit:
                t += lst[i]
                lst[i] = 0
                tmp_t += 1
            
            if tmp_t == 2:
                # lst = [i for i in lst if i !=0]
                break 
        
        lst = [i for i in lst if i !=0]
        if not lst:
            break


    
    return cnt
