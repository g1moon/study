t = int(input())
def share_candy(lst):
    tmp_lst = [0 for i in range(len(lst)+1)] # 
    for i in range(len(lst)):
        # print(i+1 % len(lst))
        tmp_lst[i+1 % len(lst)] = lst[i] // 2
        
    for i in range(len(lst)):
        lst[i] = (lst[i]//2) + tmp_lst[i]
    
    return lst

def init_candy(lst):
    for i in range(len(lst)):
        if lst[i] % 2 ==1:
            lst[i] += 1
    return lst
    
    
def same_check(lst):
    if len(set(lst)) == 1:
        return True

def process():
    
    n =  int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    while 1:
        lst = init_candy(lst)
        if same_check(lst) == True:
            print(cnt)
            break
        
        else:
            lst = share_candy(lst)
            cnt += 1
        
        
for _ in range(t):
    process()