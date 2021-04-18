
# Given an array of integers, determine whether the array is monotonic or not.

def checkMonoton(arr1):
    return (all(arr1[i]>=arr1[i+1] for i in range(len(arr1)-1)) or all(arr1[i]<=arr1[i+1] for i in range(len(arr1)-1)))

print(checkMonoton([6,5,4,4]))
print(checkMonoton([1,1,2,3,4,5,6,7,1,2,3]))
print(checkMonoton([1,1,2,3,7]))