a=int(input("Enter the first number:"))
b=int(input("Enter second number:"))
n=1
while(n==1):
    c=input("Enter the operator(+,-,*,/,**,%):")
    if c=='+':
        print("Addition undergoes")
        print("Sum is",a+b)
    elif c=='-':
        print("Subtraction undergoes")
        print("Difference is",a-b)
    elif c=='*':
        print("Multiplication undergoes")
        print("Product is",a*b)
    elif c=='/':
        print("Division undergoes")
        print("Result is",a/b)
    elif c=='**':
        print("Square operation undergoes")
        print("Square is",a**b)
    elif c=='%':
        print("Remainder is",a%b)
    else:
        print("Invalid Operator!!")
    s=input("Do you want to continue(y/n):")
    if s=='y':
        n=1
    else:
        n=0
        print("Exit")
