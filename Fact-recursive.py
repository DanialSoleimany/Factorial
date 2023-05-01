def fact_rec(x):
    if (x == 1):
        return 1
    else:
        return x * fact_rec(x-1)

x = int(input("number: "))

print(fact_rec(x))