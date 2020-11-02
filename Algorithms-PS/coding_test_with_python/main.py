

v = int(input())
str_lst = [ i  for i in str(v)]
for i in range(1, (v//2)+1):
    str_lst = [ i  for i in str(v)]
    
    x = i 
    y = v // x
    
    #ck1
    if x * y != v:
        continue
    #ck2
    if len(str(x)) != len(str(y)):
        continue 
    #ck3
    if str(x)[-2:] == '00' or str(y)[-2:] == '00':
        continue 
    
    contain = True 
    
    for x_ in str(x):
        if x_ in str_lst:
            str_lst.pop(str_lst.index(x_))
        else:
            contain = False
    
    for y_ in str(y):
        if y_ in str_lst:
            str_lst.pop(str_lst.index(y_))
        else:
            contain = False
        
    if contain:
        print(v, ' is a vampire number.')
        break 
else:
    print(v, ' is not  vampire number.')
