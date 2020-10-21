'''
-N개의 자연수로 이루어진 수열
-가장 길게 ㅈㅇ가하는 원소들의 집합을 찾아라 
-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
'''

N = int(input())
arr = list(map(int, input().split()))
lst = [0] * len(arr)

#0번쨰 인덱스를 마지막항으로하면 -> 길이는 1임
lst[0] = 1

# print(N)
# print(arr)
# print(lst)



#1번쨰를 마지막항으로 ~ 마지막을 마지막항으로
for last in range(1, N):
    res = 0 
    #0부터 마지막항 전까지 보면서 -> 작은 거 찾아
    for i in range(0, last):
        if arr[last] > arr[i]: #만약 현재값보다 더 작다면
            # print(arr[last],arr[i])
            res = max(res, lst[i]+1)
            
    if res == 0:
        lst[last] = 1
    else:
        lst[last] = res
    # print('----------------')
# print(lst)
print(max(lst))