def printStarTriangle(n):
    for i in range(0,n*2,2):
        print(' '* (((n*2)-(i+1))//2) +  ('*'*(i+1)))
    pass

printStarTriangle(10)