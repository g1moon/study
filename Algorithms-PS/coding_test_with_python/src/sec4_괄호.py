'''
- 괄호 갯수 맞추기
- 소스 코드에 작성된 모든 괄호 뽑아서 -> 순서대로 배치된 괄호 문자열을 알려주는 프로그램

- 1. ), ( 로만 구성된 문자열 -> '균형잡힌 괄호 문자열'
    -> 여기에 짝이 다 맞으면 -> '올바른 괄호 문자열'
    
- 균형잡힌 괄호 문자열에서 -> 올바른 괄호 문자열로 변환하는법

1. str = '' -> '' 반환
2. 
'''

##----------------------------
def ck_right(str):
    stack = []
    for i in str:
        stack.append(i)
        remain = True
        while remain:
            try:
                if stack[-1] == ')' and stack[-2] == '(':
                    stack.pop()
                    stack.pop()
                else:
                    remain = False
            except:
                break 
    if not stack:
        return True
    else:
        return False
#-------------------------------
p = "()))((()"
p =')('
def solution(p):
    answer = ''
    
    open_cnt = 0
    close_cnt = 0
    u, v = '', ''
    for i in range(len(p)):
        if p[i] == '(':
            open_cnt += 1
        else:
            close_cnt += 1
        
        if open_cnt == close_cnt:
            u = p[:i+1]
            v = p[i+1:]
            break
    else:
        u = p
        v = ''
    
    print(u)
    print(v)
        
        
        
    
    return answer
#-----------------------------    
print(solution(p))
            
        
            
        
        
        
