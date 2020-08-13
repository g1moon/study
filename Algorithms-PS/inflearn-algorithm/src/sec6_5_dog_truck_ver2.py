#트럭은 c킬로그램 넘게 태울 수 없음
#C를 넘지 않으면서, 가장 무겁게
#N마리의 바둑이, 각 바둑이 무게 W



##########
def dfs(idx, weight, total_sum):
    # print(weight)
    global ret 
    if weight > C:    
        return 
    
    if weight + (sum(lst) - total_sum) < ret:
        return 

    # print(sum(lst))
    if weight +  (sum(lst) - weight) < ret:
        return 
        
    if idx == N:
        # print(1111)
        if weight > ret:
            ret = weight
        return

    dfs(idx + 1, weight + lst[idx], total_sum + lst[idx])
    dfs(idx + 1, weight,  total_sum + lst[idx])
############

if __name__ == '__main__':
    C, N = map(int,input().split())
    # print(C,N)
    lst = [ int(input()) for i in range(N)]
    # print(lst)  
    ret = 0
    
    dfs(0,0,0)
    print(ret) 

    
    
