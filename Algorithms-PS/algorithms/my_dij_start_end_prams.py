import heapq

# 탐색할 그래프와 시작 정점을 인수로 전달받습니다.
def dijkstra(graph, start, end):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대(inf)로 초기화합니다.
    # 조금 다른점은 이전에서는 {vertex : inf} -> {vertex : [inf, start]}
    distance_dic = {vertex: [float('inf'),start]  for vertex in graph}
    # 그래프의 시작 정점의 거리는 0으로 초기화 해줌
    distance_dic[start] = [0, start]
    # 모든 정점이 저장될 큐를 생성합니다.
    queue = []
    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue, [distance_dic[start][0], start])

    while queue:
        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트합니다.
        current_distance, current_vertex = heapq.heappop(queue)
        # 더 짧은 경로가 있다면 무시한다.
        if distance_dic[current_vertex][0] > current_distance:
            continue
    

        print(graph[current_vertex].items())
        print(f'current_distance = {current_distance}, current_vertex = {current_vertex}')
        #현재 vertex의 정보를 adj,weight를 가져온다
        for adj, weight in graph[current_vertex].items():
            print(adj, weight)
            distance = current_distance + weight
            print(f'distance = {distance}')
            
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
            if distance_dic[adj][0] > distance:

                # 거리를 업데이트합니다.
                #adj에서 current_vertex까지의 거리는 = distance
                distance_dic[adj] = [distance, current_vertex] #이 부분 확인
                heapq.heappush(queue, [distance, adj]) #이 부분 확인
        print(distance_dic)
        print(f'=========queue: {queue}')
        print('========================================================')
    
    path = end
    path_output = end + '->'

    #distance_dic['F'] 의 [6, 'E']에서 e를 찾아 가고 -> 찾아가고 ->

    while distance_dic[path][1] != start:
        print(path)
        path_output += distance_dic[path][1] + '->'
        path = distance_dic[path][1]
    path_output += start
    print (path_output)
    return distance_dic

# direction graph
#vertices is controlled by a priority queue(actuaaly in the code I used heapq from package)
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(mygraph, 'A', 'F'))
