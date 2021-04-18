'''
 * Given a Column title as appear in an excel sheet return its corresponding column number
 * 
 A Z AA AB AC....BCDA

 26^3 * 2 + 26^2 * 3 + 26^1 * 4 + 26^0 * 1

'''


def titleToNumber(title):
    return sum((ord(j)-ord('A')+1)*(pow(26,len(title)-1-i)) for i,j in enumerate(title))



print(titleToNumber("A"));
print(titleToNumber("Z"));
print(titleToNumber("AA"));
print(titleToNumber("AZ"));
print(titleToNumber("BCD"));