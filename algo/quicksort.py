from random import randrange


def pivot(ipList,low,high):
    
    piv=randrange(low,high)
    swapindx=piv

    for i in range(low,high,1):
        if ipList[piv]<ipList[i] and i<piv:
            temp=ipList[piv]
            ipList[piv]=ipList[i]
            ipList[i]=temp
            piv=i
            swapindx=piv
        elif i>piv and ipList[piv]>ipList[i]:
            swapindx+=1
            temp=ipList[swapindx]
            ipList[swapindx]=ipList[i]
            ipList[i]=temp
            
    
    if swapindx!=piv:
        temp=ipList[piv]
        ipList[piv]=ipList[swapindx]
        ipList[swapindx]=temp
    
    return swapindx

def quicksort(ipList,low,high):
    
    if low<high:
        piv=pivot(ipList,low,high)
        quicksort(ipList,low,piv)
        quicksort(ipList,piv+1,high)

    return ipList

print(quicksort([5,4,3,2,1],0,5))
print(quicksort([5,4,3,2,1,1,5,3,9,12,15,2,3,5,8,9,10],0,17))