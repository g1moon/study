# https://www.acmicpc.net/problem/2839
# boj 2839 B1 설탕 배달
# <메모리 : 121220 / 시간: 108>
'''
- N키로 배달해야햄
- 봉지는 (3키로짜리 5키로짜리)
- 최대한 적은 봉지 
'''
n = int(input())

if n % 5 == 0:
    print(n//5)
    
else:
    for i in range(n//5, 0-1,-1):
        #i = 5키로짜리 무게 
        remain = n - (5*i)
        
        if remain % 3 == 0:
            print(i + remain//3)
            break 
    #5로도 안 나눠지고 -> 3으로도 안 나누어짐    
    else:
        print(-1)
        
     
        
            
    

