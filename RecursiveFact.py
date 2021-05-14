#factorial of a number using recursive
#define factorial function
def fact(n):
    """Function to return the factorial of a number using recursion"""
    print(n)
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

#Prompt user for positive integer
number = int(input("Please provide a positive whole number: "))

if number < 0:
    print("Error, we cannot find the factorial of a negative number.")
else:
    print("The Factorial of", number, "is", fact(number))