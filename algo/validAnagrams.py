'''
 * Check for valid Anagram
 *
 * Input : anagram , nagaram 
 * Output : true
 *  
 * Input : cat , rat
 * Output : flase
 */


 /*
 *  TIME O(n) space O(n)
 */
 '''

def isAnagram(str1,str2):

    if str1 is None or str2 is None or len(str1)!=len(str2):
        return False

    temp={}
    for i in range(len(str1)):
        temp.setdefault(str1[i],0)
        temp.setdefault(str2[i],0)
        temp[str1[i]]+=1
        temp[str2[i]]-=1

    
    for i,j in temp.items():
       if j!=0:
           return False
    return True
    

print(isAnagram('anagram','nagaram'))     
print(isAnagram('aabbccdd','abcdabcd'))    
print(isAnagram('aabbccdd','abcdaecd')) 
print(isAnagram('cat','rat'))    