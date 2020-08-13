# 첫번쨰 줄에는 동전의 종류 개수 
#동전의 종류 
#거슬러 줄 금액 
#각 동전은 100원을 넘기지 않음


#1. 만약 ㅇㄹㄴ
def dfs(idx, total):
    global ret 
    if idx > ret:
        return
    
    if total > money:
        return 
    
    if total == money:
        if ret > idx: 
            ret = idx 
        return 

    
    for i in range(N):
        if total > money:
            break
        dfs(idx+1, total + lst[i])
               
               
if __name__ == "__main__":
    ret = 1231313123123z
    # ret_ =  
    N = int(input())
    lst = list(map(int, input().split()))
    lst = sorted(lst, reverse = True)
    money = int(input())
    
    dfs(0,0)
    print(ret)
        