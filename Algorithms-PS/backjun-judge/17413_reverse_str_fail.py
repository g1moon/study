
instr = input()


def reverse_str(instr):
    lst = list(instr)
    lst.reverse()
    ret = ''
    for i in lst:
        ret += i
    return ret

def isCom(instr):
    ret = True
    for i in instr:
        if (i == '<') or (i =='>'):
            return False
    return ret 


#main###################
ret = ''
isComplete = False

if isCom(instr):
    isComplete = True
    str_lst = instr.split(' ')
    for i in str_lst:
        ret += reverse_str(i) + ' '
        
        
if isCom(instr) == False:
    start = 0 
    while isComplete == False:
        if instr[start] == '<':
            #이거인데 만약 start가 0이 아니야 -> 그러면 숫자라는거거든
            if start > 0:               
                
                if instr[0] == ' ':
                    print(1)
                    d = 0
                    while True:
                        if instr[d] ==' ':
                            ret += ' '
                            d += 1
                            continue    
                        else:
                            break
                        
                elif ' ' in instr:
                    a  = instr[:start].split(' ')
                    for i in range(len(a)):
                        if i == len(a)-1:
                            ret += reverse_str(a[i])
                            break
                        ret += reverse_str(a[i]) + ' '
                    
                        
                    
                else:          
                    ret += reverse_str(instr[:start])
                instr = instr[start:]
                isComplete = isCom(instr)
                start = 0
                continue
            
            for end in range(start, len(instr)):
                if instr[end] == '>':
                    #새로정의해주고, ret에 추가
                    ret += instr[start: end+1]
                    instr = instr[end+1:]
                    isComplete = isCom(instr)
                    start = 0
                    break
        else:
            start += 1
            
    ret += reverse_str(instr)
print(ret)
print(instr)

