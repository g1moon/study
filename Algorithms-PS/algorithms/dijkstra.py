'''
#다익스트라 알고리즘
-하나의 정점에서 다른 모든 정점 간의 각각 가장 짧은 거리를 구하는 문제

#로직
- 첫 정점을 기준으로 연결되어 있는 정점들을 추가해가면 -> 최단거리 갱신
- BFS와 유사한 방법 
    - 첫 정점부터 각 노드간의 거리를 저장하는 배열을 만들고
    - 첫 정점의 인점 노드 간의 거리부터 먼저 계산
    - 첫 정점부터 해당 노드간의 가장 짧은 거리를 해당 배열에 업데이트
    
#우선순위 큐를 이용한 다익스트라(MinHeap)
1) 첫 정점을 기준으로 배열을 선언하여 -> 첫 정점에서 각 정점까지의 거리를 저장 
    - 초기 첫 정점 거리는 0 나머지는 inf
    - 큐에 (첫 정점, 거리0)만 먼저 넣음 
2) 우선순위 큐에서 노드를 꺼냄
    - 처음에는 첫 정점만 

'''

mygraph = {
    '0' : { '4': 2, '1':6, '5':5},
    '4' : {'0': 2, '1':1, '3':9, '6':4},
    '5' : {'0':8, '1':5, '3':7},
    '1' : {'4':1, '0':6 , '5':5, '2':3, '3':8},
    '2' : {'1':3, '3':1},
    '3' : {'6':3, '4':9,'1':8,'2':1,'5':7},
    '6' : {'4':4, '3':3}
}

import heapq 

mygraph = {
    '0' : { '4': 2, '1':6, '5':8},
    '4' : {'0': 2, '1':1, '3':9, '6':4},
    '5' : {'0':8, '1':5, '3':7},
    '1' : {'4':1, '0':6 , '5':5, '2':3, '3':8},
    '2' : {'1':3, '3':1},
    '3' : {'6':3, '4':9,'1':8,'2':1,'5':7},
    '6' : {'4':4, '3':3}
}


def dij(gr, start):
    tracker_dic = {node: [] for node in gr.keys()}
    dist_dic = { node: float('inf') for node in gr.keys()}
    dist_dic[start] = 0
    queue = []
    heapq.heappush(queue, [start, dist_dic[start]])
    
    while queue:
        cur_node, cur_dist = heapq.heappop(queue)
        if dist_dic[cur_node] < cur_dist:
            continue
        
        #cur_node와 연결된 정보
        for adj, weight in gr[cur_node].items():
            tmp_dist = dist_dic[cur_node] + weight #출발지에서 현재까지 + 다음곳으로
            
            #adj까지 가는데 -> tmp_dist가 더 짧으면
            if dist_dic[adj] > tmp_dist:
                dist_dic[adj] = tmp_dist
                if tracker_dic[adj]:
                    tracker_dic[adj] = []#비우고
                    tracker_dic[adj] = tracker_dic[cur_node]
                    tracker_dic[adj].append(cur_node)
                else:
                    tracker_dic[adj].append(cur_node)
                
                heapq.heappush(queue, [adj, dist_dic[adj]])
            
    return dist_dic, tracker_dic

a,b = dij(mygraph, '0')
print(a)
print(b)
    
    
    
    