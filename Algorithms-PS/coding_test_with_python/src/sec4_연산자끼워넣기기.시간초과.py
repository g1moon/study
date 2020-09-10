'''
- (N개의 수로 이루어진 수열 A1~AN)
- (N-1)개의 연산자 +,-,x,나
- 음수 // 양수 -> -(양수 // 양수)
'''

#---------------------------
def cal(str):
    lst = []
    for i in str:
        lst.append(i)
    
    res = int(lst.pop(0))
    while lst:
        c = lst.pop(0)
        num = lst.pop(0)
        
        if c == '+':
            res += int(num)
        elif c == '-':
            res -= int(num)
        elif c =='×': ########
            res *= int(num)
        elif c =='÷':##########
            if res < 0:
                res = -((-res)//int(num))
            else:
                res = res//int(num)
    return res 
#=-----------------------
#-----input()----------
N = int(input())
lst = list(map(int, input().split()))
cal_lst = list(map(int, input().split()))
from itertools import permutations

s = ''
s += '+' *cal_lst[0]
s += '-' *cal_lst[1]
s += '×'*cal_lst[2]
s += '÷'*cal_lst[3]

cal_lst = list(s)
prob_lst = list(permutations(cal_lst, len(cal_lst)))
# print(prob_lst)
min_num = 1e9
max_num = -1e9
for case in prob_lst: 
    op_lst = list(case)
    case_lst = []
    # print('--------------------')
    # print(lst)
    # print(op_lst)
    # print('--------------------')
    for i in range(len(lst)):
        if i == len(lst)-1:
            case_lst.append(lst[i])
            break
        case_lst.append(lst[i])
        case_lst.append(op_lst[i])

    new_str = ''.join(list(map(str,case_lst)))
    test_num = cal(new_str)
    
    # if test_num == -30:
    #     print('--------------')
    #     print(case)
    #     print(lst)
    #     print('-------------')
    min_num = min(min_num, test_num)
    max_num = max(max_num, test_num)
    
print(max_num)
print(min_num)
