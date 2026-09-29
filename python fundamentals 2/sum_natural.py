# Calculate the first 'n' natural numbers.

# sum = 0

n = int(input("Enter a number: "))

for i in range(1, n+1 ):
    # sum += i
    i = int( n * (n+1)/2 ) #alternate method without using another variable
    
# print("sum = ",sum)
print(i)