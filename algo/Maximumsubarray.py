'''
Given an integer array nums, find the contigous subarray (containing atleast one number)
which has the largest sum and return its sum

ex 1: [-2,1,-3,4,-1,2,1,-5,4]
op : 6
Explanation :[4,-1,2,1] has the largest sum 6

ex 2: [1]
op :1

ex 3: [5,4,-1,7,8]
output: 23

1 <= nums.length <=3* pow(10,4)

try o(n) and devide n conqure approch..

The simple idea of Kadane’s algorithm is to look for all positive contiguous segments of the array
(max_ending_here is used for this). And keep track of maximum sum contiguous segment among all positive segments
 (max_so_far is used for this). Each time we get a positive-sum compare it with max_so_far and update max_so_far 
 if it is greater than max_so_far 
'''
import math
def findmaxsubarraysum(iparr):

    maxsofar= -maxint-1
    maxendinghere=0

    for i in iparr:
        maxendinghere+=i
        if maxsofar<maxendinghere:
            maxsofar=maxendinghere
        
        if maxendinghere<0:
            maxendinghere=0
    
    return maxsofar

