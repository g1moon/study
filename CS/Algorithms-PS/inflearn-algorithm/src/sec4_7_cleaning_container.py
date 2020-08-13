#가장 높은 곳, 가장 낮은 곳이 여러개면 아무거나 선택해도 된다.
#높이 조정 : 가장 높은 곳에서 가장 낮은 곳으로 상자를 옮기는 것
#가장 높은 컬럼을 찾고(from) -1  -> 가장 낮은 컬럼을 찾고(to) + 1 
#m회 높이 조정 -> 가장 높은 곳과 가장 낮은 곳의 차이 

#딕셔너리로 처리하고 ->20번동안 반복문 높이 조정 함수 실행 -> 
a = input()
lst = list(map(int, input().split()))
m = int(input())

dic = {}
for i in range(len(lst)):
    dic[i] = lst[i]

###################################
def process():
    max_idx = lst.index(max(lst))
    min_idx = lst.index(min(lst))
    
    lst[max_idx] -=1
    lst[min_idx] += 1
    

for _ in range(m):
    process()

print(max(lst) - min(lst))


