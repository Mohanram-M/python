'''
You are climbing a staircase . it takes n steps to reach to the top
Each time you can climb either 1 or 2 steps. in 
how many distint ways you can climb to the top.?

Example 1:
 Input : n=2
 output : 2

Example 2:

0 -> 1
1 -> 1

2 -> i can come from 0 or i can come from 1 here

so n -> i can come from n-1 or n-2 

dp[i] = dp[i-2]+dp[i-1]

'''

#With BruteForce and linear space
# time O(n) space O(n)
def climbstairsBrute(n):
    dp=[]
    dp.append(1);
    dp.append(1);
    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])
    
    return dp.pop()


#With BruteForce and linear time and constant space O(1)
# time O(n) space O(1)
def climbstairsBrute1(n):
    x,y,z=1,1,0
    for i in range(2,n+1):
        z=x+y
        x=y
        y=z
    
    return z





#With recursion and memoization
#time O(log(n)) ; space - O(n)
def climbStairsRec(m):
    mem=[1,1]

    def climbinner(n):
        if n<0: return 0
        elif n==0: return mem[0]
        else:
            x= mem[n-1] if len(mem)>n-1 else climbStairsRec(n-1)
            y= mem[n-2] if len(mem)>n-2 else climbStairsRec(n-2)
            return x+y

    return climbinner(m)

print(f'brute 4---{climbstairsBrute1(4)}')
print(f'brute1 4---{climbstairsBrute1(4)}')
print(f'brute rec mem 2 -- {climbStairsRec(2)}')
print(f'brute rec mem 3 -- {climbStairsRec(3)}')
print(f'brute rec mem 4 -- {climbStairsRec(4)}')