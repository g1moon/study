
import copy 
from operator import itemgetter, attrgetter

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]




def solution(info, query):
    ans = []
    lst = [[],[],[],[],[]]
    
    for i in info:
        tmp = i.split(' ')
        lst[0].append(tmp[0])
        lst[1].append(tmp[1])
        lst[2].append(tmp[2])
        lst[3].append(tmp[3])
        lst[4].append(int(tmp[4]))

    
    for q in query:

        posLst = [ i for i in range(len(info))]
        tmp = [ i  for i in q.split(' ') if i != 'and']
        # print(f'''
        #       q      : {q}
        #       posLst : {posLst}
        #       '''
        # )
        #여기서 5개의 질문 처리하는데 -> -면 넘어가고 -> 아닌 경우에는 
        #posLst에서 모두 보면서 -> 맞는 것만 tmpLst 넣고
        #tmpLst를 posLst로 바꾼다. 
        for infoType in range(len(tmp)):
            # print(posLst)
            if infoType != 4:                
                if tmp[infoType] == '-':
                    continue
                
                tmpLst = []
                for posIdx in posLst:
                    if lst[infoType][posIdx] == tmp[infoType]:
                        tmpLst.append(posIdx)
                posLst = copy.deepcopy(tmpLst)
                
                
            else:
                if tmp[infoType] == '-':
                    continue
                tmpLst = []
                for posIdx in posLst:
                    if lst[infoType][posIdx] >= int(tmp[infoType]):
                        tmpLst.append(posIdx)
                posLst = copy.deepcopy(tmpLst)

        ans.append(len(posLst))
    return ans 

print(solution(info, query))