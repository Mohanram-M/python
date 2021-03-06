def merge(arr1,arr2):
    i,j=0,0
    merged=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    
    while i<len(arr1):
        merged.append(arr1[i])
        i+=1

    while j<len(arr2):
        merged.append(arr2[j])
        j+=1

    return merged
       
def sort(list1):
    if list1==None or len(list1)<2: return list1
    mid=len(list1)//2
    return merge(sort(list1[:mid]),sort(list1[mid:]))
    

    
print(sort([5,4,3,2,1,5,4,3,2,1]))