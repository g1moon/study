
N = int(input()) #N미터인 선
lst = [0] * (N+1)

#2일때는 2개
#1일때는 1개 
lst[1] = 1
lst[2] = 2
depth_num = 0 
def dfs(n):
    global lst
    if lst[n] != 0:
        return 
    # #선이 2와 1이면 종료
    if n == 2:
        return 
    elif n ==1:
        return
        
    
    dfs(n-1)
    dfs(n-2)
    
    lst[n] = lst[n-1] + lst[n-2]
    
dfs(N)
print(lst[-1])