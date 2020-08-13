import heapq

mygraph = {
    'A': {'B': 8, 'C': 7, 'D': 20, 'E':14},
    'B': {'D': 13},
    'C': {'E':5},
    'D': {'A':12},
    'E': {'A':11, 'D':6, 'F':4},
    'F': {'D': 10}
}

def my_dijkstra(gr, start):
    #distace_dic = 모두 inf로 맞춰주기
    distance_dic = {node: float('inf') for node in gr}
    #시작점을 0으로 맞춰주기
    distance_dic[start] = 0
    #queue를 선언하고, 시작점을 큐에 넣어주기[시작점의거리, 시작점]
    queue = []
    heapq.heappush(queue, [distance_dic[start],start])

    #queue가 없어질때까지 실행
    while queue:
        #현재 거리와, 노드 (a,0) 잡아주기 -> 큐에서 빼서
        current_distance, current_node = heapq.heappop(queue)
        #만약 이 거리가 현재 저장된 거리보다 길다면 -> continue
        if distance_dic[current_node] < current_distance:
            continue
        
        #반복문
        #뽑인 것 아이템 즉 인접 딕셔너리를 보면서 adj, weight로 
        for adj, weight in gr[current_node].items():
            #거리를 선언해주는데 -> 현재 거리에 지금 거리를 더해야해
            distance = current_distance + weight

            #만약 이 distance가 저장된 거 보다 더 짧다면 바꿔줘 -> 그리고 큐에 넣어[거리,노드]
            if distance < distance_dic[adj]:
                distance_dic[adj] = distance
                heapq.heappush(queue, [distance, adj]) #새로운 distance 넣어주기(더 짧음)
    return distance_dic

print(mygraph, '\n')
print(my_dijkstra(mygraph, 'A'))

