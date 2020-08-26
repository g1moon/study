
'''
n개의 숫자를 오름차순 -> n개중 한개인 m이 주어지면 ->
이분 검색으로 -> m이 어디에 있나 
'''

#input 
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)

start = 0
end = len(lst)-1

while start <= end: #lt + rt 
    mid = (end + start)//2
    if lst[mid] == m:
        print(m)
        break 
    #미드값이 찾는 값보다 더 큰 경우 -> 
    elif lst[mid] > m:
        end = mid-1 
    #미드값이 더 작은 경우 ->
    elif lst[mid] < m:
        start = mid + 1

print(mid)

#--------------------------