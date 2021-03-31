'''
- 단품 메뉴 -> 조합 -> 코스요리
- 가장 많이 주문한 메뉴들로 -> 코스구성 
- 최소 2가지 이상 
- 최소 2명 이상 주문된 단품메뉴들로 


'''
#
from itertools import combinations, permutations
#
# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	
# course = [2,3,4]	
# result = ["AC", "ACDE", "BCFG", "CDE"]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	
course = [2,3,5]	
result = ["AC", "ACDE", "BCFG", "CDE"]

orders = ["XYZ", "XWY", "WXA"]	
course = [2,3,4]	
result = ["WX", "XY"]


def solution(orders, course):
    ans = []
    
    for i in course:
        tmpDic = {}
        for order in orders:
            tmpList = list(combinations(order, i))
            for tmp in tmpList:
                if tmp in tmpDic.keys():
                    tmpDic[tmp] += 1                
                else:
                    tmpDic[tmp] = 1 
        
        sortedDic = sorted(tmpDic.items(), key=lambda x: x[1], reverse=True)     
        print(sortedDic)
        if not sortedDic:
            continue
        maxCnt = sortedDic[0][1]
        
        #2보다 작으면 넘어가고 
        if maxCnt < 2:
            continue 
        
        #아니면 maxCnt인 것만 리스트에 추가해 
        for k, v in sortedDic:
            if v != maxCnt:
                break 
            
            strK = ''.join(k) 
            ans.append(strK)
            
    ans.sort()
    return ans

print(solution(orders, course) == result)
    
    
        

    


