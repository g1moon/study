#4
###############

#행과열을 바꾼다 
#행과열의 수는 같고 
#리스트
#각 문제에 한줄의 코드만 L은 바뀔 수 있음


def trans(m):
    result = []
    
    for i in range(len(m)): #0~3
        ###code hear######
        row = []
        result.append(row)

    i = 0 
    while i < len(m): #4
        j = 0  
        while j < len(m[i]) : #4,3,2,1
            ###code hear######  
            result[i].append(m[j][i])
            j += 1
        i += 1
    return result

################
def printToMatrix(m):
    for i in range(len(m)):
        ###code hear######
        row = m[i]
        for j in range(len(m)-len(row)):
            print('{:3}'.format(' '), end = ' ')
            
        for j in range(len(row)):
            print('%3s' %row[j], end = ' ')
            
        print()

#main
L = [[2,4,8,14], 
     [6,10,16], 
     [12,18],
     [20]]
M = trans(L)
printToMatrix(M)