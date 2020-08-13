#2480번: 주사위 세개
#https://www.acmicpc.net/problem/2480

#주사위 3개 상 받기 
#1. 같은 눈 3개면 -> 10000 + (같은눈)*1000
#2. 같은 눈 2개면 -> 1000 + (같은눈) * 100
#3. 모두 다른 눈 -> (가장큰눈 *100)

#같은 눈이 몇개인지 체크 
#딕셔너리로 돌면 서 다 키로 만들고
#개수 체크 
lst = list(map(int, input().split()))
dic = {k:0 for k in lst}

for i in lst:
    dic[i] += 1

# max(list(dic.keys()))

if len(dic) == 1:
    prize = 10000 + (list(dic.keys())[0]*1000)

elif len(dic) == 2:
    for k,v in dic.items():
        if v==2:
            prize = 1000 + (k*100)
elif len(dic) == 3:
    prize = max(list(dic.keys())) * 100
    
print(prize)