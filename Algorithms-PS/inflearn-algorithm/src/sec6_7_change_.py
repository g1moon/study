#다음과 같이 여러 단위의 동전들이 주어져 있을 때 
#거스름돈을 가장 적은 수의 동적으로 교환해주려면... 
#어떻게 주면 되는가 ?
#각 단위의 동전은 무한정 쓸 수 있다. 
import sys
def dfs(cnt):
    global res 
    if res == money:
        print(cnt)
        return 
    
    if res > money:
        return 
    
    else:
        for i in range(n):
            dfs(cnt + 1)
            res += lst[i]

#첫 줄에는 도전의 종류 개수 N
#동전의 종류 
#거슬러줄 금액 M

if __name__ == "__main__":
    n = int(input())
    lst = list(map(int,input().split()))
    lst = sorted(lst, reverse = True)
    money = int(input())
    res = 0 
    dfs(0)
    
    