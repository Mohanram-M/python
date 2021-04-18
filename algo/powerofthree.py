'''
Given an integer n return true if its power of three . otherwise return false.

solve with out loops or recursion
'''

def checkthreepow(n):
     
    return (1162261467 % n == 0)
    

print(f'9 -- {checkthreepow(9)}')
print(f'3 -- {checkthreepow(3)}')
print(f'6 -- {checkthreepow(6)}')
print(f'27 -- {checkthreepow(27)}')
print(f'0 -- {checkthreepow(0)}')