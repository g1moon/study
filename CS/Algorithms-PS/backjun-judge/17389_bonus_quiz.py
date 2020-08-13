# 17389: 보너스 문제 
# https://www.acmicpc.net/problem/17389

#i번째 문제는 i점
#보너스 점수가 있다 이는 처음에 영점
#if 정답 -> bonus += 1
#elif 틀리면 -> bonus = 0 으로 초기화 
n = int(input())
board = input()

score = 0 
bonus = 0
for i in range(n):
    if board[i] == 'O':
        score += bonus + i+1
        bonus += 1
    else:
        bonus = 0
    
        
print(score)