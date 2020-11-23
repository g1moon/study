'''
- 수열 a가 주어졋을떄 가장 긴 증가하는 수열으 구해라
- last와 before를 이용해서 -> 직관적으로 쓰기 
'''

n = int(input())
lst = list(map(int, input().split()))
dp = [1] * n 

#초기화
dp[0] = 1

for last in range(1, len(lst)):
    for bef in range(last):
        #만약 더 작은 값이면 체크하고 갱신
        if lst[last] > lst[bef]:
            dp[last] = max(dp[last], 1 + dp[bef])

print(max(dp))