
#n장의 카드 , 최대 m
a = input()
m = int(a.split(' ')[1])
n = int(a.split(' ')[0] )
in_list = a.split(' ')[2:]


max_num = 0

def f_max(list_):
    max_idx = 0
    for i in range(len(list_)):
        if list_[max_idx] < list_[i]:
            max_idx = i
    return max_idx 

def f_sum(list_):
    total = 0 
    for i in range(len(list_)):
        total = total + int(list_[i])
    return total

max_list = []

while True:
    # print(max_list, in_list)
    while len(max_list) < 3:
        item = in_list.pop(f_max(in_list))
        max_list.append(item)
        # print(max_list, in_list)
        if (len(max_list) == 3) and (f_sum(max_list) > m):
            # print('1')
            # print(f_sum(max_list))
            max_list.pop(0)
            continue
        
        elif (len(max_list)==3) and(f_sum(max_list) <= m):
            # print('2')
            # print(f_sum(max_list))
            break
    break

                
print(f_sum(max_list))
        
