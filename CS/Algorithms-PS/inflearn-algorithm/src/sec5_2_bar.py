#쇠막대기는 자신보다 긴 쇠막대기 위에만 (완점포함되고 끝점은 겹치지 않게->항상남아)
#각 막대기를 자르는 레이저는 적어도 하나씩은 있음
#레이저는 쇠막대기 끝을 쏘지 않음


#sol
#레이저가 나오면 팝하고 -> 개수체크
#
lst = list(input())
stack = []
ret = 0 

for i in range(len(lst)):
    if lst[i] == '(':
        stack.append(lst[i])
    else:
        #레이저
        if lst[i-1] == '(':
            stack.pop()
            ret += len(stack)
        #닫기(잘린거카운트)
        else:
            stack.pop()
            ret += 1
print(ret)
        