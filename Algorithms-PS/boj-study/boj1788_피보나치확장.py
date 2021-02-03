# https://www.acmicpc.net/problem/1003
# boj 1788 S2 (피보나치확장)
#<메모리 : 130060 / 시간 : 120 > 
'''
- 똑같이 피보나치 하는데 짝수고, 음수면 -> 음수 
'''
n = int(input())

if n == 0 or abs(n)==1:
    print(abs(n))
    print(abs(n))

else:
    dp = [0] * (abs(n)+1)
    dp[1] = 1
    for i in range(2, abs(n)+1):
        dp[i]= (dp[i-1] + dp[i-2])%1000000000
    
    if n < 0 and n % 2 == 0:
            print(-1)
    else:
        print(1)


    print(dp[abs(n)])
