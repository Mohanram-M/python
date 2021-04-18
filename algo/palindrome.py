'''
    Number is palindrome
'''

def checkPalidromeNum(num):
    absNum=abs(num)

    rev=0;
    while absNum>0:
        dig=absNum%10
        rev=rev*10+dig
        absNum=absNum//10
    
    if rev==num:
        print('number is a palindrome')
    else:
        print('number is not a palidrome')

checkPalidromeNum(11233211)
checkPalidromeNum(123)
checkPalidromeNum(1230321)

'''
string is a palindrome
'''

def checkPalindromeString(str1):
    strlen=len(str1)//2
    for i in range(strlen):
        if str1[i]!=str1[len(str1)-i-1]:
            return False
    return True


print(checkPalindromeString('abcdef'))
print(checkPalindromeString('abccba'))
print(checkPalindromeString('abcba'))
print(checkPalindromeString('aaaaa'))
