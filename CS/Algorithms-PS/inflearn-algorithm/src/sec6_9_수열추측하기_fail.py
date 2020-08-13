# 수열 추측하기 
#1~N까지의 숫자가 한개씩
#두번쨰 줄 부터는 더해져서 

#input: N, 가장밑에있는 숫자(F)
#output : 가장 윗 줄에 있는 숫자를 구하기 
    # -> 답이 여러개면 사전순으로 가장 앞에오는 것 출력 
# 1. 모든 수의 조합을 찾는다 -> 그러고 arr_lst 에 append
# 2. 파스칼을 계산한다. (cal)

def dfs(idx):
    if idx == N:
        print(arr)
        
    
    else:
        for i in range(1,N+1):
            if i in arr[:idx]: continue 
            arr[idx] = i
            dfs(idx+1)
        
def cal(arr):
    if len(arr) == 1:
        if arr[0] == F:
            find = True
            return  arr[0], arr
    
    else:
        new_arr = []
        for i in range(len(arr)-1):
            new_arr.append(arr[i] + arr[i+1])
        cal(new_arr)
        


if __name__ == "__main__":
    find = False
    N,F = map(int, list(input().split()))
    # print(N,F)
    arr = [0 for i in range(1,N+1)]
    arr_lst = [] # dfs -> append(모든 조합의 arr)
    dfs(0)
    
     

        
    
    
    
    