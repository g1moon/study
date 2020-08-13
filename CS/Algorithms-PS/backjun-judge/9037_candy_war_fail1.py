#9037: candy war
#https://www.acmicpc.net/problem/9037
#원으로 앉고, 사탕의 절반을 오른쪽 아이에게 
#if 홀수개의 사탕 가지면 -> 한개를 보충해 짝수로 
#결국 사탕 수 가 같아짐

#몇번의 순환을 거쳐야 같아지는가 
#단 맨처음에 홀수개의 사탕을 가지고 있으면 -> 선생님이 짝수로 보충해줌

#t -> test_case 개수 

def init_candy(lst):
    same = True
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            lst[i] += 1
    return lst

def check_same(lst):
    return len(set(lst)) == 1

t = int(input())
for _ in range(t):
    
    cnt = 0
    num_chd = int(input())
    
    lst = list(map(int, input().split()))
    if len(lst) == 1:
        print(0)
        continue
    else:
        lst = init_candy(lst)
    
    if check_same(lst):
        print(0)
        continue
    
    cnt = 0
    
    while True:
        half_lst = [ i//2 for i in lst]
        lst = half_lst
        
        new = [lst[0] + half_lst[-1]]
        for i in range(1, len(lst)):
            new.append(lst[i] + half_lst[i-1])
        
        lst = new
        if check_same(lst):
            print(cnt)
            break
        
        else:
            lst = init_candy(lst)
            cnt += 1
