'''
 insertion sort
'''

def insertionSort(list1):

    for i in range(1,len(list1)):
        key,swappos=list1[i],-1
        for j in range(i-1,-1,-1):
            if key<list1[j]:
                swappos=j
                list1[j+1]=list1[j]
            else:
                break
        if swappos!=-1:
            list1[swappos]=key
    return list1

print(insertionSort([5,4,3,2,1,5,4,3,2,1,1,1,2,3,4,10]))