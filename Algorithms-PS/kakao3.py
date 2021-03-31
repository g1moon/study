'''

'''
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def getIndex(lst, idx):
    return [lst[i] for i in idx]



def solution(info, query):
    ans = []
    langLst, jobLst, expLst, foodLst, scoreLst = [],[],[],[],[]
    lst = [[],[],[],[],[]]
    
    for i in info:
        tmp = i.split(' ')
        lst[0].append(tmp[0])
        lst[1].append(tmp[1])
        lst[2].append(tmp[2])
        lst[3].append(tmp[3])
        lst[4].append(tmp[4])
    
    #여기에서 정보리스트는 만들어졋고 
    
    cleanQ = []
    for q in query:
        tmp = [ i  for i in q.split(' ') if i != 'and']
        # cleanQ.append(tmp)
        
        for i in range(len(tmp)):
            if tmp[i] == '-':
                continue 
            
        
    
    return ans

print(['1','1','3'].index('1'))

def getIndex(item):
    return [i for i, ele in enumerate(lis) if ele == 1]
