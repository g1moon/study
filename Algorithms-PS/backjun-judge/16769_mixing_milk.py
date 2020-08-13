#16769: mixing milk
#https://www.acmicpc.net/problem/16769

#3마리의 다른 소 우유 -> 크기가 다를 수 있는 버켓에
#그리고 완전히 다 차지 않았을 수 있음
#1를 2로 2를 3으로 
#3을 1로 -> 1을 2로 -> 2를 3으로  
#100번 부우면(아마 1에서 2로 갈거임) -> 
#부울 떄 가능한 많이  하나가 다 없어지거나, 하나가 다 차거나 
#plz tell farmer john now much milk will be in each bucket after he finishes all 
#100 p


cp1, amt1 = map(int, input().split())
cp2, amt2 = map(int, input().split())
cp3, amt3 = map(int, input().split())

c1 = [cp1, amt1]
c2 = [cp2, amt2]
c3 = [cp3, amt3]
###################
def b_to_b(fr, t):
    amt = fr[1]
    while True:
        if (fr[1] == 0) or (t[1] == t[0]):
            break
        
        if (fr[1] >= amt) and (t[0] >= (t[1] + amt)):
            fr[1] -= amt
            t[1] += amt
        else:
            amt = amt // 2
            if amt ==0:
                break
            
            



    

#####main ########
cnt = 0
while True:
    if cnt == 100:
        break
    b_to_b(c1, c2)
    cnt += 1
    
    if cnt == 100:
        break
    b_to_b(c2,c3)
    cnt += 1
    
    if cnt == 100:
        break
    b_to_b(c3,c1)
    cnt += 1

print(c1[1])
print(c2[1])
print(c3[1])
    

    
    
    
    