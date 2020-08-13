import Node from node_kaist 

class SinglyLinkedList:
    nodeHead = ''
    nodeTail = ''
    size = 0
    
    def __init__(self):
        #테일먼저 잡아주고 연결
        self.nodeTail = Node(blnTail =True)
        self.nodeHead = Node(blnHead = True, nodeNext = self.nodeTail)
        
    def insertAt(self, objInsert, idxInsert):
        nodeNew = Node(objValue = objInsert)
        #idxInsert-1 에 prev를잡고
        nodePrev = self.get(idxInsert-1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1
    
    def removeAt(self, idxRemove):
        nodePrev = self.get(idxRemove-1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size -1
        return nodeRemove.getValue()
    
    #헤드를 잡아주고 
    def get(self, idxRetrieve):
        nodeReturn = self.nodeHead
        for itr in range(idxRetrieve +1):
            nodeReturn = nodeReturn.getNext()
            return nodeReturn 
        
    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue(), end='')
        print('')
        
    def getSize(self):
        return self.size
        
        
        
        
    