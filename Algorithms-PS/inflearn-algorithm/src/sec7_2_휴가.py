#(N+1일)쨰 되는 날 휴가가기 위해 
#(남은 N일) 동안 -> 최대한 많은 상담 -> 많은 휴가비 

#상담을 (완료하는데 걸리는 날수 T) 
#(받을 수 있는 금액 P)

'''
1. 현재 날짜는 0일부터라고 생각 
2. dfs로 넘겨줄 때 그 날의 상담을 할 것이면 -> dfs(cur+상담소요일, sp+cur의 금액)로 넘겨주고 
  -> 상담을 안 할 경우면 dfs(cur + 1, sp)
3. cur > N -> N번쨰거를 더해? -> lst인덱스는 N-1까지 -> 그러므로 return 
4. lst 범위가 벗어나면 -> 걍 넘겨 -> 꺼버려 
5. 중간마다 sum_p가 계속 res보다 크면 갱신 
'''
def dfs(cur, sp):
    global res
    if cur > N: return  #3
    if sp > res: #5
        res = sp 
    
    #2 #4 
    try: dfs(cur + t_lst[cur], sp + p_lst[cur])     
    except: pass
    dfs(cur + 1, sp) #2
     
if __name__ == "__main__":
    
    #init
    res = -1000
    t_lst, p_lst = [], []
    
    #input
    N = int(input())
    for _ in range(N):
        t, p = map(int, input().split())
        t_lst.append(t)
        p_lst.append(p)

    #op
    dfs(0,0)
    
    #print
    print(res)