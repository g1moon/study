# 볼링공 고르기 
'''
- (A,B) 두 사람은 볼링을 치고 있음
- 볼링공은 (총 N개), 공마다 무개가 적혀있음
- 공의번호는 1번부터 순서대로
- 같은 무게의 공이 여러개 -> 다른 공으로 간주
- 무게는 (1부터~M)

- 두 사람은 서로 무게가 다른 볼링공을 고르려 한다
'''

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

cnt = 0
for fir_idx in range(len(lst)):
    for sec_idx in range(fir_idx+1, len(lst)):
        
        if lst[fir_idx] < lst[sec_idx]:
            cnt += 1
            
print(cnt)