#serch procedure
#cannot use index -> so use next instead of index

#1. 헤드를 리스트에서 찾고 
#2 넥스트 노드를 찾는다 (이게 만약 테일이면 -> break)
                    #아니면 nex.obj == val 이면 종료
                    #아니면 nex.nex.node를 찾는다 



#insertion 
#see the power of a linked list
#어디에 넣고 싶은지는 알아야해
#node_prev.next = node_new 
#node_new.next = node_next


#remove
#node_remove = node_prev.next
#node_next = node_prev.next.next

