#1 나이순으로 동그랗게 앉는다
#2시계방향으로 돌면서 1부터 시작해 번호를 외친다
#한 왕자가 k를 오치ㅣ면 그 왕자는 공주를 구하러 가지 않고  제외
#다음 왕자 부터 
n, k = map(int, input().split())
queue = [ i for i in range(1,n+1)]

cnt = 0
while len(queue) > 1:
    item  = queue.pop(0)
    queue.append(item)
    cnt+=1
    if cnt ==k:
        queue.pop()
        cnt = 0
        continue
print(queue)
    
     