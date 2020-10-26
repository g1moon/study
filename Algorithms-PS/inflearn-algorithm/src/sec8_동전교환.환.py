#input()
N = int(input())
lst = list(map(int, input().split()))
m = int(input())
dy = [100000] * (m+1)
dy[0] = 0
for coin in lst:
    for i in range(coin, m+1):#coin ~ m
        dy[i] = min(dy[i], 1 + dy[i - coin])

print(dy[m])
        