


def solution(n, s, a, b, fares):
    dic = {}
    pdic = {}
    answer = 0
    #----------------------------------
    for f in fares:
        q, w, e = map(int,f)
        print(q,w,e)
        if q in pdic.keys():
            pdic[q].append(w)
        else:
            pdic[q] = [w]
        
        if q in dic.keys():
            dic[q][w] = e
        else:
            dic[q] = [0] * 201
            dic[q][w] = e
    #-------------------------------
    print(pdic)
            
            
    return answer

#----------------------
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))