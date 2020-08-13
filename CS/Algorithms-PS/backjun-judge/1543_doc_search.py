#1543번: 문서검색
#https://www.acmicpc.net/problem/1543

string = input()
word = input()
# string = 'ababababa'
# word = 'aba'

cnt = 0
while True:
    if word in string:
        cnt += 1
        start_idx = string.index(word)
        end_idx = start_idx + len(word) -1
        string = string[end_idx+1:]
        # print(start_idx, end_idx, string)
        continue
    break
print(cnt)
