# https://www.acmicpc.net/problem/9251
# boj 9251 G5 (LCS)
# <메모리 : 131044 / 시간: 140>
'''
- LCS(i,j) = Xi 과 Yj의 LCS길이 
- LCS(i,j) = case1 ( Xi = yi ):
                -> LCS(i-1, j-1) + 1
                -> 두 문자열에서 마지막이 같다면?
                -> 무조건 추가해주는게 좋으니까
                
             case2 (Xi != Yi)
                -> max(LCS(i-1, j), LCS(i, j-1))
                -> 맨뒤가 다르면 
                    str1의 맨 뒤 문자가 추가되거나->str2 끝 볼 이유 없음
                    str2의 맨 뒤 문자가 추가되거나->str1 끝 볼 이유 없음
'''
str1 = input()
str2 = input()

dp = [[0]*(len(str1)+1) for _ in range(len(str2) +1)]
res = [] 
for x in range(1, len(str2)+1):
    for y in range(1, len(str1)+1):
        #같으면
        if str1[y-1] == str2[x-1]:
            dp[x][y] = dp[x-1][y-1] + 1
            res.append(str1[y-1])
        #다르면 
        else:
            dp[x][y] = max(dp[x-1][y], dp[x][y-1])
print(dp[-1][-1])
