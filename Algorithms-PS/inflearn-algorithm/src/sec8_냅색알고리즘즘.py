n, m = map(int, input().split())
dy = [0] * (m+1) #0~m무게까지 #제한무게가 최대 idx의 무게일때 -> 담을 수 있는 가치 
for _ in range(n):
    w, v = map(int, input().split())
    for i in range(w, m+1):
        #현재 이 무게부터 ~ 맥시멈 무게까지 보면서
        #이거를 무조건 담는다 생각하고 -> 나머지 무게의 최대값을 업데이트 
        dy[i] = max(dy[i], dy[i-w] + v) 

print(max(dy))
        
    