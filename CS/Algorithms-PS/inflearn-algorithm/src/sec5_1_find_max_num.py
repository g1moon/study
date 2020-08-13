lst, n = map(int, input().split())
lst = list(map(int,list(str(lst))))
stack = [] #return 

#처음 작업
stack.append(lst.pop(0))
#스택의 맨 마지막 수와 비교해서(stack[-1]) // 들어갈 숫자(item= lst.pop(0))
#if stack[-1] < item:(아이템이 더 크다면) -> 
#stack.pop()해주고 , cnt += 1 해주고 // continue //
#그러다가 만약 작지 않다면(같다거나 stack[-1]이더 크다면) --> 종료

#반복문에서 cnt == n이 되면 종료 
#lst에 아이템이 없으면 종료
cnt = 0
while lst and cnt <= n:
    item = lst[0]
    if stack[-1] < item: #스택에서 빼버리고, 횟수 늘리고, 
        stack.pop()
        cnt += 1
    else:
        stack.append(item)
        lst.pop(0)
    
    if not stack: stack.append(item) ; lst.pop(0);
    if cnt == n: stack.extend(lst); break
         
# 종료가 되면 cnt가 전부 사용되었거나, 사용이 안 되었거나ㅣ
for _ in range(n-cnt):
    stack.pop()


print(''.join(list(map(str,stack))))
