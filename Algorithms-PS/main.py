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
if m > 0:
    broken = list(map(int, input().split()))#고장난 버튼 리스트 
else:
    broken = []

res = abs(n - 100)
# print(res)
for i in range(1000000):
    if res > abs(i - n):
        #i에 broken이 있는지 체크
        for i_unit in str(i):
            if int(i_unit) in broken:
                break 
        else:
            # print(i)
            res = len(str(i)) + abs(i-n)
print(res)

# n = int(input())
# m = int(input())
# broken = [False] * 10 
# if m > 0:
#     a = list(map(int, input().split()))
# else:
#     a = []