#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
#the non-zero elements.

def moveZero(list1):
    i=0
    j=0
    while i<len(list1):
        if list1[i]!=0:
            if j!=i:
                list1[j]=list1[i]
            j+=1
        i+=1
    
    while j<len(list1):
        list1[j]=0
        j+=1
    
    return list1


def moveZero1(list1):
    i=0
    j=0
    for i in range(len(list1)):
        try:
            list1.remove(0)
            list1.append(0)
        except:
            print('xxxxx')
    return list1
        
print(moveZero([1,2,3,0,0,0,4,5,6,0,7,0,8,9]))

print(moveZero1([1,2,3,0,0,0,4,5,6,0,7,0,8,9]))