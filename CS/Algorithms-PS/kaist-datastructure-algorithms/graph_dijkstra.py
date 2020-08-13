class DenseGraph:
    vertexes = []
    edges = {}
    
    def __init__(self):
        self.vertexes = []
        self.edges = {}
        
    def addVertex(self, vertex):
        self.vertexes.append(vertex)
        self.edges[vertex] = {} #딕셔너리에 웨이트 값을 넣을 딕셔너리 
        
    def addEdge(self, src, dst, weight, directed):
        if directed == True:
            self.edges[src][dst] = weight
        else:
            self.edges[src][dst] = weight
            self.edges[dst][src] = weight
    
    def getNeighbors(self, vertex):
        retNeighbor = []
        retWeight = []
        
        for key in self.edges[vertex].keys():
            retNeighbor.append(key)
            retWeight.append(self.edges[vertex][key])
            
        return retNeighbor, retWeight
    
    def getWeight(self, src, dst):
        return self.edges[src][dst]

######################
# dijkstra(v, w, s) 
#v = the set of vertex
#w = the set of weights on edges
#s = the source vertex
# dist = {}
# for itr in V:
#     dist[v] = 99999
# dist[s] = 0
# while size(V) !=0:
#     #retrieving minimum distance from a list. does that ring a bell
#     #거리가 제일 작은 거 찾고, 그거 지우고, 그거의 이웃들을 돌면서 가장 작은 거  업데이트
#     u = getVertexWithDistance(V, dist)
#     V.remove(u)
    
#     for neightbor in getNeighbors(u):
#         if dist[neightbor] > dist[u] + w(u.neightbor)
#############################
def performDijkstra(graph, src, dst):
    #dist와 path를 모두 딕셔너리로 선언해주고
    #방문해야할 것을 담는 리스트 : Vertexes를 선언
    dist = {}
    path = {}
    Vertexes = []
    
    #그래프의 모든 버텍스정보의 키를 가져와서 무한대값으로 세팅
    for vertex in graph.vertexes:
        dist[vertex] = 999999
        Vertexes.append(vertex)
    #초기값 0으로 세팅
    dist[src] = 0
    #버텍스에 남아있으면 계쏙 돌아
    while len(Vertexes) != 0:
        #초기값 세팅
        minDist = 999999 
        min_vertex = None 
        #만약 현재 거리가 최저값보다 낮다면 -> 갱신
        for vertex in Vertexes:
            if dist[vertex] < minDist:
                min_vertex = vertex
                minDist = dist[vertex] 
        #더작은게 없으면 종료   
        if minDist = 999999:break
        #들렸으니까 삭제 
        Vertexes.remove(min_vertex)
        #이웃값 얻어주고 
        neighbors, weights = graph.getNeighbors(min_vertex)
    
        for itr in range(len(neighbors)):
            #dist에서 네이버 길이 다 보고 -> 최저버텍스랑+현재 거리 해서 더 낮으면 갱신
            if dist[neighbors[itr]] > dist[min_vertex] + weights[itr]:
                dist[neighbors[itr]] = dist[min_vertex] + weights[itr] #
                #그런다음에 현재 보고있는게 어느 버텍스에서 온건지 적어줌
                path[neighbors[itr]] = min_vertex
                
        #역추적
        course = dst
        next = dst
        while next != src:
            next = path[next]
            course = next + '->' + course
            
        return dist, path, course