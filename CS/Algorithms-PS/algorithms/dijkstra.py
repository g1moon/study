import heapq
op = True #특이사항 관리

###############함수 정의#####################################
# 탐색할 그래프와 시작 정점을 인수로 전달받습니다.
def dijkstra(graph, source, destination):
    try:
        # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대(inf)로 초기화합니다.
        dist = {node: [float('inf'), source] for node in graph}
        # 그래프의 시작 정점의 거리는 0으로 초기화 해줌
        dist[source] = [0, source]
        # 모든 정점이 저장될 큐를 생성합니다.
        queue = []
        # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
        heapq.heappush(queue, [dist[source][0], source])

        while queue:
            # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트합니다.
            crr_distance, crr_node = heapq.heappop(queue)
            # 더 짧은 경로가 있다면 무시한다.
            if dist[crr_node][0] < crr_distance:
                continue
                
            for adjacent, weight in graph[crr_node].items():
                distance = crr_distance + weight
                # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
                if distance < dist[adjacent][0]:
                    # 거리를 업데이트합니다.
                    dist[adjacent] = [distance, crr_node]
                    heapq.heappush(queue, [distance, adjacent])
        
        path = destination
        path_out = destination + ','
        while dist[path][1] != source:
            path_out += dist[path][1] + ','
            path = dist[path][1]
        path_out += source
        return dist, path_out
    
    except:
        print('경로를 찾는데 문제가 있습니다.')

def str_reverse(string):
    reversed = ''
    for i in range(len(string)-1, -1,-1):
        reversed += string[i]
    return reversed


#################################################
f = open('graph_input.txt', 'r')
data = f.readlines()
dic = {}
arr= []
for d in data:
    a = d.replace('\n','').split('\t')
    #특이사항: 노드 이름 중간에 띄어쓰기가 있는 경우 처리
    a = list(map(lambda x: x.strip(), a))
    arr.append(a)
f.close()
####################################
dic = {}
for i in range(1, len(arr)):
    if int(arr[i][2]) < 0:
        #특이사항 : edge가 음수인 경우
        print('edge의 weight가 음수입니다.')
        op = False
    try:
        d = dic[arr[i][0]]
        d[arr[i][1]] = int(arr[i][2])
    except:
        # pass
        dic[arr[i][0]] = {}
        d = dic[arr[i][0]]
        d[arr[i][1]] = int(arr[i][2])


mygraph = dic
#############################
source = arr[0][0]
#특이사항 : source node에 해당하는 것이 graph에 존재하지 않는경우
if source not in list(mygraph.keys()):
    print('source node에 해당하는 것이 graph에 존재하지 않습니다.')
    op = False

if op:
    F = open('20162673.txt', 'w')
    done = []
    try:
        for i in range(1,len(arr)):
            destination = arr[i][1]
            lenghth, shortestPath = dijkstra(mygraph, source, arr[i][1])
            shortestPath = str_reverse(shortestPath)
            
            if (destination in done) or (destination == source):
                continue
            print('%-10s%-10s%-15s%-10s' % (source, destination,
                                            shortestPath,
                                            lenghth[destination][0]))
            txt = '%-10s%-10s%-15s%-10s\n' % (source, destination,
                                            shortestPath,
                                            lenghth[destination][0])
            done.append(destination)
            F.write(txt)

    except:
        pass

F.close()
