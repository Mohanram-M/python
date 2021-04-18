
def bubblesort(list1):

    for i in range(len(list1)-1,-1,-1):
        swaped=False
        for j in range(i):
            if list1[j]>list1[j+1]:
                temp=list1[j+1]
                list1[j+1]=list1[j]
                list1[j]=temp
                swaped=True
        if not swaped:
            break
    return list1

print(bubblesort([5,4,3,2,1,5,4,3,2,1]))