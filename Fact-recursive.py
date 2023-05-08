def fact_rec(x):
    if (x == 1):
        return 1
    else:
        return x * fact_rec(x-1)

x = int(input("number: "))

if (x == 0):
    print("Factorial of {0} is 1".format(x))
elif (x < 0):
    print("Negative number is not allowed")
else:
    print("Factorial of {0} is {1}".format(x, fact_rec(x)))
