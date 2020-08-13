in_list = input().split(' ')

ascending = True
descending = True
# print(in_list)
for i in range(len(in_list)-1):
    if int(in_list[i])+1 == int(in_list[i+1]):
        ascending = True
    else:
        ascending = False
        break
 
for i in range(len(in_list)-1):
    if int(in_list[i])-1 == int(in_list[i+1]):
        descending = True
    else:
        descending = False
        break


if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
