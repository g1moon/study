'''
한자리 숫자가 적힌 종이 조각이 흩어져있다.
흩어진 종이 조각을 붙여, 소수를 몇개 만들 수 있는지 


'''
import copy
#소수
def find(n):
    num=set(range(2,n+1))
    for i in range(2,n+1):
        if i in num:
            num -=set(range(2*i,n+1,i))
    return len(num)

def dfs(idx):
    global ck, res, lst, res_lst
    
    if idx == len(numbers):
        tmp = copy.deepcopy(res)
        tmp = [ i for i in tmp if i != -1]
        print(int(''.join(list(map(str, tmp)))))
        return 
    
    else:
        for i in range(len(numbers)):
            if ck[i] == 0:
                res[idx] = lst[i]
                ck[i] = 1
                dfs(idx + 1) 
                res[idx] = -1
                tmp = copy.deepcopy(res)
                tmp = [ i for i in tmp if i != -1]
                print(''.join(list(map(str, tmp))))

                ck[i] = 0
            else:
                continue 
        

def solution(numbers):
    res_lst = []
    global  ck, res, lst
    ck = [0] * len(numbers)
    res = [-1] * len(numbers)
    
    lst = list(numbers)
    lst = list(map(int, numbers))
    
    
    dfs(0)
    return 

if __name__ == '__main__':
    #in
    numbers = "011"
    # numbers = "011"
    
    #out
    print(solution(numbers))
    print('--------------')