# 07 럭키 스트레이트 

'''
- 점수가 특정 조건을 만족할때만 사용
- (현재 캐릭터의 점수 N) 
- 자릿수를 기준으로 // 점수 N을 반으로 나눠 // 왼쪽 부분의 각 자릿수의 합과 == 오른쪽 

- 
'''
#input
n = input()
#123 456            (012)
l = len(n)
left = n[:l//2]
right = n[l//2:]

lsum, rsum = 0, 0 
for i in range(len(left)):
    lsum += int(left[i])
    rsum += int(right[i])

print(lsum)
print(rsum)

if lsum == rsum:
    print("Lucky")
else:
    print("Ready")