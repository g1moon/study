class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj #root
        self.leftChild = None
        self.rightchild= None
        
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            #그부분에 레벨을 낮춘다.
            #새로운거에 -> 원래있던거 달아주고 -> 다시 바꿔주고 
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t    
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    #ck
    def setRootVal(self, obj):
        self.key = obj
        
    def getRootVal(self, obj):
        return self.key