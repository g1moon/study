n = int(input())
lst = list(map(int, input().split()))

ret = []
lr =''
#num보다 크고 작은 거를 골라서 넣어주는 함수
a = min(lst[0], lst[-1])
if a == lst[0]: ret.append(lst.pop(0)) ; lr += 'L'
else: ret.append(lst.pop(-1)) ; lr+= 'R'

while lst:
    #a,b를 뽑고 -> 이 두개가 ret[-1]보다 크면 -> 길이 2일떄, 1일떄, 0일떄(중지)
    a,b = lst[0], lst[-1]
    #둘다 시도가능할때
    if a > ret[-1] and b > ret[-1]:
        min_num = min(a,b)
        if min_num == a:
            ret.append(lst.pop(0))
            lr += 'L'
        else:
            ret.append(lst.pop(-1))
            lr += 'R'
    #둘중 하나만 클때  
    elif a > ret[-1] or b > ret[-1]:
        biggerA = a > ret[-1]
        if biggerA:
            ret.append(lst.pop(0))
            lr += 'L'
        else:
            ret.append(lst.pop(-1))
            lr += 'R'
    else:
        break
print(len(ret))
print(lr)
    
    