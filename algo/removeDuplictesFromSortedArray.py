'''
Remove Duplicates from sorted Array
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''


def removeDuplicates(nums):

    unqindx=0
    for i in range(1,len(nums)):
        if nums[i]!=nums[unqindx]:
            unqindx+=1
            if unqindx!=i:
                nums[unqindx]=nums[i]

    return unqindx


ar1=[1,1,1,2,2,3,4,5,6]

print('ipArr={0} opIndx={1} modArr={2}'.format(ar1,removeDuplicates(ar1),ar1))
ar2=[1,1,1,2,2,3,4,5,6]
print('ipArr={0} opIndx={1} modArr={2}'.format(ar2,removeDuplicates(ar2),ar2))

ar3=[1,1,1,2,2,3,4,4,4,5,6,6,6,7,8,10,10]
print('ipArr={0} opIndx={1} modArr={2}'.format(ar3,removeDuplicates(ar3),ar3))

ar4=[1,1,1,2,2,3,3,4,4,4,5,6,6,6,7,8,10,10,40]
print('ipArr={0} opIndx={1} modArr={2}'.format(ar4,removeDuplicates(ar4),ar4))

