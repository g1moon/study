#1920번 수 찾기
#https://www.acmicpc.net/problem/1920

#n개의 정수
#A[1]... A[N]

n = int(input())
a = {i: 1 for i in map(int, input().split())}
#a의 출력결과 {4: 1, 1: 1, 5: 1, 2: 1, 3: 1}

m = input() #무시

for i in list(map(int, input().split())):
    print(a.get(i,0)) #get을 쓰면 오류가 나지 않음

