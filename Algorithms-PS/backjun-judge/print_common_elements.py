#중복확인하기 

listA = list(map(int, input('Enter list A numbers: ').split(' ')))
listB = list(map(int, input('Enter list B numbers: ').split(' ')))

common = []
for a in listA:
    if a in listB:
        common.append(a)

return_list = []

while common:
    item = common.pop()
    if item in common:
        pass
    else:
        return_list.append(item)

return_list.sort()
print(return_list)

        
