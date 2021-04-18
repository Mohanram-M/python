# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.



def addString(str1,str2):

    num1,num2=0,0

    for i in str1:
        num1=num1*10+(ord(i)-ord('0'))

    for i in str2:
        num2=num2*10+(ord(i)-ord('0'))

    return str(num1+num2)    

print(addString('123','1234'))

print(addString('444','444'))
