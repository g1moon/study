#이분 검색
n, m = map(int, input().split())
lst = list(map(int, input().split()))

#n개의 수를 오름차순으로 정렬하고 -> 이분 검색으로 M을 찾는다
lst = sorted(lst)
print(lst)
start = 0
end = len(lst)-1

while start <= end:
    mid = (start + end)//2
    if lst[mid] < m: #m이 더 커 더 오른쪽에 있다
        start = mid + 1
    elif lst[mid] > m:
        end  = mid -1
    else:
        res = mid
        start = mid + 1
        
print(res+1)