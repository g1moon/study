'''
- 리모컨에는 0 ~ 9 , +, -
- + -> 채널 + 1
- - -> 채널 -1

- 만약 0에서 -를 누르면 -> 채널이 변하지 않음 -> pass
- 채널은 무한
- 지금 이동하려고 하는 (채널은 N) 

- 고장난 버튼이 주어졌을 떄 -> 채널N으로 이동하기 위해 -> 버튼 최소 몇번?
- 수빈이는 지금 채널 100
'''

#input()
n = int(input()) #target
m = int(input()) #고장난 버튼의 개수
broken = list(map(int, input().split()))#고장난 버튼 리스트 

ans = 0
lst = [ i for i in range(0,10) if i not in broken]
# print(lst)
res = [99] * len(str(n))

N = str(n) #strN
done = False
for i in range(len(N)):
    if done:
        break 
    if int(N[i]) in lst:
        res[i] = int(N[i])
    else: #N[i]의 차가 가장 작은것
        gap = 99
        for j in range(len(lst)):
            if gap > abs((int(N[i]) - lst[j])):
                gap = abs((int(N[i]) - lst[j]))
                res[i] = lst[j]
        #더크면 뒤는 리스트 제일 작은거로 모두 넣고
            if res[i] > int(N[i]):
                for k in range(i+1, len(N)):
                    res[k] = min(lst)
            #더작으면 -> 뒤는 리스트 제일 큰거로 모두 넣고
            else:
                for k in range(i+1, len(N)):
                    res[k] = max(lst)
            done = True
            break 
    
    
                
ans += len(res)
res = list(map(str, res))
res = ''.join(res)
# print(res)
ans += abs(int(res) - n)

#+,-만 했을떄 가능한지 확인
ans = min(ans, abs(100 - n))
print(ans)
            
# print('lst', lst)
