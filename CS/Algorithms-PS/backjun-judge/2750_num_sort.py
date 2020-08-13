n = int(input())
list_ = []
for _ in range(n):
    list_.append(int(input()))

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if list_[min_idx] > list_[j]:
            min_idx = j
    list_[i], list_[min_idx] = list_[min_idx] , list_[i]

for i in list_:
    print(i)


