# Assignment No: 2

''' #Q1. Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on the rules:
# If salary < 30,000 → 5%
# If salary is 30,000–70,000 → 15%
# If salary > 70,000 → 25% 

salary = float(input("Enter your Salary in Rs: "))

if (salary < 30000):
    final_tax = 0.05*salary
    print(f"Your tax: {final_tax}Rs ")

elif salary in range(30000, 70000):
    final_tax = 0.15*salary
    print(f"Your tax: {final_tax}Rs ")

else:
    final_tax = 0.25*salary
    print(f"Your tax: {final_tax}Rs ") '''


''' #Q2. Write a function that takes two integers a and b and prints all even numbers between them (inclusive).

def even_num(a,b):
    for i in range(a,b +1):
        if(i % 2 == 0):
            print(i)

print(even_num(20,30)) '''

''' #Q3. Write a function that prints the digits of a number, n

def digit(n):
    for i in str(n):
        print(i)
digit(345) '''

''' #Q4. Write a function to return the count the number of digits in a number, n

def count_digit(n):
    count = 0
    for i in str(abs(n)):
        count += 1
    return count

n = int(input("Enter any number: "))
print(count_digit(n)) '''

''' #Q5. Write a function to return the sum of digits of a number, n.

def sum_digit(n):
    sum = 0
    for i in str(abs(n)):
       sum += int(i)
    return sum

n = int(input("Enter the number: "))
print("The sum of the digits are: ", sum_digit(n)) '''

''' #Q6. Write a function that takes a number n and returns the reverse of the number.

def reverse_num (n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev


n = int(input("Enter any number: "))
print("The Reverse number: ", reverse_num(n)) '''

''' #Q7.Write a function that takes a number n and checks whether the number is a palindrome or not.

def pallindrome_num(n):
    og = n
    rev = 0
    while n >0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if(rev == og):
        print(f'This is a pallindrome')
        print(f'input: ',og)
        print(f'reverse ',rev)
    else:
        print("This is not a pallindrome")

n = int(input("Enter a number:"))
pallindrome_num(n)'''

''' #QLetʼs create a Simple Calculator that performs arithmetic operations. Create a function that performs addition, subtraction, multiplication, or division based on the parameter.  calculator(a, b, operation) operation [ parameter can have values , , & .operation ‘+’ ‘-’ '*’ ‘/’]

def SimpleCalculator( a,b, operation ):

    if(operation == '+'):
        print("Addtion: ", a+b)
    
    elif(operation == "-"):
        print("Subtraction: ", a-b)

    elif(operation == "*"):
        print("Multiplication: ", a*b)
        
    elif(operation == "/"):
        if b != 0:
            print("Division: ", a/b)
        else:
            print("Cannot divide by zero!")
        
    else:
        print("Invalid Opearation!")

SimpleCalculator(2,3, "+")
SimpleCalculator(2,3, "*")
SimpleCalculator(2,3, "/")
SimpleCalculator(2,3, "-") '''

''' #Q9.Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.

def is_prime(n):
    if n < 2:
        return False

        for i in range(2, n-1):
            if(n%i == 0):
                return False

    return True

print(is_prime(7)) '''

#Q10.Letʼs create a “Number Guessing Game ”. Given a secret number (already decided by you), write a program that asks the user to guess it and prints:
# • if the guess is above the number"Too high"
# • if the guess is below"Too low"
# • if the guess matches"Correct!"

def game(n):
    
    sec_num = 7

    print("============ Guess the Number =============")
    while True:
        n = int(input("Enter the guessing number: "))
        if(n > 7):
            print("Too high!")
        elif(n < 7):
            print("Too low!")
        elif(n == 7):
            print("Correct guess")
            break

    return 1

n = 0
game(n)

