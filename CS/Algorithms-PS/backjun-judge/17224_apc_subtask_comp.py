#17224번: APC는 왜 서브태스크 대회가 되었을까?
#https://www.acmicpc.net/problem/17224
#문제 먼저 읽기
#n=문제의 개수
#l= 역량
#k= 대회중에 풀 수 있는 문제의 최대개수
n, l, k = map(int, input().split())
score = 0
for i in range(n):
    easy, hard = map(int, input().split())
    if i+1 > k: #3번문제 3개까지풀수있음
        continue
    
    if hard <= l:
        score += 140
    elif easy <= l:
        score += 100
    else:
        pass
    # print(score)
    
print(score)