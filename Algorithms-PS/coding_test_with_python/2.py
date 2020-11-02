
print('열번 찍어 안 넘어가는 나무 없다!!!')

# N = int(input())
N = 5
cnt = 0
for i in range((N*2)):
    cnt += 1
    p = '나무를 ' + str(cnt) + '번 찍습니다, ' + '콩, ' * cnt
    print(p[:-2])
