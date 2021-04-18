'''
Given the root of a binary tree, check whether it is a mirror of itself
(i.e, symetric around its centers)
Example 1 :
        i
    2       2
  3   4    4  3
  
  root= [1,2,2,3,4,4,3]
  output =true

'''

class Node(object):
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None


def checkSymetric(root):

    def comp(leftnode,rightnode):
        if leftnode!=None and rightnode!=None:
            if leftnode.value==rightnode.value:
                return (comp(leftnode.left,rightnode.right) and comp(leftnode.right,rightnode.left))
        elif leftnode==None and rightnode==None:
            return True
        return False
            
    return comp(root.left,root.right) 


n1=Node(1)
n2=Node(2)
n3=Node(2)
n4=Node(3)
n5=Node(3)
n6=Node(4)
n7=Node(4)

n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n6
n3.left=n7
n3.right=n5

print(checkSymetric(n1))

n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n6
n3.left=n5
n3.right=n7


print(checkSymetric(n1))