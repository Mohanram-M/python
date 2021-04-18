'''
takes an unsigned integer and returns the number of 1 bits in it
'''

def getonebitscount(ipint):
    count=0
    while ipint>0:
        count+=ipint & 1
        ipint=ipint>>1
    return count

print(f'6---{getonebitscount(6)}')
print(f'9---{getonebitscount(9)}')
print(f'8---{getonebitscount(8)}')
print(f'23---{getonebitscount(23)}')

'''
Brian Kernighan’s Algorithm
subtract the number by one and and it with itself
this will unset the right most bit.and then flip all the bits from right most
so the number of loop execution will be the count
'''

def getonebitcountbk(ipint):
    count=0
    while ipint>0:
        count+=1
        ipint=ipint&(ipint-1)
    return count


print(f'bk 6---{getonebitscount(6)}')
print(f'bk 9---{getonebitscount(9)}')
print(f'bk 8---{getonebitscount(8)}')
print(f'bk 23---{getonebitscount(23)}')