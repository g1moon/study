

v = int(input())
for i in range(1, (v//2)+1):
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
    for i in str(x):
        if i not in str(v):
            contain = False
            break 
        
    for j in str(y):
        if j not in str(v):
            contain = False
            break 
        
    if contain:
        print(v, ' is a vampire number.')
        break 
else:
      print(v, ' is not a vampire number.')
