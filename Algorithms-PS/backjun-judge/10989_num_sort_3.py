import sys
n = int(sys.stdin.readline()) #더욱 빠름 
array = [0] * 10001 # 이 수는 10,000보다 작거나 같은 자연수

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001): #0~ 10000
    if array[i] !=0:
        for j in range(array[i]) #2번이면 두번 프린트 
        print(i)
