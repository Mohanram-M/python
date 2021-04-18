
'''
nth largest number
'''

def nthLargestNuber(list1,n):
    if len(list1)>=n :
        list1.sort()
        return list1[n-1]
    else:
        return None

    

print(nthLargestNuber([1,5,4,3,1,3,5,7,9],4))
print(nthLargestNuber([1,5,4,3,1,3,5,7,9],20))