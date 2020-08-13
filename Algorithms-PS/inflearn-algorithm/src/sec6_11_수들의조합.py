'''
N개의 정수가 주어지면 -> 그 숫자들중 K개를 뽑는 조합의 합이 -> 임이의 정수 M의 배수의개수는 몇개?

'''

def dfs(idx,start_idx):
    global cnt
    if idx == K:
        if sum(res) % M == 0:
            cnt += 1
            return 
    else:
        for i in range(start_idx, N):
            res[idx] = lst[i]
            dfs(idx+1, i+1)



if __name__ == "__main__":
    N,K = map(int, input().split())
    lst = list(map(int, input().split()))
    M = int(input())
    cnt = 0
    res = [0 for i in range(K)]
    
    dfs(0,0)
    print(cnt)