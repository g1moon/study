# 1668번: 트로피 진열
# https://www.acmicpc.net/problem/1668


n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

# array = [5,1,1,2,1,1]

#왼쪽에서 보기
def solution(array):
    cnt = 1
    for i in range(len(array)-1):
        if array[i] >= array[i+1]: #같아도 보이지 않아요 주의!
            m = array[i]
            for j in range(i+1, len(array)): 
                if m < array[j]:
                    cnt +=1
                    m = array[j]
            # print(array[i])
            return cnt
        else:
            cnt += 1
    return cnt
print(solution(array))

reverse_array = []
for i in range(len(array)-1, -1, -1):
    reverse_array.append(array[i])

print(solution(reverse_array))

