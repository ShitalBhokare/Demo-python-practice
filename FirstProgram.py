# This is first python program

print("Hello World")
print("Shital Bhokare")

# Instead of using print() twice

print("Hello, My name is Shital." , "I live in Shirdi" )

# Variable - It is a name given to the memory location

length=40
breadth=30
print("Area of rectangle is ",length * breadth )

# type() function is used to identify the datatype of the variable

name = "Shital"
age = 22
marks = 87.60

print(type(name))
print(type(age))
print(type(marks))

# print sum 

a=20
b=30
sum=a+b    
print(sum)

# Arithmetic operator

a=30
b=5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)   # remaider
print(a**b)  # square

#Relational operator

a=50
b=20

print(a==b) #false
print(a!=b) #true
print(a>b) #true
print(a<b) #false
print(a>=b) #true
print(a<=b) #false


# assignment operator

num=10 
num+=10
print(num)

num-=10
print(num)

num*=10
print(num)

num/=10
print(num)

num%=2 
print(num)

num**=10
print(num)

#logical operator

# 1. not operator

print(not True)
print(not False)

a=30
b=50

print(not(a<b))   #not(true) -> false

# 2. and operator , or operator

val1=True
val2=True

print(val1 and val2) # and operator returns true when both conditions are true
print(a>=b and a<=b) # false and true -> false

print(val1 or val2) # or operator returns false when both conditions are false
print(a>=b or a<=b) #false or true->true

#type conversion(implicitly)

a=5
b=8.9
sum=a+b  #convert int to float automatically
print(sum)

#type casting(explicitly)

# a=4
# b="9"
# sum=a+b
# print(sum) #it gives error. because string and float cant add

a=4
b="9"
c=int(b)  #convert string into int manually i.e. explicitly
sum=a+c 
print(sum)

#input in python

name=input("Enter your Name : ")  #result of input() is string 
age=int(input("Enter your age : "))   
marks=float(input("Enter your marks : "))

print("Welcome" , name)
print("age : ",age)
print("marks : ",marks) 