#hash table
#x가 하나의 y로 매핑이 되어야 함수라고 한다.
#f(x) = y 
#one key can be associated wuth one idx(0)
#one index can be associated with multiple keys (o)
    #1241231-> key:10 , 11111 -> key:10
    #이걸 해결해야함
    
#perfetc hash function : bijective fucntion(have to match one x : one y)
#but it is difficult so
#good hash fucntion : hash function resulting in a uniform distribution
#어느정도 일정하게 매핑되는 y엘리먼트에 두개씩... 10개 2개 1개 8개 가 아닌 -> bias

#hash fucntion
#modulo based hash function : divide a numeric key with a number
#(key % num)
#idx = key mod size(table
# 
#square based hash fucntion
#the problem of the modulo fucntion - under urilizing available information(일의자리수는 잘 
# 유틸라이징이 되는데 -> 앞 부분은 잘 안되는 점) 
#제곱을하고 일부 숫자만 사용 -ㅣ> 1239 면 23만 이용

#check sum
#1. sum all digit and apply modulo 

###################
#colision이 들어오면 좋지 않느데 이걸 처리해야
#Load factor
#load factor determine the perfomance of the hash table 
#얼마나 조밀하게 있나 -> 조밀하게 있으면 -> 콜리젼이 일어날 확률이 높은 
#Load factor = size of stored entries / size of the hash table 

#closed addressing : 동일한 인덱스에 같이 삻자 -> idx50에 링크드리스트로 연결
#최악의 상황 : 한 인덱스에 모두 -> 그냥 링크드 리스트임 
#idx : head of a linked list라고 생각하면 됨

#open addressing : 한 테이블에는 한 정보만
#-linear probing idx에 차있으면 idx+i로 바로 다음으로
#-quadatic probing : idx + i + i*2 (위 방법과 달리 점점 멀리감)
    #-콜리젼이 뭉쳐있는 구간이 있는데 조금씩 이동해봐야 그 부분의 복잡을 해결 할 수 없음
#open addressing에서의 문제는 삭제할떄 일어나는데 이 문제를 위해 삭제를 하지 않음
    #계속 찾아간느데 공백상태로 있으면 그 다음으로 넘어가지못해
    #그래서 그냥 지웠다고 마크만하고(lazy deletion) -> 다음에 더 큰 해쉬로 넘어갈때 삭제

#hash table size
#삭제는 할 수 없고 계쏙 데이터는 들어오는데 어떻게 할 거냐? -> 계속 로드 팩터는 증가될거임
#you need to extend the storage space 
#and insert the entires to new space with more-bucket
#다시 인설트해주는 과정 - re-hashing 




################ys#######################
#weight factor
#문자열은 ord값이 모두 같아 cat과 tac이 같은 걸 받을 수 있어서 웨이트를 줌
#ord(c) * 3 , ord()a *2 이런식으로

