#바이너리 힙 
#다이어그램하면 트리처럼 보이지만 사실 하나의 싱글리스트로 가능
#미니 힙: 스몰리스트 키 벨류가 항상 프론트에 있는거
#맥스 힙 :라지스트 키 벨류가 항상 프론트에 있는거
############

#build_heap : builds a new heap from a list of keys
#임의의 리스트를 힙의 구조로 바로 컨버팅
#즉 새로운 힙을 만든다 

#################
#BinHeap #항상 제일 작은게 루트에 있어 
#그래서 계쏙 제일 작은 값 삭제하면 -> 루트에서부터 빠져 
#이런 걸 잘 이용하면 소팅펑션도 구현할 수 있어. 
# 힙솔팅이라고 있어 

#힙의 특징############
#리스트에서 0인덱스를 쓰지않음 걍 0넣어줌 
############################3
#> 1개, 2개, 4개, 8개 .... 
#1. 스트럭쳘 프로퍼티: ###########
# 컴플리트한 바이너리 트리가 돼야함 -> 발란스되어있어야해
#최대 2개의 칠드런을 가지는 걸 바이너리-> 컴플리트한 바이너리 트리는 모두 2개만
#가져야하고 맨 마지막 레벨거는 하나만 있어도 됨, 그러나 레프트 투 라이트의 오더로 
#채워져있어야함 

#바이너리 힙은 싱글리스트르로 구현 가능해 왜냐하면 힙의 스트럭쳐가 컴플릿해서 
#노드 레퍼런스 . 리스트 오브 리스트 안 씀
#컴플릿한 트리는 항상 차일드를 2개씩 풀로 가져야함 
#인덱스 1부터 넣는다고 하면 -> 어떤 특정 노드의 레프트 차일드는 컴플릿하니까
#2곱하기 p 인덱스에 위치행있음 -> 
#그러니까 라이트 차이들은 2곱하기 p인덱스 + 1

#4,5에대한 페어런트는 4와 5를 // 2했을때에 위치해있음 
#정리
#1. 부모 포지션 p의 레프트 차일드는 항상 2p에 있음 -> 
#2/ 라이트 차일드는 2p + 1에 있음 
#3. 포지션 n의 포지션은 n//2에 있음
##################################
#2.오더링 프로퍼티 
#페어런츠는 항상 작거나 같아야한다 자식보다.
####################################

#엠티 바이너리 힙이 싱글 제로를 퍼스트 엘레먼트로 가져있음
#왜냐하면 트레버스 할때 스트럭쳐 프로퍼티에서 얻을 수 있는 이점을 살리기위해
# 
class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0 #인덱스 0을 무시 
        
    #가장효율적인 인서트는 어펜드로.. 이러면 근데 오더링프로퍼티가 깨짐
    #넣고 페어런츠랑 비교하고 -> 만약 부모가 더 작아 -> 스왑 ->
    #그리고 만족할 때 까지 스왑 percolating
    #i = 현재노드 인덱스
    #계속 위에거랑 비교하면서 올라가는거 
    def perc_up(self, i):
        while i// 2 > 0:
            #부모가 더 크니까 바꿔줘야지
            #부모가 자식이되고, 자식이 부모가 되게 
            if self.heap_list[i] < self.heap_list[i//2]:
                tmp = self.heap_list[i//2]
                self.heap_list[i//2] = self.heap_list[i]
                self.hea_list[i] = tmp
            #아니면
            i = i //2 
    
    
    def insert(self,k):
        self.heap_list.append(k)
        self.current_size += 1
        #사이즈로, 현재의 비교해야하는 위치 
        self.perc_up(self.current_size) 
                
    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.hea_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        #맨 마지 막 걸 루트로 옮겨줌 
        self.perc_down(1) #루트 포지션(1) 부터 시작
        return ret_val
    
    def perc_down(self, i):
        #레프트 차일드가 현재 사이즈보다 작거나 같을때만 
        #그니까 레프트 차일드가 -> 현재 크기 넘어가면 중단 
        while (i * 2) <= self.current_size:
            mc = self.min_child(i) #두개중에 작은 인덱스 값을 리턴
            #현재값(부모)이 차일드 보다 더 커 -> 그러면 바꿔줘야지 ->
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc #i값을 아래로 내려줌.             
                
    def min_child(self, i):
        #오른쪽이 현재 사이즈보다 더 커 -> 왼쪽만 있어 -> 왼쪽 리턴
        if i * 2 + 1  > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.hea_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    
    #########효과적 #############
    #위 방법보다 (엔로그엔 vs 로그엔 ) 효과적 
    #######################33
    def build_heap(self, a_list):
        i = len(a_list) // 2 #중간 인덱스부터 찾아서(레벨이 2까지있으면 중간부터(3개짜리))
        self.current_size = len(a_list) #현재 사이즈 잡아주고
        self.heap_list = [0] + a_list[:] #새로운 힙 리스트를 만들어주고
        #중간부터 퍼콜레이팅 그러면서 하나씩 올려주고 루트노드 i==1에 오면 중단 
        while i > 0: 
            self.perc_down(i)
            i = i - 1  
        
    
            
    #그래도 퀵소트가 가장 빠르다 !!
    #그런데 힙을 어디에 사용할까 그럼 ?
    #priority queue
    #인서트와 델리트로 인큐 디큐하는데
    #큐랑 비슷한데 로지컬 오더가 다르다 
    #각아이템별로 프라이어티를 갖고 -> 그거의 순서에따라 디큐가된다
    #바이너리 힙에서는 인큐디큐로 로그엔,  인서트소팅은 엔로그엔 

    
        
    