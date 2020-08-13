#i를 행, j를 열
#정방행렬의 크기 N을 입력받아 0과 1을 입력 
import random 
def printMatrix(n):
    ret = []
    a = []
    isZero = 0 
    for i in range(n):
        a = []
        for k in range(i):
            a.append(random.randint(0,1))
        a.append(0)
        
        while len(a) != n:
            a.append(random.randint(0,1))
        
        ret.append(a)
    
    for lst in ret:
        for i in lst:
            print(i, end= ' ')
    
N = int(input('N = '))
printMatrix(N)