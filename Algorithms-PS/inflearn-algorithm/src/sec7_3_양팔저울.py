#(K개의 추, 빈그릇) -추의 무게는 정수, 그릇의 무게는 0
#(모든 추의 합 S) 

#양팔 저울을 한번만 이용해 (1~S)사이에 대응되는 모든 무게의 물을 그릇에 담아
#(X는 그릇에 담는 물의 무게 )

#out : 측정이 불가능한 물의 무게는 몇 가지?
'''
#--각각의 수(lst[idx])를 최대 한번씩만 사용해서 수를 만드는 경우 3개 --#
    1. 더하는 경우 dfs(idx+1, cur_sum + lst[idx])
    2. 빼는 경우 dfs(idx+1, cur_sum - lst[idx]) 
    3. 그냥 넘어가는 경우 dfs(idx+1)
-----------------------------------------------------------
조건
1. idx가 k되면 멈출 것(idx가3이면 -> 3가지 모두 사용했다는 것)
2. list에 어펜드할때 -> 범위를 맞출 것(0초과 s이하)

'''
def dfs(idx, cur_sum):
    if idx == k:
        if cur_sum > 0 and cur_sum <= s:
            prob_lst.append(cur_sum) 
        return 
    else:
        dfs(idx+1, cur_sum + lst[idx])
        dfs(idx+1, cur_sum - lst[idx])
        dfs(idx+1, cur_sum)
    
if __name__ == "__main__":
    #init
    cnt = 0
    prob_lst = []
    
    #input
    k = int(input()) #추의 개수 
    lst = list(map(int, input().split())) #추의 무게 리스트
    s = sum(lst) #가능한 최대 수 

    #op
    dfs(0,0)
    
    #print
    print(s - len(list(set(prob_lst))))
    
    
