# 두 리스트 합치기
# 오름차순으로 정렬된 두 리스트 
# 합쳐서 오름차순 정렬 

input()
lst1 = list(map(int, input().split()))
input()
lst2 = list(map(int, input().split()))

lst = lst1 + lst2
lst.sort()
print(lst)