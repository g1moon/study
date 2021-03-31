# https://www.acmicpc.net/problem/1759
# boj 2529 S2 부등호 
#<메모리 : 127492, 시간 : 192>
import sys
input = sys.stdin.readline
'''
# -----솔루션--------------------------
- 1. ck 함수 내 조건 만족하고 
- 2. used에 없으면 
'''

# new_id, result = "...!@BaT#*..y.abcdefghijklm", "bat.y.abcdefghi"
# new_id, result = "z-+.^.", "z--"
new_id, result = "123_.def", ''
new_id, result = "=.=", ''	


def solution(new_id):
    tmp = new_id
    
    #1 
    tmp = tmp.lower()
    print('1', tmp)
    
    #2
    alpList = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    tmpList = []
    for i in tmp:
        if (i in alpList) or (i in ['-','_','.']) or (i in ['1','2','3','4','5','6','7','8','9','0']):
            tmpList.append(i)
    tmp =  ''.join(tmpList)
    print('2', tmp)
    
    #3
    tmpList = []
    cnt = 0
    flag = False
    for i in tmp:
        if i == '.':
            cnt += 1
            continue 
        
        if cnt != 0 and i !='.':
            tmpList.append('.')
            cnt =0

        tmpList.append(i)
        
    tmp = ''.join(tmpList)
    print('3', tmp)
    
    #4 
    if not tmp: 
        pass
    else:
        if tmp[0] == '.': 
            tmp = tmp[1:]
            
        if tmp[-1] == '.':
            tmp = tmp[:-1]
    print('4', tmp)
        
    #5
    if tmp == '':
        tmp = 'a'
    print('5', tmp)
        
    #6
    if len(tmp) >= 16:
        tmp = tmp[:15]
        if tmp[-1] == '.':
            tmp = tmp[:-1]
            
    print('6', tmp)
        
    #7
    if len(tmp) <= 2:
        a = tmp[-1]
        
        while len(tmp) < 3:
            tmp += a
    print('7', tmp)
        
    answer = tmp
    
    return answer

print(solution(new_id))