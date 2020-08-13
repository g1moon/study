#자연수 n입력
#첫째행에는 1개원소
#둘째행에는 2배씩 출력되는 원소
n = int(input('N = '))
r = 0
num = 0 
op = True
while op == True:
    for i in range(2**r):
        num += 1
        print(num, end=' ')
        if num == n:
            op = False
            break
    

    r += 1
    print('\n', end ='')
    
