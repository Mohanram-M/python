import math

def countNumberOfDigits(num):
    absNum=abs(num)
    digits=0
    while absNum>0:
        absNum=absNum//10
        digits+=1

    return digits

def countnumberOfDigitsmath(num):
    if num>0:
        return math.floor(math.log10(abs(num))) +1
    else:
        return 0

print(countNumberOfDigits(123456))
print(countNumberOfDigits(4567))
print(countNumberOfDigits(0))

print(countnumberOfDigitsmath(123456))
print(countnumberOfDigitsmath(4567))
print(countnumberOfDigitsmath(0))
