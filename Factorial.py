def fact(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact

x = int(input("number: "))       

if (x == 0):
    print("Factorial of {0} is 1".format(x))
elif (x < 0):
    print("Negative number is not allowed")
else:
    print("Factorial of {0} is {1}".format(x, fact(x)))
