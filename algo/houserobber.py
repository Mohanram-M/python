'''
You are a professional robber plnning to rob houses along a street.Each house has certain amount of money stashed,
the only contraint stopping you from robbing each of then is that adjeacent houses have security systems connected 
and it will automaticaly contact the police if two adjecent houses wrer broken into the same night

given an integer array nums representing the
amount of money of each house, return the maximum amount of money you can rob to night

Example :

Input: hval[] = {6, 7, 1, 3, 8, 2, 4}
Output: 19

Explanation: The thief will steal 6, 1, 8 and 4 from the house.

Input: hval[] = {5, 3, 4, 11, 2}
Output: 16

Explanation: Thief will steal 5 and 11

Solve subproblems dynamic progrming approach
Time : O(n), Space: O(1)

'''

def findmaxLoot(ipList):

    n=len(ipList)

    if n==0: return 0
    elif n==1: return ipList[0]
    elif n==2: return max(ipList[0],ipList[1])
    else:
        loot1=ipList[0]
        loot2=max(ipList[0],ipList[1])

        maxloot=0
        for i in range(2,n):
            maxloot=max(ipList[i]+loot1,loot2)
            loot1=loot2
            loot2=maxloot
        
        return maxloot

print(f'1.--{findmaxLoot([6, 7, 1, 3, 8, 2, 4])}')
print(f'2.--{findmaxLoot([5, 3, 4, 11, 2])}')