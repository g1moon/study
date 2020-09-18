def solution(info, query):
    answer = []
    return answer

lang =  'cpp,java,python'.split(',')
position ='backend,frontend'.split(',')
exp =  'junior,senior'.split(',')
food = 'chicken,pizza'.split(',')

def solution(info, query):
    ans = []
    dic = {'lang' : [], 'pos': [], 'exp' : [],'food': [], 'score': []}
    
    for i in info:
        t = i.split()
        r = t.pop()
        t.append(int(r))
        
        dic['lang'].append(t[0])
        dic['pos'].append(t[1])
        dic['exp'].append(t[2])
        dic['food'].append(t[3])
        dic['score'].append(t[4])
    
    # print(dic)#----------------------------------------   
    for i in query:
        a = i.split(' and ')
        b = a.pop()
        a += b.split()
        # a=  ['-', 'backend', 'senior', '-', '150']
        prob_idx = []
        #_---------------------------------------
        if a[0] == '-':
            prob_idx = [ i for i in range(0, len(dic['lang']))]
        else:
            for i in range(len(dic['lang'])):
                if dic['lang'][i] == a[0]:
                    prob_idx.append(i)
            if len(prob_idx) == 0:
                ans.append(0)
                continue
        # print('1', prob_idx)
        #-------------------------------------------
        if a[1] == '-':
            pass
        else:
            tmp = []
            for i in prob_idx:
                if dic['pos'][i] == a[1]:
                    tmp.append(i)
            prob_idx = tmp 
        # print('2', prob_idx)
        #----------------------------------------------
        if a[2] == '-':
            pass
        else:
            tmp = []
            for i in prob_idx:
                if dic['exp'][i] == a[2]:
                    tmp.append(i)
            prob_idx = tmp 
        # print('1', prob_idx)
        #----------------------------------------------
        if a[3] == '-':
            pass
        else:
            tmp = []
            for i in prob_idx:
                if dic['food'][i] == a[3]:
                    tmp.append(i)
            prob_idx = tmp 
        #-----------------------------------    
        if a[4] == '-':
            ans.append(len(prob_idx))
        else:
            tmp = []
            for i in prob_idx:
                if dic['score'][i] >= int(a[4]):
                    tmp.append(i)
            prob_idx = tmp 
        
        
        # print('----------------')
        ans.append(len(prob_idx))
        # print(prob_idx)
        # break
        
        
        
        
        
        
    return ans


#-----------------------------
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))


