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

#Q3. Write a function that prints the digits of a number, n

def digit(n):
    for i in str(n):
        print(i)
digit(345)





