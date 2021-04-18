def reverse(num):
    absnum=abs(num)
    revNum=0
    while absnum>0:
        dig=absnum%10
        revNum=revNum*10+dig
        absnum=absnum//10
    
    if num<0:
        revNum=-revNum
    return revNum

print(reverse(12345))

print(reverse(-12345))