'''
first unique charecter
'''

def firstUniqueCharecter(str1):

    f={}
    for i in str1:
        f.setdefault(i,0)
        f[i]+=1
    
    for i in str1:
        if f[i]==1:
           return i
    return None

print(firstUniqueCharecter('abcdabd'))
print(firstUniqueCharecter(''))