import heapq

def dij(gr, start, end):
    dist_dic = {node : [start, float('inf')] for node in gr.keys()}
    dist_dic[start] = [start, 0]
    queue = []
    # heapq.heappush(queue, [dist_dic[start][0], dist_dic[start][1]])
    heapq.heappush(queue, [start, 0])
    
    while queue:
        cur_node, cur_dist = heapq.heappop(queue)
        if dist_dic[cur_node][1] < cur_dist:
            continue 
        
        #cur_node와 연결되어잇는
        for adj, weight in gr[cur_node].items():
            tmp_dist = dist_dic[cur_node][1] + weight
            
            if tmp_dist < dist_dic[adj][1]:
                dist_dic[adj] = [cur_node, tmp_dist]
                heapq.heappush(queue, [adj, tmp_dist])
                

    
    res = [end]
    cur_node = dist_dic[end][0]
    res.append(cur_node)
    while True:
        nxt_node = dist_dic[cur_node][0]
        if nxt_node not in res:
            res.append(nxt_node)
        if nxt_node == start:
            break 
        cur_node = nxt_node
        
    
    return dist_dic, '->'.join(res[::-1])



if __name__ == "__main__":
    mygraph = {
        '0' : { '4': 2, '1':6, '5':8},
        '4' : {'0': 2, '1':1, '3':9, '6':4},
        '5' : {'0':8, '1':5, '3':7},
        '1' : {'4':1, '0':6 , '5':5, '2':3, '3':8},
        '2' : {'1':3, '3':1},
        '3' : {'6':3, '4':9,'1':8,'2':1,'5':7},
        '6' : {'4':4, '3':3}
    }

    
    for k in mygraph:
        a, b = dij(mygraph, '0', k)
        print(f'0에서 {k}까지의 최단 경로 : {b}\n최단거리:{a[k][1]}')
        print('-------------------------------------')
        
    
    
    
    
    
    
    
#------------------------
# import heapq

# def dij(gr, start, end):
#     dist_dic = { node :[start, float('inf')] for node in gr.keys()}
#     dist_dic[start] = [start, 0]
#     queue= [ [ dist_dic[start][0], dist_dic[start][1] ] ]
    
#     while queue:
#         cur_node, cur_dist = heapq.heappop(queue)
#         if dist_dic[cur_node][1] < cur_dist:
#             continue 

#         #만약 더 작은게 있으면
#         for adj, weight in gr[cur_node].items():
#             tmp_dist = cur_dist + weight
#             if dist_dic[adj][1] > tmp_dist:
#                 dist_dic[adj] = [cur_node ,tmp_dist] #cur노드에서 adj로 갓다
#                 heapq.heappush(queue, [adj, tmp_dist])
                
                
    
#     cur_vertex = dist_dic[end][0]
#     res = [end, cur_vertex]
#     while True:
#         nxt_vertex = dist_dic[cur_vertex][0]
#         if nxt_vertex not in res:
#             res.append(nxt_vertex)
#         if nxt_vertex == start: break 
#         cur_vertex = nxt_vertex
    
    
               
#     return dist_dic, '->'.join(res[::-1])

# if __name__ == "__main__":
#     mygraph = {
#         '0' : { '4': 2, '1':6, '5':8},
#         '4' : {'0': 2, '1':1, '3':9, '6':4},
#         '5' : {'0':8, '1':5, '3':7},
#         '1' : {'4':1, '0':6 , '5':5, '2':3, '3':8},
#         '2' : {'1':3, '3':1},
#         '3' : {'6':3, '4':9,'1':8,'2':1,'5':7},
#         '6' : {'4':4, '3':3}
#     }

    
#     for k in mygraph:
#         a, b = dij(mygraph, '0', k)
#         print(f'0에서 {k}까지의 최단 경로 : {b}\n최단거리:{a[k][1]}')
#         print('-------------------------------------')

           
    
    