# https://www.acmicpc.net/problem/1541
# boj 1541 S2 (잃어버린 괄호)

'''
- 양수, + , - , 괄호로 -> 식을 만들고 -> 괄호 모두 삭제
- 괄호를 쳐서 -> 이 식의 값을 최소로 
- 괄호로 이 식의 값을 최소로 만들기 
- 5자리보다 많이 연속되는 숫자는 없음 
'''
import sys
instr = input()
res = 0
if '-' not in instr and '+' not in instr:
    res = int(instr)

elif '-' in instr:
    f = instr[: instr.index('-')] #+만있을거임 
    r = instr[instr.index('-')+1:]
    r = r.replace('+','-')
    
    f = list(map(int, f.split('+')))
    r = list(map(int,r.split('-')))
    
    res += sum(f)
    res += sum(r)*-1
    
    
else:
    res = sum(list(map(int,instr.split('+'))))
    
    
print(res)
    

