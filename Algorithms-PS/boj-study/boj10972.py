# https://www.acmicpc.net/problem/10972
# boj 10972 S3 다음순열 
# 진짜 뭐가 틀렸는지 모르겠네요 ㅜㅜ 반례를 못 찾겠어요...
'''
문제 요약
- 인덱스 두개로 맨뒤부터 하나 하나 앞 수와 비교해 -> 뒤에있는 수가 크면 바꿔주고
- 그 이후로 오름차순 정렬 
'''
n = int(input())
lst = list(map(int, input().split()))
ret = []
done = False
for i in range(len(lst)-1, 1-1, -1):
    for j in range(i-1, 0-1, -1):
        #만약 i가 더크면 바꾸고 -> 그 인덱스부터 정렬 
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
            ret = lst[:j+1] + sorted(lst[j+1:])
            done = True
            print(' '.join(list(map(str, ret))))
            break
    if done:
        break 
else:
    print(-1)

