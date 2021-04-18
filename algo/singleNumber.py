'''
    Single Number With Duplicates Appearing Twice
'''

def findSingleNumber(list1):

    j=0;
    for i in list1:
        j=j^i
    return j

print(findSingleNumber([1,2,3,1,2,3,4]))

'''
    Single number with Duplicates Appearing N times

    twice =twice | once and x
    once = once ^ x
    notthrice = ~ (once & twice)
    once = once & notThrice
    twice= twice & notThrice

'''


        
