# WAP to check if a number entered by the user is odd or even

num=int(input("Enter the number: "))
if(num%2==0):
    print(num," is Even")
else:
    print(num, " is Odd")

# WAP to find the greatest of 3 numbers entered by the user

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
num3=int(input("Enter the third number : "))

if(num1>=num2 and num1>=num3):
    print(num1 ," is Greatest ")
elif(num2>=num1 and num2>=num3):
    print(num2," is Greatest")
else:
    print(num3, " is Greatest")


#WAP to check if a number is multiple of 7 or not 

n=int(input("Enter a number : "))
if(n%7==0):
    print(n , " is multiple of 7")
else:
    print(n, " is not multiple of 7")