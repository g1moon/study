def solution(number, k):
    answer = ''
    stack = [int(number[0])]
    
    for i in range(1, len(number)):
        num = int(number[i])
        stack.append(num)
        while True:
            if k == 0 or len(stack) < 2:
                break 
            
            #k도 0보다 크고(뺄 수 있고) , 스택의 길이도 2개이상 (비교가능)
            if stack[-2] >= stack[-1]: #뒤에있게 더 크거나 같은 상태
                break 
            else:#앞에있는게 더 커서 -> 바껴야하는 상태(k는0보다크고, 길이도있음)
                stack[-2] = stack[-1] 
                stack.pop()
                k -= 1
                
    #다 돌았는데도 k가 남아있는경우 -> 처리해주기 
    if k != 0:
        for _ in range(k):
            stack.pop()
    
    ans = ''.join(list(map(str, stack)))

            
                
    
    return ans
