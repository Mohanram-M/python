'''
Given a non-empty array of decimal digits representing a non-negative integer,
incrment one to the integer
The digits are stored such that the most significant
digit is the head of the list,each elemnt in the array contains a single digit.

you may assume the integer does not contain any leading zeros,except th number 0 itself

Time: O(n), Space: O(1)
'''

def plusone(iplist):

    for i in range(len(iplist)-1,-1,-1):
        if iplist[i]<9:
            iplist[i]+=1
            return iplist
        iplist[i]=0
    
    iplist.insert(0,1)
    return iplist

print(f'0--{plusone([0])}')
print(f'12345--{plusone([1,2,3,4,5])}')
print(f'12949--{plusone([1,2,9,4,9])}')
print(f'99999--{plusone([9,9,9,9,9])}')