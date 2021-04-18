'''
Sorted Arry to Binary tree
'''

class Node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    

def sortedArrToBinTree(list1):

    if len(list1)<1: return None 
    else:
        mid=len(list1)//2
        if mid>0:
            node=Node(list1[mid])
            node.left=sortedArrToBinTree(list1[:mid])
            node.right=sortedArrToBinTree(list1[mid+1:])

    return node


def inorder(root):
    inorder=[]
    def traverse(node):
        if node!=null:
            traverse(node.left)
            inorder.append(node.value)
            traverse(node.right)

    traverse(root)
    return inorder
