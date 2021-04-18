

def addTwo(a,b):

    while b>0:
        carry = a&b
        a=a^b
        b=carry <<1

    return a

print(addTwo(1,2))
print(addTwo(123,123))