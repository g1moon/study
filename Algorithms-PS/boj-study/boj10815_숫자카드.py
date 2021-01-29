# https://www.acmicpc.net/problem/10815
# boj 10815 숫자카드(S4)
'''
- 상근이는 숫자 카드 N개 
- 정수 M개가 주어졌을 떄 , 이 수가 있는 카드를 상근이가 갖고 있나?
'''

n = int(input())
sang_lst = list(set(map(int,input().split())))
sang_lst.sort()
m = int(input())
prob_lst= list(map(int,input().split()))

for i in prob_lst:
    s, e = 0, n
    while s <= e:
        cur = (s + e) // 2
        if (0 <= cur) and (cur < n): #범위내에 잘 있다면 
            if sang_lst[cur] == i:
                print(1, end = ' ')
                break
            if sang_lst[cur] < i:
                s = cur + 1
            else:
                e = cur - 1
        else:
            print(0, end =' ')
            break
    else:
        print(0, end =' ')
        