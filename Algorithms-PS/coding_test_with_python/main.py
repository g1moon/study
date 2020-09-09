'''
- (N*N)인 도시가 있다.
- 각 칸은 (빈칸, 치킨집)
- (r행, c열) , r과 c는 1부터시작
- 치킨거리 : 집과 가장 가까운 치킨집사이의 거리 , 
    -각각의 집은 치킨거리를 갖고있다
- 도시의 치킨 거리 : 모든 집의 치킨거리 

'''

from itertools import combinations

#input-----------------------
N, M = map(int, input().split())
mat = [ list(map(int, input().split())) for _ in range(N)]
#---------------------------
home_lst = []
store_lst = []
for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j] == 1:
            home_lst.append((i,j))
        elif mat[i][j] == 2:
            store_lst.append((i,j))

print(home_lst)
print(store_lst)

comb_lst = list(combinations(store_lst,M))
city_dist_lst = []
for comb_store_lst in comb_lst:
    city_dist = 0
    for home in home_lst:
        hx, hy = home[0], home[1]
        home_dist = 200000
        for store in comb_store_lst:
            sx, sy = store[0], store[1]
            new = abs(hx - sx) + abs(hy - sy)
            # print('new', new)
            home_dist = min(home_dist, new)
            # print(home_dist)
        #여기서 집1의 가장 가까운 home_dist가 나오고
        #이걸 city_dist에 업데이트해줘야해 
        city_dist += home_dist
    city_dist_lst.append(city_dist)
        
print(min(city_dist_lst))

