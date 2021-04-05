
import sys
input = sys.stdin.readline
'''
- 모든 괄호를 뽑아 -> 올바른 순서대로 배치된 괄호 문자열을 알려주는 
- (의 개수와 )의 개수가 같으면 -> 균형 
- 짝도 모두 맞으면 -> 균형 and 올바른 (짝맞고, 개수 같고)
- 균형잡힌 문자열이라면 -> 올바른으로 변경 
- 2
    - w -> u,v -> 
    - u는 균형잡힌으로 -> 더 이상 분리 할 수 없어야 하고 
    - v는 빈 문자열 가능 
    - u가 올바른 문자열이면 -> v에 대해 다시 1단계부터 
'''

#2
p = ")("	
result = "()"
#3
p = "()))((()"	
result = "()(())()"
#1
p = "(()())()"	
result = "(()())()"

#3
p = "()))((()"	
result = "()(())()"

def checkRight(s):
    stack = [] 
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            #(도 없는데 -> )이게 나올떄 
            else:
                return False
    if stack:
        return False 
    else:
        return True
    

def splitString(s):
    u = ''
    openCnt, closeCnt = 0, 0 
    
    for i in range(len(s)):
        if s[i] == '(':
            openCnt += 1
            u += s[i]
            
        else:
            closeCnt += 1
            u += s[i]
        
        if openCnt == closeCnt:
            break 
    
    try: v = s[i+1:]
    except : v = ''
    
    return u, v 



def solution(s):
    ans = ''
    #1
    if s == '':
        return ''
    
    #2
    u, v = splitString(s)
    
    #3
    if checkRight(u):
        ans += u
        ans += solution(v)
        
    
    else:
        tmp = ''
        tmp += '('
        tmp += solution(v)
        tmp += ')'
        
        #뒤집기 
        u = u[1:-1]
        new = ''
        for i in u:
            if i == '(' : new += ')'
            else: new+='('
        tmp += new 
        #ans 뒤에 붙이기 
        ans = tmp 
        
    return ans 
        
    

print(solution(p))
print(solution(p) == result)

