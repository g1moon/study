##
def short_bubble(lst):
    ckChange = True
    end = len(lst) - 1
    
    while ckChange and end > 0:
        for i in range(end):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                ckChange = True
        end -= 1
        
a_lst = [12,6,1,33,57,3,9,5,61,14]
short_bubble_sort(a_lst)
print(a_lst)








def short_bubble_sort(lst):
    exchanges =True
    pass_num = len(lst) -1
    
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if lst[i] > lst[i+1]:
                exchanges = True
                lst[i], lst[i+1] = lst[i+1], lst[i]
        pass_num -= 1












