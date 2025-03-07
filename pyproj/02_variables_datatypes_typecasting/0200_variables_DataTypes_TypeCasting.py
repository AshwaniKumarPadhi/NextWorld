var1 = "SRE"
var2 = "Principal"
var3 = 12
var4 = 24.67
var5 = "12"
var6 = "36.34"

print(var1,var2,var3,var4)
print(var1 + var2)
print(var3 + var4)
tt=type(str(var4))
print(tt)
print(type(var1))
print(type(var3))
print(var5 + var6)
print(int(var5) + float(var6))
print(10* str(int(var5) + float(var6)))
print(type(var4))
print(10* var1)
print(10* "Hello World!!!\n")

print("What's your name : ")
name = input()
print("Hi", name , "Welcome to Tomorrowland!!!")

age = input("Enter Your Age : ")
print("Hi", name , "Your age is : ", age)

num1 = input("Enter your first Monitor size : ")
num2 = input("Enter your second Monitor size : ")
print("Hi", name , "Total size of both monitors is : ", int(num1) + int(num2))