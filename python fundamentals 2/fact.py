# Write a function to find the factorial for 'n'.

def factorial(n):
    fact = 1

    for i in range(1, n+1):
        fact = fact * i #fact *= i
    return fact

n = int(input("Enter no: "))
print(factorial(n))