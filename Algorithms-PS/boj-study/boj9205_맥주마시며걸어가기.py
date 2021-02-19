# https://www.acmicpc.net/problem/1389
# boj 1389 S1 맥주마시면서 걸어가기
# <메모리 : 123332, 시간 120>
'''
- 맥주 한 박스에 20개
- 50미터에 한 병씩 마셔야함 
- 편의점에서 빈병 버리고 새 맥주 살 수 있음, 그러나 20병 넘길 수 없어 
- (편의점, 상근이집, 페스티벌좌표) -> 

- t 테스트 캐스
'''
from collections import deque

t = int(input()) #테케
for _ in range(t):
    lst = []
    visited = []
    
    
    n = int(input())#편의점 개수
    start = tuple(map(int, input().split())) #집
    
    for _ in range(n):
        lst.append(tuple(map(int, input().split())))
    dest = tuple(map(int, input().split()))
    lst.append(dest)
    
    #
    done = False
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.pop()
        visited.append(cur)
        #lst에서 갈 곳이 있나 보고 -> 갈 수 있고, visited에 없는 거 
        for node in lst:
            dist = abs(cur[0]-node[0]) + abs(cur[1]- node[1])
            #만약 dist가 1000이하면 가능 
            if dist <= 1000 and node not in visited:
                if node == dest: 
                    done = True
                    break 
                queue.append(node)

        if done:
            print('happy')
            break 
        
    else:
        print('sad')
        
    
    
    
    
    
    
    
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
'''
- 플로이드 와샬(All pairs shortest path problem)
- (start -> dest) vs (start -> intermediation -> dest)
'''