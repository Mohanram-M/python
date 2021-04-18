'''
SelectionSort
'''

def selectionSort(list1):

    for i in range(len(list1)-1):
        minpos=i
        for j in range(i+1,len(list1)):
            if list1[i]>list1[j]:
                minpos=j
        if minpos!=i:
            temp=list1[i]
            list1[i]=list1[minpos]
            list1[minpos]=temp
        else:
            break
    return list1

print(selectionSort([5,4,3,2,1]))