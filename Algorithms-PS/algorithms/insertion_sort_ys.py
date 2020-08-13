#my selection sort 
def insertion_sort(lst):
    for idx in range(1, len(lst)):
        item = lst[idx]
        for sub_idx in range(idx-1, 0-1, -1):
            if lst[sub_idx] < item: ##<=
                lst[sub_idx+1] = lst[sub_idx] 
                lst[sub_idx+1] = item
                break
            else:
                lst[sub_idx+1] = lst[sub_idx]
        else:
            lst[0] = item
##########################################
def insertion_sort(lst):
    for idx in range(1, len(lst)):
        item = lst[idx]
        for sub_idx in range(idx-1, 0-1, -1):
            lst[sub_idx+1] = lst[sub_idx] 
            if lst[sub_idx] < item:
                lst[sub_idx+1] = item
                break
        else:
            lst[0] = item
             
# a_lst = [12,6,1,33,57,3,9,5,61,14]
# insertion_sort(a_lst)
# print(a_lst)            

#################################

def insertion_sort(lst):
    for idx in range(1, len(lst)):
        item = lst[idx]
        sub_idx = idx -1
        
        while sub_idx >= 0:
            lst[sub_idx+1] = lst[sub_idx]
            if lst[sub_idx] < item:
                lst[sub_idx+1] = item
                break
            sub_idx -= 1
        else: 
            lst[0] = item
        
         
        

###########################
def insertion_sort(lst):
    for idx in range(1, len(lst)):
        curr_val = lst[idx]
        pos = idx
        
        while (pos > 0) and (lst[pos-1] > curr_val):
            lst[pos] = lst[pos-1]
            pos -= 1
        lst[pos] = curr_val
        
a_lst = [12,6,1,33,57,3,9,5,61,14]
insertion_sort(a_lst)
print(a_lst)        
