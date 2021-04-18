'''
Given an rray of integers nums and an integer target, return indices of the two numbers such that
they add up to target.
You may assume that each input would have exactly one solution and you may not use the same element twice
you can return the answer in any order
'''

#Bruteforce
#Time O(n^2) Space O(1)
def findTwoSumb(ipList,target):
    for i in range(len(ipList)-1):
        ele1 =ipList[i]
        for j in range(len(ipList)):
            ele2=ipList[j]
            if((ele1+ele2)==target):
                return (ele1,ele2)
    return (None,None)

#Hashng
def findTwoSumh(ipList,target):
    htable={}
    for i,j in enumerate(ipList):
        htable.setdefault(j,[])
        htable[j].append(i)

    for i in range(len(ipList)):
        compliment=target-ipList[i]
        if  compliment in htable and (len(htable[compliment])>1 or ipList[i]!=compliment):
            cmpIndx=-1
            for j in htable[compliment]:
                if j != i:
                    cmpIndx=j
                    break
            return (i,cmpIndx)
    
    return (None,None)

print('nums = [2,7,11,15], target = 9 : ans = {0}'.format(findTwoSumh([2,7,11,15], 9)))
print('nums = [3,2,4], target = 6 : ans = {0}'.format(findTwoSumh([3,2,4], 6)))
print('nums = [3,3], target = 6 : ans = {0}'.format(findTwoSumh([3,3], 6)))



