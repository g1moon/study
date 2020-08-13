n = int(input())
rev = list(map(int, input().split()))
dic = {}
org = [False for _ in range(n)]
num_lst = [i for i in range(1, n+1)]

for i in range(1, n+1):
    dic[i] = rev[i-1]
    
#######################
while num_lst:
    num = num_lst.pop(0)
    cnt = -1 
    
    for i in range(len(org)):
        #있으면 넘어가고
        if org[i]:
            continue
        else: #없으면
            cnt += 1
            if cnt == dic[num]:
                org[i] = num
                break
            
print(' '.join(map(str,org)))
            
    