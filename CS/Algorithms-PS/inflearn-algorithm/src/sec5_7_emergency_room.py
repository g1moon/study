#환자가 접수한 순서대로의 목록에서 제일 앞에 있는 환자목록 꺼냄
#위험도가 높은 환자가 존재하면 -> 대기목록 제일 뒤로 넣고, 
#없으면 -> 진료를 받아 

#제일처음은 0
N,M = map(int, input().split())
lst = list(map(int,input().split()))
queue = [ [i,False] for i in lst]
queue[M][1] = True

def ck(num):
    for q, _ in queue:
        if q > num:
            return False
    return True

#이게 가장 크면(ck(item[0])) ->cnt += 1 -> item[1]==True면 break// 뽑고 ->  -> 
#가장 큰게 아니면 pop(0)해서 뒤로 append
cnt = 0
while queue:
    item = queue[0]
    if ck(item[0]):
        cnt += 1
        if item[1]:
            break
        else:
            queue.pop(0)        
    else:
        queue.pop(0)
        queue.append(item)
        # print(queue)
    
print(cnt)

    
