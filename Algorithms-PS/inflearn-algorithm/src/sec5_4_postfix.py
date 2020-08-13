case = list(input())
def cal(num1,num2,mark):
    if mark == '*':
        return num1 * num2
    elif mark == '+':
        return num1 + num2
    elif mark == '-':
        return num1 - num2
    elif mark == '/':
        return num1 / num2    

lst = []
for i in range(len(case)):
    if case[i] in '123456789':
        lst.append(int(case[i]))
    else:
        b = lst.pop()
        a = lst.pop()
        lst.append(cal(a,b,case[i]))
        
print(int(lst[0]))
    