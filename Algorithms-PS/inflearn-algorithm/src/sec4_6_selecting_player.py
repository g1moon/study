#n명의 지원자
#다른 모든 지원자보다 키와 몸무게 중 적어도 하나는 큰 사람 뽑는다 

n = int(input())

lst = [tuple(map(int, input().split()))for i in range(n)]

candidate = lst[0]

lst.sort(key = lambda x: (x[0], x[1]), reverse = True)

cnt = 1
idx = 1

while idx <= len(lst)-1:
    ck = True
    for i in range(idx):
        if lst[idx][1] <= lst[i][1]:
            ck = False
    if ck:
        cnt += 1
        idx += 1
    else:
        idx += 1

print(cnt)
    
    
    