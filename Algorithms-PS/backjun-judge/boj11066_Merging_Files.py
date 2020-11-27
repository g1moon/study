#boj 11066
#Merging Files

'''
- merges the files into one file in the order of the chapters for a new novel
- merge two file containing chapters into a new intermediate file, 
and keep merging the original files until he gets one final file 
cost = the size sum of the two files, 
# calculate the min cost to complete the final one file 
'''
def go(s,e):
    #같으면 0리턴하고
    if s == e:
        return 0
    #본 곳이면 디피 값 리턴하구 
    if d[s][e] != -1:
        return d[s][e]
    
    ans = d[s][e]
    cost = sum(lst[s:e+1])   #s~e
    for k in range(s, e): #s ~ e-1 
        tmp = go(s, k) + go(k+1, e) + cost
        #ans가 -1이거나, tmp가 더 작으면 갱신
        if ans == -1 or ans > tmp: 
            ans = tmp         
    
    d[s][e] = ans
    return ans 
    

#input
t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    d = [ [-1] * n for _ in range(n)]
    print(go(0, n-1))
    
    
#---------------------------------
# def go(i, j):
#     if i == j:
#         return 0
#     if d[i][j] != -1:
#         return d[i][j]
#     ans = d[i][j]
#     cost = sum(a[i:j+1])
#     for k in range(i, j):
#         temp = go(i,k) + go(k+1,j) + cost
#         if ans == -1 or ans > temp:
#             ans = temp
#     d[i][j] = ans
#     return ans

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int,input().split()))
#     d = [[-1]*n for _ in range(n)]
#     print(go(0,n-1))
    

    