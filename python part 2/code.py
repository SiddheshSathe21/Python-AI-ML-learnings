''' age = int(input("Enter your age: "))
criminal_case = input("Do you have any criminal case, only (Yes/No): ")

if age >= 18:
    print("You can vote!!")
    print("You are allowed to drive!")
elif criminal_case == "Yes":
    print("You are detained !!")
else:
    print("You cannot vote!!")
    print("You cannot drive!!") '''

''' color = input("Enter Color: ")

if color == "red":
    print("STOP!")

elif color == "yellow":
    print("WAIT!")

elif color == "green":
    print("YOU CAN GO!")

else:
    print("Invalid color Input for traffic light.") '''


''' age = int(input("Enter your age: "))

if age < 13:
    print("CHILD")
elif age >= 13 and age <= 18:
    print("TEENAGER")
elif age > 18 and age < 100:
    print("ADULT")
else:
    print("Invalid age entered") '''

''' username = input("Enter username: ")
password = input("Enter Password: ")

if (username == "admin" and password == "pass"):
    print("You are logged in.")

elif username != "admin":
    print("invalid username.")

elif password != "pass":
    print("invalid Password.")

else:
    print("Invalid credentials.") '''


''' n = int(input("Enter the number: "))

if (n % 5 == 0):
    print("This is multiple of 5: ", n)

else:
    print("Its not multiple of 5")'''

''' n = int(input("ENter nay number: "))

if( n % 2 == 0):
    print("it is even no.", n)
else:
    print("Its a odd number", n) '''


''' username = input("Enter username: ")
password = input("Enter password: ")

if(username == "admin" and password == "pass"):
    print("You are logged in.")

else:
    if(username !="admin"):
        print("Invalid username")
    else:
        print("Invalid password") '''

''' # match case

color = input("Enter the color: ")

match color:
    case "green":
        print("go")
    case "red":
        print("stop")
    case "yellow":
        print("wait") '''


# loops

# for i in range(10):
#     print("hello world")
# i = 10
# while i >= 1 :
#     print(i,"Hello world")
#     i -= 1


# n = int(input("Enter number: "))
# i = 1
# while ( i <= 10 ):
#     print(f"{n}X{i} = ", n*i)
#     i += 1


# while(20 >= 5): #true condition
#     break
#     print("hjhjsh")
# print("breakkkkk")

# i = 1

# while(i <= 10):
#     if(i % 3 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1


# odd num 1 to 10

i = 0

while( i < 10 ):
    i += 1
    if( i % 2 == 0 ):
        continue
    print(i)



