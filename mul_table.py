t=int(input("Enter the table number:"))
i=1
print("multiplication table using while")
while(i<11):
    print(i ,"*" ,t ,"=" ,i*t)
    i=i+1
i=1    
print("multiplication table using for")
for i in range(1,11,1):
     print(i ,"*" ,t ,"=" ,i*t)

    
