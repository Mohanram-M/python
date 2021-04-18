
class MinHeap(object):

    def __init__(self):
        self.heap=[]
        self.len=0;
    
    def insert(self,val):
        self.heap.append(val)
        self.len+=1
        self.bubbleUp()
    
    def bubbleUp(self):
        if self.len<2:
            return None
        else:
            nodepos=self.len-1
            parentpos=nodepos//2
            while nodepos>0 and self.heap[nodepos]<self.heap[parentpos]:
                temp=self.heap[parentpos]
                self.heap[nodepos]=self.heap[parentpos]
                self.heap[parentpos]=temp
                nodepos=parentpos
                parentpos=nodepos//2
            
    def sinkdown(self):
        if(self.len>2):
            nodeIndx=0
            while nodeIndx<self.len:
                leftchildIndx=2*nodeIndx+1
                rightchildIndx=2*nodeIndx+2
                swapindx=-1

                if leftchildIndx<self.len and self.heap[nodeIndx]>self.heap[leftchildIndx]:
                    swapindx=leftchildIndx
                
                if rightchildIndx<self.len and self.heap[nodeIndx]>self.heap[rightchildIndx] and (self.heap[leftchildIndx]>self.heap[rightchildIndx] or swapindx==-1):
                    swapindx=rightchildIndx

                if swapindx!=-1:
                    temp=self.heap[nodeIndx]
                    self.heap[nodeIndx]=self.heap[swapindx]
                    self.heap[swapindx]=temp
                    nodeIndx=swapindx
                else:
                    break

    def pop(self):
        minnode=None
        if self.len>0:
            minnode=self.heap[0]
            self.heap[0]=self.heap[self.len-1]
            self.heap.pop()
            self.len-=1
            self.sinkDown()
        return minnode