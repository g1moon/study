#적어도 하나의 루트는 있어야하니까
def BinaryTree(r):
    return [r, [], []]

#어떤 노드 아래 넣을 건지, 그리고 넣을 거
def insertLeft(root, newBranch):
    t = root.pop(1) #left꺼 뺴서
    
    if len(t) > 1:
        #아래거 내려서 넣어
        root.insert(1, [newBranch, t, [])
    else: #길이가 0 ->아무것도 없다면 -> 그냥 넣어
        #넣을떄는 레프트 라이트 만들어서
        root.insert(1, [newBranch, [], [])
    return root
    
def insertRight(root, newBranch):
    t = root.pop(2)
    
    if len(t) > 1:
        root.insert(2, [newBranch, t, []])
    else:
        root.insert(2, [newBranch, [], []])
    return root

#맨처음 값이 루트, 레프트, 라이트 
def getRootval(root):
    return root[0]
    
def setRootval(root, newVal):
    root[0] = newVal
    
def getLeftChile(root):
    return root[1]
    
def getRightChil(root):
    return root[2]
    