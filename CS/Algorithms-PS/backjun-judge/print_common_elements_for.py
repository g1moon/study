#중복확인하기 

str_listA = input('Enter list A numbers: ').split(' ')
str_listB = input('Enter list B numbers: ').split(' ')

listA = []
listB = []
for str_a in str_listA:
    listA.append(int(str_a))
for str_b in str_listB:
    listB.append(int(str_b))

common = []
for a in listA:
    if a in listB:
        common.append(a)

return_list = []

# while common:
#     item = common.pop()
#     if item in common:
#         pass
#     else:
#         return_list.append(item)

for item in common:
    if item in return_list:
        pass
    else:
        return_list.append(item)

return_list.sort()
print(return_list)
