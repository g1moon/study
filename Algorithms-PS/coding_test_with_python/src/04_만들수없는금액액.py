#만들 수 없는 금액
'''
- n개의 동전을 가지고 있고
- 만들 수 없는 양의 정수 금액중 최솟값 
- 1원 부터 sum(lst)원 까지 

'''
#input
n = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst)

target = 1 #1원을 만들 수 있는지 체크 

for idx in range(len(lst)):
    if target < lst[idx]:
        break
    target += lst[idx]
    
print(target)