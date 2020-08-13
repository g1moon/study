'''
- ck_lst, dis_lst 사이즈는 max보다 1 크게해서 index로 접근
- 출발지 큐에 넣고
    -체크
    -거리업데이트(0으로)
- queue에 있으면 계쏙 반복문 돌고
    - next를 cur에 -1, +1, +5 for문 돌면서 업데이트해주고
    - 범위에 맞으면(0~max) -> 
                -체크하고
                -큐에넣고
                -dis[nxt] = dis[now] + 1
'''

#init
MAX = 10000
queue = []
ck_lst, dis_lst = [0] * (MAX+1), [0] * (MAX+1)


#input
st, dst = map(int, input().split()) #출발, 도착

#
ck_lst[st] = 1
dis_lst[st] = 0
queue.append(st)

found = False
while queue:
    cur = queue.pop(0)
    if cur == dst:
        break 
    
    for nxt in (cur +5, cur-1, cur+1):
        if 0<nxt<=MAX:
            if ck_lst[nxt] == 0:
                queue.append(nxt)
                dis_lst[nxt] = dis_lst[cur] + 1
                ck_lst[nxt] = 1
                
                if nxt == dst:
                    found = True
                    break
        
    if found:
        print(dis_lst[dst])
        break 
    
    
    
    



 
    
    
    
    