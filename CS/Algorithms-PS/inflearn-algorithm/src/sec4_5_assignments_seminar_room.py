#n개의 회읟르에 대해 // 회의실 사용표 
#회의들은 시작시간과 끝나는 시간 주어져있고 
#겹치지 않게하면서 최대 회의 
n = int(input())
lst = []
for i in range(n):
    d = input().split()
    lst.append((int(d[0]), int(d[1])))

lst.sort(key = lambda x : (x[1], x[0]))

start , end = lst[0]
cnt = 1

for s, e in lst[1:]:
    if s >= end:
        cnt +=1 
        start = s
        end = e
    
print(cnt)