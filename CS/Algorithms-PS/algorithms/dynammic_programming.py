#Dynamic programming###############################
#작은 문제를 점점 크게 만들어보자 
#리컬젼들이 잡아먹는 불피요한 펑션콜은 없애
#dynamic programming : a general alogorithm design tech for solving 
#problems : defined by or formulated as recurrences with overlapping 
#sub- instances

#moemoization (storing the result of previous function call to 
# reuse the results again in the future 
# 피보나치를 볼때 피보(0)부터 풀고 -기록하다보면 -> 언젠가 목표에 도달하지 않을까?
#recursion과 dp는 접근 방밥이 상반된다 
#recursion-top down, #dynamic programming- bottom up 

def fiboDP(n):
    #setting up a memoization table
    dic = {}
    dic[0] = 0
    dic[1] = 1
    for itr in range(2, n+1):
        dic[itr] = dic[itr-1] + dic[itr-2]
    
    return dic[n]

#execution part 
for itr in range(0,10):
    print(fiboDP(itr))


