'''
- 단품을 -> 조합해서 코스요리로
- 가장 많이 주문한 단품메뉴들을 -> 코스요리로
- 최소 2가지 이상의 단품메뉴로 구성
- 최소 2명이상에게 주문된 단품메뉴 조합에 대해서만 요리후보


'''
from itertools import combinations
def solution(orders, course):
    answer = []
    alp_lst = list('abcdefghijklmnopqrstuvwxyz'.upper())
    prob_lst = []
    for order in orders:
        tmp_lst = list(order)
        for c in course:
            prob_lst += list(combinations(tmp_lst,c))
    print(prob_lst)
    dic = {}

    for i in prob_lst:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    
    for k, v in dic.items():
        if v >= 2:
            print(k, v)
            
     
    return answer




#------------------------------
orders =["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))