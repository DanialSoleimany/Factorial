# Factorial 

number = int(input("Enter a number:\n"))

def factorial(number):

    if number < 0:
        print("Negative number is not allowed.")

    elif number == 0:
        print(f"The factorial of {number} is {1}")

    else:
        factorial = 1
        count = number

        while True:
            factorial *= count
            count -= 1
            if count <= 0:
                break

        print(f"The factorial of {number} is {factorial}")

factorial(number)