def sum(a,b):
    c=a+b
    return c
def dif():
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    c=a-b
    return c
def mul():
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    c=a*b
    print("Multiplication of a and b:",c)
def div(a,b):
    c=a//b
    print("Division of a and b:",c)
choice=(input("Enter your choice:"))
if(choice =='+'):
    a=int(input("Enter a value:")) 
    b=int(input("Enter b value:"))
    add=sum(a,b)
    print("Addition of a and b:",add)
elif(choice =='-'):
    sub=dif()
    print("Subtraction of a nad b:",dif)
elif (choice=='*'):
        mul()
elif (choice=='/'):
    a=int(input("Enter a value:")) 
    b=int(input("Enter b value:"))
    div(a,b)
