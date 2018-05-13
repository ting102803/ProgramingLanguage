def sum(n):
    if n==1  or n==0:
        return n
    else:
        return n+sum(n-1)

def fibonacci(n):
    if n<2:
        return n
    else :
        return fibonacci(n-2)+fibonacci(n-1)


def factorial(n):
    if n==1 or n==0:
        return 1
    else :
        return n*factorial(n-1)

def decimal_to_binary(n):
    if n==0 :
        return 0
    else :
        return (n%2)+10*decimal_to_binary(n/2)

def TestRecursionFunction():
    print sum(100)
    print fibonacci(10)
    print factorial(10)
    print decimal_to_binary(15)

TestRecursionFunction()

