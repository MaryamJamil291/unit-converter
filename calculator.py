num1=input("Enter first number:")

A=int(num1)

num2=input("enter second number:")

B=int(num2)

Task=input("Which method do you want to do + - / * ? ")

Sum=A+B
Subtraction=A-B
Multiplication=A*B
Division=A/B

if Task=="+":
    print("Result 1=","sum is",Sum)

elif Task=="-":
    print("Result 2=","subtraction is",Subtraction)

elif Task=="*":
    print("Result 3=","Multiplication is",Multiplication)
    
elif Task=="/":
    print("Result 4=","Division is",Division)
    
else:
    print("invalid operation")


    
    