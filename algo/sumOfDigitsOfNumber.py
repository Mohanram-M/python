
def sumOfDigits(num):
    absnum=abs(num)
    sumd=0
    while absnum>0:
        dig=absnum%10
        sumd+=dig
        absnum=absnum//10
    return sumd

print(sumOfDigits(12345))
print(sumOfDigits(123))
print(sumOfDigits(-123))
