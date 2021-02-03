# https://www.acmicpc.net/problem/1003
# boj 1003 S3 (피보나치)
#<메모리 : 121220 / 시간 : 104 > 
'''
- fibo(3) 은 fibo(2) 와 fibo(2) 호출 
- fibo(4) 는 fibo(3)과 fibo(2) 호출 
 -> fibo(3) 값과 fibo(2) 값을 참고해 값 계산 
'''
t = int(input())
for _ in range(t):
    import sys
    input = sys.stdin.readline

    n = int(input())

    #양수
    if abs(n) == 0 or abs(n) == 1:
        print(abs(n))
        print(abs(n))


    else:
        dp = [abs(n)] * (abs(n)+1)
        dp[0], dp[1] = 0, 1
        for i in range(2, len(dp)):
            dp[i] = (dp[i-1] + dp[i-2])%1000000000
        
        if n < 0: print(-1)
        else:     print(1)
            
            
        print(dp[abs(n)])
    print('-----------------')

