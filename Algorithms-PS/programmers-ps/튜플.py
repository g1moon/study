'''
1. 중복 가능
2. 순서가 있음 (순서 다르면 -> 다른 투플)
3. 튜플 원소는 유한 

input
원소n개 / 중복없음 -> 튜플이 주어질떄  -> {} 
'''

def solution(s):
    s = s[1:-1]
    ret = []
    a = set()
    for alp in s:
        if alp == "{":
            str = ""
        
        elif alp == "}":
            str_lst = list(map(int,str.split(',')))
            ret.append(str_lst)
            
            str = ""
        
        else:
            str += alp
            
    sorted_lst = sorted(ret, key=len)
    
    res = []
    for lst in sorted_lst:
        for i in lst:
            if i not in res:
                res.append(i)
    
    return res
