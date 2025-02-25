a=int(input("Enter a number:"))
s=0
while(a!=0):
    r=a%10
    s=s*10+r
    a=a//10
print("Reversed number:",s)
      
