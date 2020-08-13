#(N개의 문제)를 푼다 
#문제는 - 풀은 뒤 점수와 // 걸리는 시간이 주워짐 
#(제한시간 M)안에 (N개의 문제) 중 -> 최대점수를 얻을 수 있도록해야함 

#-> 해당시간이 걸리면 푸는 걸로 간주
#한 유형당 한개만 풀 수 있음 

'''
1. 현재 스코어 + 남은 스코어의 합(sum(score_lst[idx:])) < 현재 최고 스코어 -> 종료
2. 제한시간이 넘으면 -> 종료
3. idx == N -> 점수가 더 크면 -> res에 현재 s_score, s_time 등록 
'''
def dfs(idx, s_score, s_time):
    if s_score + sum(score_lst[idx:]) < res[0]:return  #1
    if s_time > M: return  #2
    if idx == N: #3 
        if s_score > res[0]:
            res[0] = s_score
            res[1] = s_time 
        return 
    else:
        dfs(idx+1, s_score + score_lst[idx], s_time + time_lst[idx])
        dfs(idx+1, s_score, s_time)
        
if __name__ == "__main__":
    #init
    score_lst, time_lst = [], [] 
    res = [-1000, 0]
    
    #input
    N,M = map(int, input().split())
    for _ in range(N):
        score, time = map(int, input().split())
        score_lst.append(score)
        time_lst.append(time)
    
    #op
    dfs(0,0,0)
    
    #print
    print(res[0])
        
        