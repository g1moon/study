#16675: 두개의 손
#https://www.acmicpc.net/problem/16675

#양손에 같은 걸 할 수도 있음;
#민성이의 왼손, 오른손, 태경이의 왼손 ,오른손 
#s= 가위
#r= 바위
#p=보

#만약 둘줄 한명이 

in_data = input().split(' ')

ms = in_data[0], in_data[1]
tk = in_data[2], in_data[3]

win_lst = [['R','P'], ['S','R'], ['P', 'S']]
dontKnow = True 

if (len(set(ms)) == 2) and (len(set(tk)) == 2):
    dontKnow = False
    print('?')
    
elif (len(set(ms)) == 1) and (len(set(tk)) == 2):
    for i in range(3):
        if (ms[0] == win_lst[i][0]) and (win_lst[i][1] in tk ):
            # print(1)
            print('TK')
            dontKnow = False 
            break
        
        
        

elif (len(set(ms)) == 2) and (len(set(tk)) == 1):
    for i in range(3):
        if (tk[0] == win_lst[i][0]) and (win_lst[i][1] in ms):
            print('MS')
            dontKnow = False 
            break

#두개다 같은 경우 
else:
    for i in range(3):
        if (ms[0] == win_lst[i][0]) and (win_lst[i][1] == tk[0] ):
            # print(2)
            print('TK')
            dontKnow = False 
            break
        
        elif (tk[0] == win_lst[i][0]) and (win_lst[i][1] == ms[0]):
            print('MS')
            dontKnow = False 
            break
        
if dontKnow:
    print('?')