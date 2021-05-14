#factorial through function
#part a - function

def fact(x):
    i = 1
    fact = 1
    while i <= x:
        fact *= i
        i += 1
    return fact

#part b - Program

#prompt user for input
user_int = int(input("Please provide a positive whole number: "))

#check user_int < 0
if user_int < 0:
    print("We cannot use negative numbers")
else:
    fact = fact(user_int)
    print("The factorial of", user_int, "is", fact)
print("Finished!")