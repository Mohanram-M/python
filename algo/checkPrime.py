

def checkprime(n):
    h=n//2;
    for i in range(2,h+1):
        if n%i==0:
            return False
    return True


# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 

def genPrime(k):
    primes=[]
    for i in range(1,k+1):
        isprime=True
        for j in range(2,((i+1)//2)+1):
            if i%j==0:
                isprime=False
                break;
        if isprime:
            primes.append(i)
    return primes


print(genPrime(1000))


print(checkprime(7))
print(checkprime(1))
print(checkprime(8))
print(checkprime(13))