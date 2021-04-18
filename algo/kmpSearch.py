def lsp(pattern):    
    ls=[0]
    count=0
    i=1
    while i<len(pattern):
        if pattern[i]==pattern[count]:
            count+=1
            ls.append(count)
            i+=1
        elif count==0:
            ls.append(0)
            i+=1
        else:
            count-=1

    return ls

def kmpSearch(str1,pattern):

    ls=lsp(pattern)

    i,j=0,0
    foundindx=[]

    while i<len(str1):
        if str1[i]==pattern[j]:
            i+=1
            j+=1
        
        if j==len(pattern) and i<(len(str1)+1):
            foundindx.append(i-j)
            j=ls[j-1]

        if i<len(str1) and str1[i]!=pattern[j]:
            if j!=0:
                j=ls[j-1]
            else:
                i+=1
    
    return foundindx



print(kmpSearch('aaaaabcdefghdef','aa'))