'''
- (N개의 수로 이루어진 수열 A1~AN)
- (N-1)개의 연산자 +,-,x,나
- 음수 // 양수 -> -(양수 // 양수)
'''

def dfs(idx):
    global res
    if idx == N-1:
        #-----------------------------------------
        print(res)
        #-----------------------------------------
        res[idx-1] = -1
        return 
    
    else:
        for i in range(N-1):
            if i not in res:
                res[idx] = i
                dfs(idx+1)
                res[idx] = -1
                
            
    
if __name__ == "__main__":
    #input()
    N = int(input())
    A = list(map(int, input().split()))
    OP = list(map(int, input().split()))
    
    a =''
    a += '+'*OP[0]
    a += '-'*OP[1]
    a += '*'*OP[2]
    a += '%'*OP[3]
    
    #연산자개수를 담은 리스트 
    op_lst = list(a)
    
    res = [-1] * len(op_lst)
    print(op_lst)


    ret = []
    dfs(0)
    
    from itertools import product, combinations, permutations
    
    print(op_lst)
    
    
    