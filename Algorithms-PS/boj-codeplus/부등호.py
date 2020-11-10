'''
op : 부등호 담은 리스트
res : 결과 리스트 
'''

def ck(num1, num2,opt):
    if opt == '<':
        if num1 < num2:
            return True
        return False
    
    elif opt == '>':
        if num1 > num2:
            return True
        return False


#range(1,9)중 -> ck만족하고 , used에 없으면 
def dfs(idx, used):
    global min_num, max_num, min_ans, max_ans
    if idx == k+1:
        ans.append(used)
        return 
    
    #맨처음에는 다 돌아
    if idx == 0:
        for i in range(10):
            dfs(idx+1, used+[i])
            # res[idx] = 0
    else:  
        for i in range(10):
            if (i not in used)  and ck(used[idx-1], i, op[idx-1]):
                dfs(idx+1, used + [i])
                # res[idx] = 0
    
    return 

    

if __name__ == "__main__":
    k = int(input())
    op = input().split()
    min_num, max_num = 2300000, -2300000
    ans = []
    dfs(0, [])
    ans.sort
    print(''.join(list(map(str,ans[-1]))))
    print(''.join(list(map(str,ans[0]))))
    
    
    