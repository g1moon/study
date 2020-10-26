'''
- 거스름돈을 가장 적은 수의 동전으로 교환 
- 동전은 무한정으로 사용 가능
- 거스름돈을 가장 적은 수의 동전으로 교환 


'''
import copy 

#input()
n = int(input()) 
lst = list(map(int, input().split())) #동전 리스트 
m = int(input()) #저슬러 줄 돈 
dy = [1000] * (m+1)
dy[0] = 0

for coin in lst:
    for i in range(coin, m+1): #코인값을 뺏을때 -> 음수가 되기 위함을 방지
        #i-coin은 코인을 사용했다는 것이니 -> +1
        #vs
        #그냥 현재 값 
        dy[i] = min(dy[i - coin] + 1, dy[i])
        
        
print(dy[m])

# #
# for money in range(1, m+1):
#     # print('money', money)
#     for coin in lst:
#         #빼서 음수라면 하지말고
#         if money - coin < 0:
#             # print(1)
#             continue 
#         #0이면은 뺴주고할다아하고
#         elif money - coin == 0:
#             dy[money] = 1
#             # print(2)
#             break 
#         #음수도아니고, 0도 아니면 -> 남은 거 더해줘 
#         else:
#             dy[money] = dy[money-coin] + 1
#             break 
            
# print(dy[-1])
        
    

    
            
        
    
    

