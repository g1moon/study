must_str = input()

t = int(input())
########################################
def process():
    lst = list(input())
    must = list(must_str)
    for i in lst:
        if not must:
            return 'Yes'
        if i == must[0]:
            must.pop(0)
    print(must)
    if must:
        return 'No'
    else:
        return 'Yes'
        

#main######################################
idx = 1
for _ in range(t):
    print(idx, process())
    idx += 1
print('==========================')
    