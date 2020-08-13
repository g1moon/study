'''
- 3개일떄 -> 0개쓰냐 1개쓰냐 2개쓰냐 3개쓰냐
	-> for문 돌면서 처리
- cur_sum이 target 이면 멈추고 
- idx가 == k -> 종료 
- cur_sum이 이미 target을 넘으면 종료


'''

def dfs(idx, cur_sum):
    global cnt

    if cur_sum > target:
        return

    if cur_sum == target:
        cnt += 1
        return 

    if idx == k:
        return 
    
    else:
        for i in range(0,num_lst[idx]+1):             
            dfs(idx+1, cur_sum + (coin_lst[idx] * i))



if __name__ == "__main__":
    
    #init
    coin_lst = []
    num_lst = []
    cnt = 0
    
    #
    target = int(input())
    k = int(input()) #동전가지수
    for _ in range(k):
        p, n = map(int, input().split())
        coin_lst.append(p)
        num_lst.append(n)

    #
    dfs(0,0)
    #
    print(cnt)