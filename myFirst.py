# import random

# x = "this is first variable in the"
# print(x)

# # this is commented code
# y = 10
# print(y)

# if 5 > 2:
#     print("5 is greater than 2")
# if 5 < 3:
#     print("3 is greater than 3")

# print("Muhammad Muneeb is a website developer,")

# print("This is random number", random.randrange(1, 10))


# name = input("Enter the name ")
# print("the length of name is", len(name))

# dolor = "$this is $ and it $price$ is $$$"

# print(dolor.count("$"))


# light = "green"

# if light == "red":
#     print("Stop")
# elif light == "yellow":
#     print("Warning")
# elif(light == "green"):
#     print("Go")
# else:
#     print("Broken")

# age = 10
# if age >= 18:
#     print("you are eligible")
# else:
#     print("you are not eligible")


# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")


# number = int(input("Number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("The first largest number", a)
# elif b >= c and b >= a:
#     print("The second largest number", b)
# elif c >= a and c >= b:
#     print("The third largest number", c)
# else:
#     print("All numbers are equal")


# a = int(input("Enter number: "))

# if a % 5 == 0:
#     print("The number is divisible by 5")
# else:
#     print("The number is not divisible by 5")


# int
# float
# complex
# str
# bool
# list
# tuple
# set
# dict
# None


# 123
# 234.423
# "muneeb"
# True / False
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,10, 11, 12, 13, 14, 15, 16]
# num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# {"name": "Muneeb", "age": 25, "city": "Karachi"}


# i = 1

# while i <= 10:
#     print(i)
#     i += 1

# i, j, k = 0, 0, 0
# email = input("Enter your email: ")
# if len(email) >= 6:
#     if email[0].isalpha():
#         if ("@" in email) and (email.count("@") == 1):
#             if (email[-4] == ".") ^ (email[-3] == "."):
#                 for a in email:
#                     if a == a.isspace():
#                         i = 1
#                     elif a.isalpha():
#                         if a.isupper():
#                             k = 1
#                     elif a.isdigit():
#                         continue
#                     elif a == "_" or a == "." or a == "@":
#                         continue
#                     else:
#                         j = 1
#                 if i == 1 or k == 1 or j == 1:
#                     print("Wrong Email 5")
#             else:
#                 print("Wrong Email 4")
#         else:
#             print("Wrong Email 3")
#     else:
#         print("Wrong Email 2")
# else:
#     print("Wrong Email 1")


# import qrcode

# # Create QR code
# qr = qrcode.QRCode(
#     version=1,  # Size of the QR Code (1 se 40 tak hoti hai)
#     error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
#     box_size=10,  # Each box (pixel) size
#     border=4,  # Border size
# )

# qr.add_data("Hi I'm Muhammad Muneeb")  # Data add karna
# qr.make(fit=True)  # Automatically adjust size

# # Generate Image
# img = qr.make_image(fill="black", back_color="white")

# # Save image
# img.save("Muneeb.png")

# print("QR Code successfully saved as Muneeb.png!")


# def mistake(para1,para2):

# import random

# number = input("Roll the dice? (y/n): ").lower()

# if number == "y":
#     dice1 = random.randint(1, 10)
#     dice2 = random.randint(1, 10)
#     print("you rolled a dice ", dice1, ",", dice2)
# elif number == "n":
#     print("Thank you for playing!")
# else:
#     print("Invalid Choice")


# import random

# randNum = random.randint(1, 20)
# while True:
#     try:
#         userNum = int(input("Guess the number between 1 to 20 : "))
#         if userNum < randNum:
#             print("Too low!")
#         elif userNum > randNum:
#             print("Too high!")
#         else:
#             print("Congratulation, you guess the number")
#             break
#     except:
#         print("Enter a valid number")
