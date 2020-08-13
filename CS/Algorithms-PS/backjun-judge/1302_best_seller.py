# 1302번: 베스트셀러
# https://www.acmicpc.net/problem/1302

#input : 하루동안팔린책의제목
#out : 가장 많이 팔린 책

n = int(input())
dic = {}
for _ in range(n):
    item = input()

    try: 
        dic[item] += 1
    except:
        dic[item] = 1 

sdic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
most_cnt= sdic[0][1]

best_seller_list = [] 
for k,v in dic.items():
    if v == most_cnt:
        best_seller_list.append(k)

if len(best_seller_list) != 1:
    best_seller_list.sort()
    print(best_seller_list[0])
else:
    print(best_seller_list[0])

