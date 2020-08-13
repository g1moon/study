
def check_remain_tag(instr):
    if ('>' in instr) or ('<' in instr):
        return True
    return False
    
def process_words(instr, ret):
    while True:
        if ' ' in instr:
            if instr[0] == ' ':
                ret += ' '
                instr = instr[1:]
            else:
                ret += instr[: instr.index(' ')][::-1]
                instr = instr[instr.index(' '):]
        
        else:
            ret += instr[::-1]
            return ret
            break

                
                
        
# print(process_words(' asd tag', '<open>' ))

# main
def f():
    instr = input()
    ret = ''
    isTag = check_remain_tag(instr)
    if isTag == False:
        print(process_words(instr, ret))
        return 

    while isTag:
        if instr[0] == '<':
            # print(1)
            # print(instr,'//', ret)
            ret += instr[: instr.index('>')+1]
            instr = instr[instr.index('>')+1:]
            isTag = check_remain_tag(instr)
        
        else:
            # print(2)
            # print(instr,'//', ret)
            words = instr[: instr.index('<')]
            ret = process_words(words, ret)
            instr = instr[instr.index('<'):]
            isTag = check_remain_tag(instr)
            
    #결국 instr은 태그가 다 빠져서 올거니까 남은 문자열 처리도 해줄 수 있음
    print(process_words(instr, ret))        

    return 
    
    
            
f()





#만약 idx = 0에서 <가 나오면 다음 '>'인덱스를 찾고 -> instr = instr[>idx+1:]
#ret = ret + instr[:>idx+1]
#이제 instr에 태그가 있는 지 찾고 -> 있다면 -> 다시찾고(수정)
#없다면 -> instr을 뒤집어서 추가하는데 공백끼리 나눠줘야함
#
#만약 idx가 >가 아니면 -> 



#태그와 태그사이에만한정시켜야함
#[:다음공백] -> ac를 뒤집어서 ret에넣어주고 -> 
# str = str[위공백:] -> 공백인덱스오류 안나네?(또잇음)  ' bd ca'
# -> [:다음공백] -> 
#만약 맨앞이 공백이면 ? -> 공백을 ret에 넣어주고 -> str = instr[1:] -> 공백없으면->break



            
    
                
                
                
            
        
        
        
    
    
    