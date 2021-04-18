import math

def numLen(num):
    if num>0:
        return (math.floor(math.log10(num))+1)
    else:
        return 0

def getDigit(num,pos):
    return ((num//pow(10,pos))%10)


def radixSort(ipList):
    maxlen=max(numLen(ip) for ip in ipList)

    for i in range(maxlen):
        bucket=[[] for i in range(10)]
        for j in range(len(ipList)):
            bucket[getDigit(ipList[j],i)].append(ipList[j])
        
        ipList=[j for b in bucket for j in b]

    return ipList

print(radixSort([10,9,9,8,7,6,20,5,4,3,1,188,0]))